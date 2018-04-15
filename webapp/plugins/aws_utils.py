import boto3

class AWSUtils():
    def __init__(self):
        self.session = boto3.Session(profile_name='lydell-testing')
        self.ec2 = self.session.resource('ec2')

    def retrieve_instances(self, name):
        self.instances = self.ec2.instances.filter(
            Filters=[{'Name': 'tag:Name', 'Values': [name]}, {'Name': 'tag:Application', 'Values': ['Simple-aws']}])
        return self.instances

    def retrieve_instances_by_application(self, type):
        self.instances = self.ec2.instances.filter(
            Filters=[{'Name': 'tag:Application', 'Values': [type]}])
        return self.instances

    def create_instances(self, name, number):
        self.instances = self.ec2.create_instances(
            ImageId='ami-43874721',
            MinCount=1,
            MaxCount= int(number),
            InstanceType = 't2.micro',
            NetworkInterfaces=[{
                'AssociatePublicIpAddress': False,
                'DeviceIndex': 0
            }],
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [
                        {
                            'Key': 'Name',
                            'Value': name
                        },
                        {
                            'Key': 'Application',
                            'Value': 'Simple-aws'
                        },
                    ]
                },
            ],
            )
        return self.instances

    def stop_instances(self, application):
        self.retrieve_instances_by_application(application)
        return self.instances.stop()

    def terminate_instances(self, name):
        self.retrieve_instances(name)
        self.instances.terminate()
        return self.instances
