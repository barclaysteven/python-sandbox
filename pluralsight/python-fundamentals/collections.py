test_ami_name_event = {
    'blueprint': 'my-blueprint',
    'definition': {
        'type': 'Ami Bakery v1_0',
        'source': [
            {
                'region': 'us-east-1',
                'ami_name': 'paas-base-ami'
            }
        ],
        'target_ami_name': 'custom-ami',
        'target_ami_description': 'my custom ami'
    },
    'artifact_url': 'http://s3.amazonaws.com/my-bucket/my-data.zip'
}

print(test_ami_name_event['definition']['source'][0]['ami_name'])
