import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login
from nimbleclient.v1 import NimOSAPIError
from create_volume import create_volume
from publish_volume import publish_volume


def offline_and_delete_volume(client, vol_id, noisy):
    screen('\nWORKFLOW: Offline and Delete Volume - {}'.format(vol_id), noisy)
    vol = client.volumes.get(id=vol_id)
    if vol is None:
        print('ERROR: Volume {} does not exist.'.format(vol_id))
    else:
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tOfflined and Deleted volume: {}, Id: {}'.format(vol.attrs['name'], vol_id), noisy)


def detach_volume(client, acr_id, noisy):
    try:
        screen('\nWORKFLOW: Detach Volume for ACR - {}'.format(acr_id), noisy)
        acr = client.access_control_records.get(acr_id)
        if acr is None:
            screen('ERROR: ACR {} does not exist.'.format(acr_id), noisy)
            return False
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tDeleted ACR: {}'.format(acr.attrs['id']), noisy)
        client.initiator_groups.delete(id=acr.attrs['initiator_group_id'])
        screen('\tDeleted initiator group: {}'.format(acr.attrs['initiator_group_name']), noisy)
        offline_and_delete_volume(client, acr.attrs['vol_id'], False)
        screen('\tOfflined and Deleted volume: {}, Id: {}'.format(acr.attrs['vol_name'], acr.attrs['vol_id']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy=False)
    acr_id = publish_volume(client, vol_id, False)
    screen('\nCreated and published volume to detach.'.format(vol_id), noisy)
    screen('\tVol Id: {}'.format(vol_id), noisy)
    screen('\tACR Id: {}'.format(acr_id), noisy)
    detach_volume(client, acr_id, noisy)
