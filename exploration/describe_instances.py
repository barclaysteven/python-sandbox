def all_instances_stopped():
    return {
        'Reservations': [
            {
                'Instances': [
                    {
                        'InstanceId': 'i-123456789abcdef12',
                        'State': {
                            'Code': 80,
                            'Name': 'running'
                        },
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'docker-build-agents'
                            }
                        ]
                    }
                ]
            },
            {
                'Instances': [
                    {
                        'InstanceId': 'i-a1b2c3d4e5f622312',
                        'State': {
                            'Code': 80,
                            'Name': 'running'
                        },
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'docker-build-agents'
                            }
                        ]
                    }
                ]
            },
            {
                'Instances': [
                    {
                        'InstanceId': 'i-abcdef123456789ab',
                        'State': {
                            'Code': 80,
                            'Name': 'running'
                        },
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': 'docker-build-agents'
                            }
                        ]
                    }
                ]
            }
        ]
    }


def get_instance_id(build_agents):
    for instances in build_agents:
        for instance in instances['Instances']:
            if instance['State']['Name'] == "stopped":
                instance_id = instance['InstanceId']
                return instance_id
    else:
        return "wait"


build_agents = all_instances_stopped()['Reservations']
print(get_instance_id(build_agents))

