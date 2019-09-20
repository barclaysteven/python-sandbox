import boto3
import json
import authentication


def lambda_handler(event, context):
    client = authentication.Authentication()


    subject = event['Records'][0]['Sns']['Subject']
    message_json = json.loads(event['Records'][0]['Sns']['Message'])
    message_desc = message_json['Description']
    message_event = message_json['Event']
    print(subject)
    print(message_desc)
    print(message_event)
    print(context.invoked_function_arn)
    print(context.invoked_function_arn.split(":")[4])

    log_message = {
        "subject": subject,
        "description": message_desc,
        "asg_event": message_event
    }

    return log_message
