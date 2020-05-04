import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login, cleanup
from nimbleclient.v1 import NimOSAPIError
from create_volume import create_volume


def publish_volume(client, vol_id, noisy):
    acr_id = None
    try:
        screen('\nWORKFLOW: Publish Volume - {}'.format(vol_id), noisy)
        vol = client.volumes.get(id=vol_id)
        vol_name = vol.attrs['name']
        # Create an initiator group
        ig_name = vol_name + 'ig'
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Create the ACR
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig.attrs['id'],
                                                   vol_id=vol.attrs['id'])
        screen('\tCreated access control record: {}'.format(acr.attrs['id']), noisy)
        acr_id = acr.attrs['id']
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()
    return acr_id


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy=False)
    screen('\nCreated volume {} to publish.'.format(vol_id), noisy)
    acr_id = publish_volume(client, vol_id, noisy)
    cleanup(client, {'acr_id_list': [acr_id], 'vol_id_list': [vol_id]}, noisy)
