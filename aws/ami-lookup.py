import boto3
import argparse

from pprint import pprint

parser = argparse.ArgumentParser(description='AWS AMI Look up')
parser.add_argument('--profile', dest='profile', default='default',
                    help='AWS session profile to use')
parser.add_argument('--ami-prefix', dest='prefix', required=True,
                    help='Prefix to the AMI name you wish to look up')
parser.add_argument('--sort-by', dest='sort_by', default='Name',
                    help='Sorts by desired output field. Defaults to Name.')
parser.add_argument('--arch', dest='arch', default='x86_64',
                    help='AMI Architecture')
parser.add_argument('--display', dest='display', type=int,
                    help='Number of results to display')

args = parser.parse_args()

session = boto3.Session(profile_name=args.profile)
ec2_client = session.client('ec2')

results = ec2_client.describe_images(
    Filters=[
        {
            'Name': 'name',
            'Values': [
                args.prefix + "*"
            ]
        },
        {
            'Name': 'state',
            'Values': [
                'available'
            ]
        },
        {
            'Name': 'architecture',
            'Values': [
                args.arch
            ]
        }
    ]
)

sorted_images = sorted(
    results['Images'], key=lambda key: key[args.sort_by], reverse=True
)

if args.display is not None:
    count = args.display
else:
    count = len(sorted_images)

for image in range(count):
    print(sorted_images[image]['Name'])
