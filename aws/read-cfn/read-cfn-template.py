import yaml
import boto3
import json

TEST_CONFIG = "test-config.yaml"
TEST_ACCOUNT_ID = "221453998677"


class POC:
    def __init__(self):
        print("Inside __init__")
        session = boto3.Session(profile_name="play-fh2")
        self.iam_client = session.client('iam', region_name='us-east-1')

    def main(self):
        test_config = yaml.load(open(TEST_CONFIG), Loader=yaml.FullLoader)

        for test_cases in test_config['TestCases']:
            modified_file = "mod." + test_cases['TemplateName']

            with open(test_cases['TemplateName'], 'r') as infile, \
                 open(modified_file, 'w') as outfile:
                data = infile.read()
                data = data.replace("!Sub", '').replace("${AWS::AccountId}", TEST_ACCOUNT_ID)
                outfile.write(data)

            template = yaml.load(open(modified_file), Loader=yaml.FullLoader)

            for assertion in test_cases['PolicyAssertions']:
                test_policy_name = assertion['PolicyName']
                for resource in template['Resources']:
                    properties = template['Resources'].get(resource)['Properties']
                    managed_policy_name = properties['ManagedPolicyName']
                    if managed_policy_name == test_policy_name:
                        policy_doc = properties['PolicyDocument']
                        break
                for test in assertion['Tests']:
                    test_name = test['Name']
                    actions = test['Actions']
                    expected_decision = test['ExpectedDecision']
                    test_resources = test['Resources']

                    print("Executing test: " + test_name)
                    if "Context" in test:
                        key_name = test['Context']['KeyName']
                        value = test['Context']['Value']
                        context_type = test['Context']['Type']
                        response = self.iam_client.simulate_custom_policy(
                            PolicyInputList=[json.dumps(policy_doc)],
                            ActionNames=actions,
                            ResourceArns=test_resources,
                            ContextEntries=[
                                {
                                    'ContextKeyName': key_name,
                                    'ContextKeyValues': [value],
                                    'ContextKeyType': context_type
                                }
                            ]
                        )
                    else:
                        response = self.iam_client.simulate_custom_policy(
                            PolicyInputList=[json.dumps(policy_doc)],
                            ActionNames=actions,
                            ResourceArns=test_resources
                        )

                    evaluation_results = response['EvaluationResults']
                    # print(evaluation_results)
                    for evaluation_result in evaluation_results:
                        action = evaluation_result['EvalActionName']
                        decision = evaluation_result['EvalDecision']
                        resource_name = evaluation_result['EvalResourceName']
                        if decision != expected_decision:
                            print(action + ' has result of ' + decision + ' but wanted ' + expected_decision + ' for '
                                  + resource_name + '::Fail')
                        else:
                            print(action + ' has result of ' + decision + ' for ' + resource_name + '::Pass')
                    print()


if __name__ == '__main__':
    tester = POC()
    tester.main()
