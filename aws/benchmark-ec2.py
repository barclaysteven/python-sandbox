import boto3
import time

session = boto3.Session(profile_name='fh2-us-east-1')

ec2 = session.client('ec2')
waiter = ec2.get_waiter('instance_running')

instance_types = ['t2.micro', 't2.small', 't2.medium', 't2.large', 'm5.large', 'c5.large']

for instance_type in instance_types:
    start = time.time()
    print("Instance Type: " + instance_type)
    ec2_resp = ec2.run_instances(ImageId='ami-0ff8a91507f77f867',
                                 SubnetId='subnet-8935a4e7',
                                 SecurityGroupIds=[
                                     'sg-0655fc9a4d38020c7'
                                 ],
                                 MinCount=1,
                                 MaxCount=1,
                                 InstanceType=instance_type,
                                 UserData='IyEvYmluL2Jhc2gKCmZ1bmN0aW9uIGdldF9jb250ZW50cygpIHsKICAgIGlmIFsgLXggIiQod2hpY2ggY3VybCkiIF07IHRoZW4KICAgICAgICBjdXJsIC1zIC1mICIkMSIKICAgIGVsaWYgWyAteCAiJCh3aGljaCB3Z2V0KSIgXTsgdGhlbgogICAgICAgIHdnZXQgIiQxIiAtTyAtCiAgICBlbHNlCiAgICAgICAgZGllICJObyBkb3dubG9hZCB1dGlsaXR5IChjdXJsLCB3Z2V0KSIKICAgIGZpCn0KCnJlYWRvbmx5IElERU5USVRZX1VSTD0iaHR0cDovLzE2OS4yNTQuMTY5LjI1NC8yMDE2LTA2LTMwL2R5bmFtaWMvaW5zdGFuY2UtaWRlbnRpdHkvZG9jdW1lbnQvIgpyZWFkb25seSBUUlVFX1JFR0lPTj0kKGdldF9jb250ZW50cyAiJElERU5USVRZX1VSTCIgfCBhd2sgLUZcIiAnL3JlZ2lvbi8geyBwcmludCAkNCB9JykKcmVhZG9ubHkgREVGQVVMVF9SRUdJT049InVzLWVhc3QtMSIKcmVhZG9ubHkgUkVHSU9OPSIke1RSVUVfUkVHSU9OOi0kREVGQVVMVF9SRUdJT059IgoKcmVhZG9ubHkgU0NSSVBUX05BTUU9ImF3cy1pbnN0YWxsLXNzbS1hZ2VudCIKcmVhZG9ubHkgU0NSSVBUX1VSTD0iaHR0cHM6Ly9hd3Mtc3NtLWRvd25sb2Fkcy0kUkVHSU9OLnMzLmFtYXpvbmF3cy5jb20vc2NyaXB0cy8kU0NSSVBUX05BTUUiCgpjZCAvdG1wCmdldF9jb250ZW50cyAiJFNDUklQVF9VUkwiID4gIiRTQ1JJUFRfTkFNRSIKY2htb2QgK3ggIiRTQ1JJUFRfTkFNRSIKLi8iJFNDUklQVF9OQU1FIiAtLXJlZ2lvbiAiJFJFR0lPTiIKCnNsZWVwIDUKZWNobyAic2xlcHQgNSBzZWNvbmRzIg==',
                                 TagSpecifications=[
                                     {
                                         'ResourceType': 'instance',
                                         'Tags': [
                                             {
                                                 'Key': 'Name',
                                                 'Value': 'adhoc-p1-barclays-benchmarks'
                                             },
                                             {
                                                 'Key': 'council',
                                                 'Value': 'PlatformSvc-DPT-VPC'
                                             },
                                             {
                                                 'Key': 'deploy-meta',
                                                 'Value': 'blueprint: null manual: VPC-Resource'
                                             }
                                         ]
                                     }
                                 ])
    instance_id = ec2_resp['Instances'][0]['InstanceId']
    waiter.wait(
        InstanceIds=[
            instance_id
        ],
        WaiterConfig={
            'Delay': 2,
            'MaxAttempts': 60
        }
    )
    end = time.time()
    delta = end - start
    print('Creation Time (in seconds): {:>9.2f}'.format(delta))

    ec2_terminate_resp = ec2.terminate_instances(
        InstanceIds=[
            instance_id
        ]
    )
