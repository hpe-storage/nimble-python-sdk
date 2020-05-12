# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login
from nimbleclient.v1 import NimOSAPIError
from publish_volume import publish_volume


def do_cleanup(noisy):
    screen('\nDoing Cleanup:', noisy)
    screen('\tNo cleanup required for detach_volume workflow', noisy)


def force_cleanup(noisy):
    do_cleanup(noisy)


def do_setup(client, noisy):
    screen('\nDoing Setup:', noisy)
    acr_id = publish_volume(client, noisy, cleanup=False, show_header=False)
    return acr_id


def offline_and_delete_volume(client, vol_id, noisy):
    screen('\nWORKFLOW: Offline and Delete Volume - {}'.format(vol_id), noisy)
    vol = client.volumes.get(id=vol_id)
    if vol is None:
        print('ERROR: Volume {} does not exist.'.format(vol_id))
    else:
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tOfflined and Deleted volume: {}, Id: {}'.format(vol.attrs['name'], vol_id), noisy)


def detach_volume(client, noisy, cleanup, show_header=True):
    acr_id = do_setup(client, noisy)
    try:
        if show_header:
            screen('\nWORKFLOW: Detach Volume for ACR - {}'.format(acr_id), noisy)
        acr = client.access_control_records.get(acr_id)
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tDeleted ACR: {}'.format(acr.attrs['id']), noisy)
        client.initiator_groups.delete(id=acr.attrs['initiator_group_id'])
        screen('\tDeleted initiator group: {}, Id: {}'.format(acr.attrs['initiator_group_name'],
                                                              acr.attrs['initiator_group_id']), noisy)
        offline_and_delete_volume(client, acr.attrs['vol_id'], False)
        screen('\tOfflined and Deleted volume: {}, Id: {}'.format(acr.attrs['vol_name'], acr.attrs['vol_id']), noisy)
        if cleanup:
            do_cleanup(noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    detach_volume(client, noisy, cleanup)
