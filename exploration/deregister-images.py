import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    image_name = "adhoc-p1-barclays-image"

    print("Describing Images for: " + image_name)
    images = ec2.describe_images(
        Filters=[{'Name': 'is-public', 'Values': ['false']},
                 {'Name': 'name', 'Values': [image_name + '*']}],
        Owners=['self']
    )['Images']

    print(images)
    sorted_images = sorted(images, key=lambda x: x['CreationDate'], reverse=True)

    for img in sorted_images:
        print(img['ImageId'])

    print("Dead Images")
    for dead_image in sorted_images[2:]:
        print(dead_image['ImageId'])
        ec2.deregister_image(
            ImageId=dead_image['ImageId']
        )
