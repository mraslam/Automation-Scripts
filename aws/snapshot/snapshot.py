import boto3
import subprocess
import pandas as pd
from datetime import datetime

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

instanceIds = []

with open('servers.txt') as f:
    instances_list = [instance.rstrip() for instance in f]
instances = set(instances_list)

instanceDf = pd.read_csv("servers.csv")

instanceDict = instanceDf.set_index('Unique Asset Identifier').to_dict()['IP Address']

def get_instance_id():
    for key, value in instanceDict.items():
        for instance in instances:
            if instance == value:
                instanceIds.append(key)


# print(instanceIds)

ec2_client = boto3.client('ec2')

def create_snapshots():
    for instanceId in instanceIds:
        response = ec2_client.create_snapshots(
            Description=f"MANUAL_SNAP_{date}",
            InstanceSpecification={
                'InstanceId': instanceId,
                'ExcludeBootVolume': False
            },
            TagSpecifications=[
                    {
                        'ResourceType': 'snapshot',
                        'Tags': [
                            {
                                'Key': 'InstanceID',
                                'Value': f"{instanceId}"
                            },
                        ]
                    },
                ],
            CopyTagsFromSource='volume'
        )
        # print(len(response['Snapshots']))



if __name__ == '__main__':

    get_instance_id()
    create_snapshots()




# add function to check status of snapshot creation
# add sleep
# add instance name to either name/tag
