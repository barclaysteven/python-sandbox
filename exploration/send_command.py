import boto3

ssm = boto3.client('ssm')
blueprint_name = "my-blueprint"
auto_doc = "paas-cloudformation-deploy-paas-vpc-docker-bakery-prod-dev-docker-bakery-DockerRunDocument-15CBZ4N87EXEJ"

response = ssm.send_command(InstanceIds=["i-0882c21998d221411"],
                            DocumentName=auto_doc,
                            Parameters={
                                "documentName": ["runValidateCommand.yml"],
                                "documentParameters": [
                                    '{"DockerImageName": "' + blueprint_name + '" }'
                                ]
                            })

print(response)
