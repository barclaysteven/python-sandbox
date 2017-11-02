import boto3


ec2 = boto3.client('ec2', region_name='us-east-1')

results = ec2.describe_images(
    Owners=[
        'self'
    ],
    Filters=[
        {
            'Name': 'name',
            'Values': [
                'paas-vpc.*'
            ]
        }
    ]
)

print(results)

sorted_images = sorted(results['Images'], key=lambda key: key['CreationDate'], reverse=True)
print(sorted_images[0]['ImageId'])
