import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login, cleanup
from nimbleclient.v1 import NimOSAPIError
from create_volume import create_volume
from create_snapshot import create_snapshot
from publish_volume import publish_volume
from detach_volume import detach_volume


def clone_volume(client, vol_name, noisy):
    try:
        screen('\nWORKFLOW: Clone Volume - {}'.format(vol_name), noisy)
        snap_id = create_snapshot(client, vol_name, noisy=False)
        clone_name = vol_name + 'clone'
        clone = client.volumes.create(name=clone_name, base_snap_id=snap_id, clone=True)
        screen('\tCloned volume: {}, Id: {}'.format(clone.attrs['name'], clone.id), noisy)
        clone_acr_id = publish_volume(client, clone.attrs['id'], noisy=False)
        screen('\tPublished cloned volume: {}'.format(clone_name), noisy)
        detach_volume(client, clone_acr_id, noisy=False)
        screen('\tDeleted cloned volume: {}'.format(clone_name), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy=False)
    vol = client.volumes.get(id=vol_id)
    screen('\nCreated volume to clone: {}, Id: {}'.format(vol.attrs['name'], vol_id), noisy)
    clone_volume(client, vol.attrs['name'], noisy)
    cleanup(client, {'vol_id_list': [vol_id]}, noisy)
