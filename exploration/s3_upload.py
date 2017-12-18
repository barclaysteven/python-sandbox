import boto3
import json


s3_bucket = 'paas-vpc-ami-bakery-dev-artifacts-us-east-1-074150922133'
blueprint = 'paas-vpc-ami-bakery-at'
artifact = 'paas-vpc-ami-bakery-at.zip'

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(s3_bucket, blueprint + '/' + artifact)
s3_object.delete()
print("deleted s3 object: {}".format(s3_object))

s3_object.upload_file(artifact)
