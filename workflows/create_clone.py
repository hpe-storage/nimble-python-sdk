# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, KEY_SNAP, KEY_CLONE,\
    cleanup_vol, cleanup_snapshots
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, clone_name, vol_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_vol(client, clone_name, noisy)
    cleanup_snapshots(client, vol_name, noisy)
    cleanup_vol(client, vol_name, noisy)


def force_cleanup(client, clone_name, vol_name, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    do_cleanup(client, clone_name, vol_name, noisy=False)


def do_setup(client, config, noisy):
    screen('\nDoing Setup:', noisy)
    vol_name = config[KEY_VOL]
    vol = client.volumes.get(name=vol_name)
    # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
    if vol is not None:
        force_cleanup(client, config[KEY_CLONE], vol_name, noisy)
    # Create volume
    vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
    screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    return vol.attrs['id']


def create_clone(client, noisy, cleanup):
    config = read_config()
    try:
        vol_id = do_setup(client, config, noisy)
        screen('\nWORKFLOW: Create Clone:', noisy)
        # Create a snapshot
        snap = client.snapshots.create(name=config[KEY_SNAP], vol_id=vol_id)
        screen('\tCreated snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.attrs['id']), noisy)
        # Create a clone from a snapshot
        clone = client.volumes.create(name=config[KEY_CLONE], base_snap_id=snap.attrs['id'], clone=True)
        screen('\tCreated clone: {}, Id: {}'.format(clone.attrs['name'], clone.attrs['id']), noisy)
        if cleanup:
            do_cleanup(client, clone.attrs['name'], config[KEY_VOL], noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    create_clone(client, noisy, cleanup)
