import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login, cleanup
from nimbleclient.v1 import NimOSAPIError
from create_volume import create_volume


def create_snapshot(client, vol_name, noisy):
    snap_id = None
    try:
        screen('\nWORKFLOW: Create Snapshot for Volume - {}'.format(vol_name), noisy)
        res = client.volumes.list()
        vol = None
        for item in res:
            if item.attrs['name'] == vol_name:
                vol = item
                break
        if vol is None:
            screen('ERROR: Volume {} does not exist.'.format(vol_name), noisy)
            return None
        # Create a snapshot
        snap = client.snapshots.create(name=vol_name + 'snap', vol_id=vol.attrs['id'])
        screen('\tCreated a snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.id), noisy)
        snap_id = snap.attrs['id']
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()
    return snap_id


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy=False)
    screen('\nCreated volume {} to snapshot.'.format(vol_id), noisy)
    snap_id = create_snapshot(client, get_config_vol_name(), noisy)
    cleanup(client, {'snap_id_list': [snap_id], 'vol_id_list': [vol_id]}, noisy)
