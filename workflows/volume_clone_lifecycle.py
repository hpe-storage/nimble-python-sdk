import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login
from nimbleclient.v1 import NimOSAPIError


def volume_clone_lifecycle(client, vol_name, noisy):
    try:
        screen('\nWORKFLOW: Volume/Clone Lifecycle:', noisy)
        # Create a volume
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        # Create a snapshot
        snap_name = vol_name + 'snap'
        snap = client.snapshots.create(name=snap_name, vol_id=vol.attrs['id'])
        screen('\tCreated snapshot: {}'.format(snap.attrs['name']), noisy)
        # Create a clone from a snapshot
        clone_name = vol_name + 'clone'
        clone = client.volumes.create(name=clone_name, base_snap_id=snap.attrs['id'], clone=True)
        screen('\tCreated clone: {}'.format(clone.attrs['name']), noisy)
        # Delete a clone
        client.volumes.offline(clone.attrs['id'])
        client.volumes.delete(clone.attrs['id'])
        screen('\tDeleted clone: {}'.format(clone.attrs['name']), noisy)
        # Delete a snapshot
        client.snapshots.delete(id=snap.attrs['id'])
        screen('\tDeleted snapshot: {}'.format(snap.attrs['name']), noisy)
        # Delete a volume
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tDeleted volume: {}'.format(vol.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    volume_clone_lifecycle(client, get_config_vol_name(), noisy)
