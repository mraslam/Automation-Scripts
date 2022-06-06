import boto3
import botocore
import time


if __name__ == '__main__':

    instance_ids = []
    volume_id = []
    snapshot_id = []

    with open('servers.txt') as f:
        hosts = [host.rstrip() for host in f]

    ec2 = boto3.resource('ec2')
    instance_iterator = ec2.instances.filter(
            Filters=[
            {
                'Name': 'private-ip-address',
                'Values': hosts
            },
        ],
    )

    for instance_iter in instance_iterator:
        instance_ids.append(instance_iter.id)

    for ins in instance_ids:
        instance = ec2.Instance(ins)
        volumes = instance.volumes.all()
        for volume in volumes:
            volume_id.append(volume.id)

    client = boto3.client('ec2')

    for vol in volume_id:
        response = client.create_snapshot(VolumeId=vol)
        snapshot_id.append(response["SnapshotId"])

    snapshot_complete_waiter = client.get_waiter('snapshot_completed')

    try:
        print("Snapshot Creation In Progress...Please wait!")
        time.sleep(3)
        print("...")

        snapshot_complete_waiter.wait(SnapshotIds=snapshot_id)

        print("Snapshot Creation is now Completed")

    except botocore.exceptions.WaiterError as e:
        if "Max attempts exceeded" in e.message:
            print("Snapshot did not complete in 600 seconds")
        else:
            print(e.message)