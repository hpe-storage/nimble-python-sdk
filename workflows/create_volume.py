import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login, cleanup
from nimbleclient.v1 import NimOSAPIError


def create_volume(client, vol_name, noisy):
    vol_id = None
    try:
        screen('\nWORKFLOW: Create Volume - {}'.format(vol_name), noisy)
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        vol_id = vol.id
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()
    return vol_id


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy)
    cleanup(client, {'vol_id_list': [vol_id]}, noisy)
