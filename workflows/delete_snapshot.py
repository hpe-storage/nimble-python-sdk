import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login, cleanup
from nimbleclient.v1 import NimOSAPIError
from create_volume import create_volume
from create_snapshot import create_snapshot


def delete_snapshot(client, snap_id, noisy):
    try:
        screen('\nWORKFLOW: Delete Snapshot - {}'.format(snap_id), noisy)
        snap = client.snapshots.get(id=snap_id)
        if snap is None:
            screen('ERROR: Snapshot does not exist: {}'.format(snap_id), noisy)
            return
        # Delete snapshot
        client.snapshots.delete(id=snap_id)
        screen('\tDeleted snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.id), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy=False)
    screen('\nCreated volume to snapshot: {}'.format(vol_id), noisy)
    snap_id = create_snapshot(client, get_config_vol_name(), noisy=False)
    screen('Created snapshot: {}'.format(snap_id), noisy)
    delete_snapshot(client, snap_id, noisy)
    cleanup(client, {'vol_id_list': [vol_id]}, noisy)
