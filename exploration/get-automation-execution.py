import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='dev-fh5')
ssm = session.client('ssm', region_name='us-east-1')


def get_string_list():
    try:
        results = ssm.get_parameter(Name='/priv-1/paas-aws-user-mgmt/1234321/admin')
        return results
    except ClientError as e:
        raise e


try:
    response = get_string_list()
except ClientError as e:
    if e.response['Error']['Code'] == "ParameterNotFound":
        admin_string = "123454321"
    else:
        raise e

try:
    print(admin_string)
    ssm.put_parameter(Name='/priv-1/paas-aws-user-mgmt/1234321/admin',
                      Value=admin_string, Type='StringList', Overwrite=True)
except ClientError as e:
    print(e.response)
