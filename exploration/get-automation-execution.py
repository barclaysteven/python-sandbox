import boto3


ssm = boto3.client('ssm', region_name='us-east-1')

results = ssm.get_automation_execution(AutomationExecutionId="1c992fd0-c50c-11e7-b3b8-1957b5544865")['AutomationExecution']

step_executions = results['StepExecutions']

print(results)

outputs = {}

for step in step_executions:
    outputs[step['StepName']] = step['Outputs']

print(outputs)
