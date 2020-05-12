# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import sys
import json
import getpass
from nimbleclient.v1 import Client, NimOSAuthenticationError

config_file = 'workflow_config.json'
KEY_VOL = 'vol_name'
KEY_ENCRYPT_VOL = 'encrypted_vol_name'
KEY_IG = 'ig_name'
KEY_MK = 'mk_name'
KEY_MK_PHRASE = 'mk_phrase'
KEY_CLONE = 'clone_name'
KEY_SNAP = 'snap_name'
KEY_PS = 'protection_sched'
KEY_VOLCOLL = 'volcoll_name'


def screen(msg, noisy, end='\n'):
    if noisy:
        print(msg, end=end)


def usage(file, noisy=True):
    screen('Usage:', noisy)
    screen('\t{} [--query_login] [--skip_cleanup]'.format(file), noisy)
    sys.exit(1)


def read_config():
    data = None
    config_dict = None
    with open(config_file, 'r') as myfile:
        data = myfile.read()
    if data is not None:
        config_dict = json.loads(data)
        config_dict[KEY_ENCRYPT_VOL] = config_dict[KEY_VOL] + 'encrypted'
        config_dict[KEY_CLONE] = config_dict[KEY_VOL] + 'clone'
        config_dict[KEY_SNAP] = config_dict[KEY_VOL] + 'snap'
        config_dict[KEY_VOLCOLL] = config_dict[KEY_VOL] + 'volcoll'
    if config_dict is None:
        screen('ERROR: Failed to read config file', noisy=True)
        sys.exit(1)
    return config_dict


def handle_params(file, param_list):
    query_login = False
    cleanup = True
    valid_params = ['--query_login', '--skip_cleanup']
    if len(param_list) > 3:
        usage()
    for param in param_list[1:]:
        if param not in valid_params:
            usage()
    if '--query_login' in param_list:
        query_login = True
    if '--skip_cleanup' in param_list:
        cleanup = False
    return query_login, cleanup


def login(query_login, noisy):
    client = None
    if query_login:
        hostname = input('Enter the hostname: ')
        username = input('Enter the username: ')
        password = getpass.getpass(prompt='Enter the password: ', stream=None)
    else:
        config_dict = read_config()
        hostname = config_dict['hostname']
        username = config_dict['username']
        password = config_dict['password']
    screen('\nAttempting to establish connection to array:', noisy)
    screen('\tHostname: {}'.format(hostname), noisy)
    screen('\tUsername: {}'.format(username), noisy)
    # Instantiate nimble client object
    try:
        client = Client(hostname, username, password)
        screen('\tConnection successful!', noisy)
    except NimOSAuthenticationError:
        screen('ERROR: Invalid credentials.', noisy)
        sys.exit(1)
    return client


def cleanup_vol(client, volume_name, noisy):
    vol = client.volumes.get(name=volume_name)
    if vol is not None:
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tDeleted volume: {}, Id: {}'.format(vol.attrs['name'], vol.attrs['id']), noisy)


def cleanup_master_key(client, mk_name, noisy):
    mk = client.master_key.get(name=mk_name)
    if mk is not None:
        client.master_key.delete(mk.attrs['id'])
        screen('\tDeleted master key: {}, Id: {}'.format(mk.attrs['name'], mk.attrs['id']), noisy)


def cleanup_access_control_record(client, acr_id, noisy):
    acr = client.access_control_records.get(id=acr_id)
    if acr is not None:
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tDeleted ACR: {}'.format(acr.attrs['id']), noisy)


def cleanup_initiator_group(client, ig_name, noisy):
    ig = client.initiator_groups.get(name=ig_name)
    if ig is not None:
        client.initiator_groups.delete(id=ig.attrs['id'])
        screen('\tDeleted initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.attrs['id']), noisy)


def cleanup_snapshots(client, vol_name, noisy):
    # Deletes ALL the snapshots on the specified volume
    # screen('\tCleaning up snapshots for volume: {}'.format(vol_name), noisy)
    vol = client.volumes.get(name=vol_name)
    if vol is not None:
        snap_list = client.snapshots.list(vol_name=vol.attrs['name'])
        for snap in snap_list:
            client.snapshots.delete(id=snap.attrs['id'])
            screen('\tDeleted snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.attrs['id']), noisy)


def cleanup_snapshot(client, snap_id, noisy):
    snap = client.snapshots.get(id=snap_id)
    if snap is not None:
        client.snapshots.delete(id=snap_id)
        screen('\tDeleted snapshot: {}, Id: {}'.format(snap.attrs['name'], snap_id), noisy)


def cleanup_protection_schedule(client, ps_name, noisy):
    ps = client.protection_schedules.get(name=ps_name)
    if ps is not None:
        client.protection_schedules.delete(id=ps.attrs['id'])
        screen('\tDeleted protection schedule: {}, Id: {}'.format(ps.attrs['name'], ps.attrs['id']), noisy)
        # print(ps.attrs)


def cleanup_volume_collection(client, vc_name, noisy):
    vols = client.volumes.list()
    vc = None
    for vol_short in vols:
        vol = client.volumes.get(id=vol_short.attrs['id'])
        if vol.attrs['volcoll_name'] == vc_name:
            vc = client.volume_collections.get(id=vol.attrs['volcoll_id'])
    if vc is not None and vc.attrs['volume_list'] is not None:
        for vol in vc.attrs['volume_list']:
            client.volumes.dissociate(id=vol['id'])
            screen('\tDisassociated vol {} from volume collection {}'.format(vol['name'], vc.attrs['name']), noisy)
    if vc is not None:
        client.volume_collections.delete(id=vc.id)
        screen('\tDeleted volume collection {}'.format(vc.attrs['name']), noisy)
