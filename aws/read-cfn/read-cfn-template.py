import yaml

test_policy = "test-policy.yaml"


class POC:
    def __init__(self):
        print("Inside __init__")

    def main(self):
        template = yaml.load(open(test_policy), Loader=yaml.FullLoader)
        print(template)
        resources = template['Resources']

        for resource in resources:
            properties = resources.get(resource)['Properties']
            policies = properties['Policies']
            for policy in policies:
                policy_doc = policy['PolicyDocument']
                print(policy_doc)
        # policies = yaml.load(open('policies.yaml'), Loader=yaml.FullLoader)
        # for policy in policies['policies']:
        #     print(policy['policyName'])
        #     actions = policy['actions']
        #     print(actions)
        #     permission = policy['permission']
        #     print(permission)
        #     resources = policy['resources']
        #     if 'context' in policy:
        #         context = policy['context']
        #         key_name = context['keyName']
        #         context_type = context['type']
        #         value = context['value']
        #         response = self.iam.simulate_principal_policy(
        #             PolicySourceArn=source_policy_arn,
        #             ActionNames=actions,
        #             ResourceArns=resources,
        #             ContextEntries=[
        #                 {
        #                     'ContextKeyName': key_name,
        #                     'ContextKeyValues': [value],
        #                     'ContextKeyType': context_type
        #                 }
        #             ]
        #         )
        #     else:
        #         response = self.iam.simulate_principal_policy(
        #             PolicySourceArn=source_policy_arn,
        #             ActionNames=actions,
        #             ResourceArns=resources
        #             )
        #     evaluation_results = response['EvaluationResults']
        #     for evaluation_result in evaluation_results:
        #         action = evaluation_result['EvalActionName']
        #         decision = evaluation_result['EvalDecision']
        #         resource_name = evaluation_result['EvalResourceName']
        #         if decision != permission:
        #             print(action + ' has result of ' + decision + ' but wanted ' + permission + ' for '
        #                   + resource_name + '::Fail')
        #         else:
        #             print(action + ' has result of ' + decision + ' for ' + resource_name + '::Pass')
        #     print()


if __name__ == '__main__':
    tester = POC()
    tester.main()
