event = {
    'Images': [
        {'CreationDate': '2017-03-21T23:03:39.000Z',
         'ImageId': 'ami-abcd1234',
         'Name': 'paas-base-ami',
         'Tags': [{'Key': 'securityLevel', 'Value': 'VPCAdmin'},
                  {'Key': 'council', 'Value': 'testAmiCleanup'},
                  {'Key': 'deploy-meta',
                   'Value': 'blueprint: null manual: TestAmiBakery'}]},
        {'CreationDate': '2017-04-21T22:03:39.000Z',
         'ImageId': 'aami-efgh5678',
         'Name': 'paas-base-ami',
         'Tags': [{'Key': 'securityLevel', 'Value': 'VPCAdmin'},
                  {'Key': 'council', 'Value': 'testAmiCleanup'},
                  {'Key': 'deploy-meta',
                   'Value': 'blueprint: null manual: TestAmiBakery'}]},
        {'CreationDate': '2017-05-21T21:03:39.000Z',
         'ImageId': 'ami-abcd5678',
         'Name': 'paas-base-ami',
         'Tags': [{'Key': 'securityLevel', 'Value': 'VPCAdmin'},
                  {'Key': 'council', 'Value': 'testAmiCleanup'},
                  {'Key': 'deploy-meta',
                   'Value': 'blueprint: null manual: TestAmiBakery'}]},
        {'CreationDate': '2017-06-21T22:03:39.000Z',
         'ImageId': 'ami-efgh1234',
         'Name': 'paas-base-ami',
         'Tags': [{'Key': 'securityLevel', 'Value': 'VPCAdmin'},
                  {'Key': 'council', 'Value': 'testAmiCleanup'},
                  {'Key': 'deploy-meta',
                   'Value': 'blueprint: null manual: TestAmiBakery'}]}
    ]
}

images = event['Images']
print(images)
sorted_images = sorted(event['Images'], key=lambda k: k['CreationDate'], reverse=True)
print(sorted_images[0]['ImageId'])
