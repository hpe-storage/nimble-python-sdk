# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login, read_config, KEY_VOL, KEY_SNAP,\
    cleanup_snapshots, cleanup_snapshot, cleanup_vol
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, snap_id, vol_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_snapshot(client, snap_id, noisy)
    cleanup_vol(client, vol_name, noisy)


def force_cleanup(client, vol_name, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    cleanup_snapshots(client, vol_name, noisy=False)
    cleanup_vol(client, vol_name, noisy=False)


def do_setup(client, config, noisy):
    screen('\nDoing Setup:', noisy)
    vol_name = config[KEY_VOL]
    # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
    if client.volumes.get(name=vol_name) is not None:
        force_cleanup(client, vol_name, noisy)
    vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
    screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    return vol.id, vol.attrs['name']


def create_snapshot(client, noisy, cleanup):
    config = read_config()
    try:
        vol_id, vol_name = do_setup(client, config, noisy)
        screen('\nWORKFLOW: Create Snapshot for Volume - {}'.format(vol_name), noisy)
        vol = client.volumes.get(name=vol_name)
        # Create a snapshot
        snap = client.snapshots.create(name=config[KEY_SNAP], vol_id=vol.attrs['id'])
        screen('\tCreated a snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.id), noisy)
        if cleanup:
            do_cleanup(client, snap.id, vol_name, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    create_snapshot(client, noisy, cleanup)
