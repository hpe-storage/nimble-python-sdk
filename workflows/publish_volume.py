# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, cleanup_vol,\
    cleanup_access_control_record, cleanup_initiator_group
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, acr_id, noisy):
    screen('\nDoing Cleanup:', noisy)
    acr = client.access_control_records.get(acr_id)
    cleanup_access_control_record(client, acr.attrs['id'], noisy)
    cleanup_initiator_group(client, acr.attrs['initiator_group_name'], noisy)
    cleanup_vol(client, acr.attrs['vol_name'], noisy)   # Cleanup clone vol


def force_cleanup(client, config, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    res = client.access_control_records.list()
    for item in res:
        acr = client.access_control_records.get(id=item.attrs['id'])
        if acr.attrs['vol_name'] == config[KEY_VOL]:
            do_cleanup(client, acr.attrs['id'], noisy=False)
            break


def do_setup(client, config, noisy, show_header=True):
    if show_header:
        screen('\nDoing Setup:', noisy)
    # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
    if client.volumes.get(name=config[KEY_VOL]) is not None:
        force_cleanup(client, config, noisy)
    vol = client.volumes.create(name=config[KEY_VOL], size=50, limit_iops=12000)
    screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    return vol.id


def publish_volume(client, noisy, cleanup, show_header=True):
    config = read_config()
    try:
        vol_id = do_setup(client, config, noisy, show_header)
        if show_header:
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
        screen('\tCreated ACR: {}'.format(acr.attrs['id']), noisy)
        if cleanup:
            do_cleanup(client, acr.attrs['id'], noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    publish_volume(client, noisy, cleanup)
