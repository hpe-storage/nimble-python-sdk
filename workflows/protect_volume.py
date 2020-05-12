# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, KEY_PS, KEY_VOLCOLL,\
    cleanup_protection_schedule, cleanup_volume_collection, cleanup_vol
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, ps_name, vc_name, vol_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_protection_schedule(client, ps_name, noisy)
    cleanup_volume_collection(client, vc_name, noisy)
    cleanup_vol(client, vol_name, noisy)


def force_cleanup(client, ps_name, vc_name, vol_name, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    do_cleanup(client, ps_name, vc_name, vol_name, noisy=False)


def do_setup(client, config, noisy):
    screen('\nDoing Setup:', noisy)
    vol_name = config[KEY_VOL]
    # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
    vol = client.volumes.get(name=vol_name)
    if vol is not None:
        force_cleanup(client, config[KEY_PS], config[KEY_VOLCOLL], vol_name, noisy)
    vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
    screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    return vol.id, vol.attrs['name']


def protect_volume(client, noisy, cleanup):
    config = read_config()
    try:
        vol_id, vol_name = do_setup(client, config, noisy)
        screen('\nWORKFLOW: Protect Volume - {}'.format(vol_id), noisy)
        # Get the volume
        vol = client.volumes.get(vol_id)
        # Create a volume collection
        volcoll1 = client.volume_collections.create(name=config[KEY_VOLCOLL], description="created by workflow")
        screen('\tCreated volume collection: {}, Id: {}'.format(volcoll1.attrs['name'], volcoll1.id), noisy)
        # Associate a volume with the volume collection
        asoc = client.volumes.associate(id=vol.attrs['id'], volcoll=volcoll1)
        screen('\tAssociated volume: {}, with volume vollection: {}'.format(
               asoc['id'], asoc['volcoll_name']), noisy)
        # Create a protection schedule
        ps_name = config[KEY_PS]
        ps_days = "monday,tuesday,wednesday,thursday,friday"
        ps_info = "just a schedule"
        ps = client.protection_schedules.create(name=ps_name, period=60, period_unit="minutes",
                                                days=ps_days, description=ps_info,
                                                volcoll_or_prottmpl_id=volcoll1.id,
                                                volcoll_or_prottmpl_type='volume_collection',
                                                num_retain=2)
        screen('\tCreated protection schedule: {}, Id: {}'.format(ps.attrs['name'], ps.id), noisy)
        if cleanup:
            do_cleanup(client, ps_name, config[KEY_VOLCOLL], vol_name, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    protect_volume(client, noisy, cleanup)
