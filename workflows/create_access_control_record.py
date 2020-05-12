# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login, read_config, KEY_VOL, KEY_IG,\
    cleanup_access_control_record, cleanup_initiator_group, cleanup_vol
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, acr_id, ig_name, vol_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_access_control_record(client, acr_id, noisy)
    cleanup_initiator_group(client, ig_name, noisy)
    cleanup_vol(client, vol_name, noisy)


def force_cleanup(client, ig_name, vol_name, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    res = client.access_control_records.list()
    for item in res:
        acr = client.access_control_records.get(id=item.attrs['id'])
        if acr.attrs['vol_name'] == vol_name:
            do_cleanup(client, acr.attrs['id'], ig_name, vol_name, noisy=False)
            break


def create_access_control_record(client, noisy, cleanup):
    config = read_config()
    vol_name = config[KEY_VOL]
    ig_name = config[KEY_IG]
    try:
        screen('\nWORKFLOW: Create Access Control Record:', noisy)
        # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
        vol = client.volumes.get(name=vol_name)
        if vol is not None:
            force_cleanup(client, ig_name, vol_name, noisy)
        # Create a volume
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        # Create an initiator group
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Create the ACR
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig.attrs['id'],
                                                   vol_id=vol.attrs['id'])
        screen('\tCreated ACR: {}'.format(acr.attrs['id']), noisy)
        if cleanup:
            do_cleanup(client, acr.attrs['id'], ig_name, vol_name, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    create_access_control_record(client, noisy, cleanup)
