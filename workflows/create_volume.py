# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, cleanup_vol
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, vol_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_vol(client, vol_name, noisy)


def force_cleanup(vol_name, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    do_cleanup(client, vol_name, noisy=False)


def create_volume(client, noisy, cleanup):
    config = read_config()
    try:
        vol_name = config[KEY_VOL]
        screen('\nWORKFLOW: Create Volume - {}'.format(vol_name), noisy)
        # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
        if client.volumes.get(name=vol_name) is not None:
            force_cleanup(vol_name, noisy)
        vol = client.volumes.create(name=config[KEY_VOL], size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        if cleanup:
            do_cleanup(client, vol_name, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    create_volume(client, noisy, cleanup)
