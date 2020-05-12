# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, cleanup_access_control_record,\
    KEY_VOL, KEY_SNAP, KEY_CLONE, cleanup_initiator_group, cleanup_vol, cleanup_snapshots
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, clone_acr_id, snap_name, vol_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    acr = client.access_control_records.get(clone_acr_id)
    cleanup_access_control_record(client, acr.attrs['id'], noisy)
    cleanup_initiator_group(client, acr.attrs['initiator_group_name'], noisy)
    cleanup_vol(client, acr.attrs['vol_name'], noisy)   # Cleanup clone vol
    cleanup_snapshots(client, vol_name, noisy)
    cleanup_vol(client, vol_name, noisy)    # Cleanup orig vol


def force_cleanup(client, config, noisy):
    screen('\tCleaning up existing workflow objects...YO', noisy)
    res = client.access_control_records.list()
    for item in res:
        acr = client.access_control_records.get(id=item.attrs['id'])
        if acr.attrs['vol_name'] == config[KEY_CLONE]:
            do_cleanup(client, acr.attrs['id'], config[KEY_SNAP], config[KEY_VOL], noisy=True)
            break


def do_setup(client, config, noisy):
    screen('\nDoing Setup:', noisy)
    # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
    if client.volumes.get(name=config[KEY_VOL]) is not None:
        force_cleanup(client, config, noisy)
    vol = client.volumes.create(name=config[KEY_VOL], size=50, limit_iops=12000)
    screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    return vol.id, vol.attrs['name']


def clone_and_publish_volume(client, noisy, cleanup):
    config = read_config()
    try:
        vol_id, vol_name = do_setup(client, config, noisy)
        screen('\nWORKFLOW: Clone And Publish Volume - {}'.format(vol_name), noisy)
        snap = client.snapshots.create(name=config[KEY_SNAP], vol_id=vol_id)
        screen('\tCreated a snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.id), noisy)
        clone = client.volumes.create(name=config[KEY_CLONE], base_snap_id=snap.attrs['id'], clone=True)
        screen('\tCloned volume: {}, Id: {}'.format(clone.attrs['name'], clone.id), noisy)
        # Create an initiator group
        ig_name = config[KEY_CLONE] + 'ig'
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Create the ACR
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig.attrs['id'],
                                                   vol_id=clone.attrs['id'])
        screen('\tCreated ACR: {}'.format(acr.attrs['id']), noisy)
        if cleanup:
            do_cleanup(client, acr.attrs['id'], snap.attrs['name'], vol_name, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    clone_and_publish_volume(client, noisy, cleanup)
