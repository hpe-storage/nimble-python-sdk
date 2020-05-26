# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import sys
import json
import getpass
from nimbleclient.v1 import NimOSClient
from nimbleclient.exceptions import NimOSAuthenticationError

config_file = 'workflow_config.json'
# config file fields
KEY_HNAME = 'hostname'
KEY_UNAME = 'username'
KEY_PWD = 'password'
KEY_VOL = 'volume_name'
KEY_IG = 'initiator_group_name'
KEY_MK = 'master_key_name'
KEY_MK_PHRASE = 'master_key_phrase'
KEY_PS = 'protection_sched'
# genrated config fields
KEY_ENCRYPT_VOL = 'encrypted_vol_name'
KEY_CLONE = 'clone_name'
KEY_SNAP = 'snap_name'
KEY_VOLCOLL = 'volcoll_name'


def screen(msg, noisy, end='\n'):
    if noisy:
        print(msg, end=end)


def usage(file, noisy=True):
    screen('Usage:', noisy)
    screen('\t{} [--query_login] [--cleanup]'.format(file), noisy)
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
    cleanup = False
    valid_params = ['--query_login', '--cleanup']
    if len(param_list) > 3:
        usage(file)
    for param in param_list[1:]:
        if param not in valid_params:
            usage(file)
    if '--query_login' in param_list:
        query_login = True
    if '--cleanup' in param_list:
        cleanup = True
    return query_login, cleanup


def login(query_login, noisy):
    client = None
    hostname, username, password = None, None, None
    config_dict = read_config()
    if KEY_HNAME in config_dict:
        hostname = config_dict[KEY_HNAME]
    if KEY_UNAME in config_dict:
        username = config_dict[KEY_UNAME]
    if KEY_PWD in config_dict:
        password = config_dict[KEY_PWD]
    cred_list = [hostname, username, password]
    if not query_login and (None in cred_list or '' in cred_list):
        screen('\n\tFailed to find Nimble Array login credentials in {}.'.format(config_file), noisy)
        screen('\tUpdate that file to remove login query.\n', noisy)
        query_login = True
    if query_login:
        hostname = input('Enter the hostname: ')
        username = input('Enter the username: ')
        password = getpass.getpass(prompt='Enter the password: ', stream=None)
    screen('\nAttempting to establish connection to array:', noisy)
    screen('\tHostname: {}'.format(hostname), noisy)
    screen('\tUsername: {}'.format(username), noisy)
    # Instantiate nimble client object
    try:
        client = NimOSClient(hostname, username, password)
        screen('\tConnection successful!', noisy)
    except NimOSAuthenticationError:
        screen('ERROR: Invalid credentials.', noisy)
        sys.exit(1)
    return client


def cleanup_vol_prep(client, volume_name, noisy):
    svols = client.volumes.list()
    # Delete any clones of the volume
    for svol in svols:
        lvol = client.volumes.get(id=svol.attrs['id'])
        if lvol.attrs['clone'] and lvol.attrs['parent_vol_name'] == volume_name:
            client.volumes.offline(id=lvol.attrs['id'])
            client.volumes.delete(id=lvol.attrs['id'])
            screen('\tCleanup Vol Prep "{}": Removed clone "{}"'.format(volume_name, lvol.attrs['name']), noisy)
    # Disassociate the vol from any volume volume_collections
    vol = client.volumes.get(name=volume_name)
    if vol.attrs['volcoll_name'] != '':
        client.volumes.dissociate(id=vol.attrs['id'])
        screen('\tCleanup Vol Prep "{}": Dissassociated from volume collection "{}"'.
               format(volume_name, vol.attrs['volcoll_name']), noisy)


def cleanup_vol(client, volume_name, noisy):
    vol = client.volumes.get(name=volume_name)
    if vol is not None:
        cleanup_vol_prep(client, volume_name, noisy)
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tCleanup Vol "{}": Offlined and deleted Id: {}'.format(vol.attrs['name'], vol.attrs['id']), noisy)
    else:
        screen('\tCleanup Vol "{}": Volume does not exist.'.format(volume_name), noisy)
    return None


def create_vol(client, volume_name, noisy):
    vol = client.volumes.get(name=volume_name)
    if vol is None:
        vol = client.volumes.create(name=volume_name, size=50, limit_iops=12000)
        screen('\tCreate Volume "{}": Created Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    else:
        screen('\tCreate Volume "{}": Already exists. Continuing.'.format(vol.attrs['name']), noisy)
    return vol


def clone_vol(client, volume_name, snap_id, noisy):
    clone = client.volumes.get(name=volume_name)
    if clone is None:
        clone = client.volumes.create(name=volume_name, base_snap_id=snap_id, clone=True)
        screen('\tCreate Clone "{}": Created Id: {}'.format(clone.attrs['name'], clone.id), noisy)
    else:
        screen('\tCreate Clone "{}": Already exists. Continuing.'.format(clone.attrs['name']), noisy)
    return clone


def create_encrypted_vol(client, volume_name, noisy):
    vol = client.volumes.get(name=volume_name)
    if vol is None:
        vol = client.volumes.create(name=volume_name, size=50, limit_iops=12000, encryption_cipher='aes_256_xts')
        screen('\tCreate Encrypted Volume "{}": Created Id: {}'.format(vol.attrs['name'], vol.id), noisy)
    else:
        screen('\tCreate Encrypted Volume "{}": Already exists. Continuing.'.format(vol.attrs['name']), noisy)
    return vol


def associate_vol(client, vol_id, volume_coll, noisy):
    vol = client.volumes.get(id=vol_id)
    if vol is not None:
        if vol.attrs['volcoll_name'] == volume_coll.attrs['name']:
            screen('\tAssociate Volume: Volume "{}" already associated with volume collection "{}". Continuing.'.
                   format(vol.attrs['name'], volume_coll.attrs['name']), noisy)
        else:
            asoc = client.volumes.associate(id=vol_id, volcoll=volume_coll)
            screen('\tAssociate Volume: Volume "{}" associated with volume vollection "{}"'.
                   format(vol.attrs['name'], asoc['volcoll_name']), noisy)
    else:
        screen('\tAssociate Volume: Volume does not exist. Continuing. Id: {}'.format(vol_id), noisy)


def find_encrypted_vols(client):
    encrypted_vols = []
    vols = client.volumes.list(detail=True)
    for item in vols:
        if item.attrs['encryption_cipher'] != 'none':
            encrypted_vols.append(item.attrs['name'])
    return encrypted_vols


def cleanup_master_key(client, mk_name, noisy):
    mk = client.master_key.get(name=mk_name)
    encrypted_vol_list = find_encrypted_vols(client)
    if mk is not None and len(encrypted_vol_list) == 0:
        client.master_key.delete(mk.attrs['id'])
        screen('\tCleanup Master Key "{}": Deleted Id: {}'.format(mk.attrs['name'], mk.attrs['id']), noisy)
    elif mk is None:
        screen('\tCleanup Master Key "{}": Key does not exist'.format(mk_name), noisy)
    elif len(encrypted_vol_list) > 0:
        screen('\tCleanup Master Key "{}": Found {} encrypted volumes'.format(mk_name, len(encrypted_vol_list)), noisy)
        screen('\tCleanup Master Key "{}": All encrypted volumes must be removed prior to deleting the master key.'.
               format(mk_name), noisy)


def create_master_key(client, mk_name, mk_phrase, noisy):
    mk = client.master_key.get(name=mk_name)
    if mk is None:
        mk = client.master_key.create(name=mk_name, passphrase=mk_phrase)
        screen('\tCreate Master Key "{}": Created Id: {}'.format(mk.attrs['name'], mk.attrs['id']), noisy)
    else:
        screen('\tCreate Master Key "{}": Already exists. Continuing.'.format(mk.attrs['name']), noisy)
    return mk


def cleanup_access_control_rec(client, acr_id, noisy):
    acr = client.access_control_records.get(id=acr_id)
    if acr is not None:
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tCleanup Acccess Control Record: Deleted Id: {}'.format(acr.attrs['id']), noisy)
    else:
        screen('\tCleanup Acccess Control Record: ACR does not exist. Id: {}'.format(acr_id), noisy)


def create_access_control_rec(client, ig_id, vol_id, noisy):
    acr = None
    acr_list = client.access_control_records.list()
    for item in acr_list:
        temp_acr = client.access_control_records.get(id=item.attrs['id'])
        if temp_acr.attrs['initiator_group_id'] == ig_id and temp_acr.attrs['vol_id'] == vol_id:
            acr = temp_acr
            break
    if acr is None:
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig_id, vol_id=vol_id)
        screen('\tCreate Access Control Record: Created Id: {}'.format(acr.attrs['id']), noisy)
    else:
        screen('\tCreate Access Control Record: Already exists. Continuing.'.format(acr.attrs['id']), noisy)
    return acr


def cleanup_initiator_group(client, ig_name, noisy):
    ig = client.initiator_groups.get(name=ig_name)
    if ig is not None:
        client.initiator_groups.delete(id=ig.attrs['id'])
        screen('\tCleanup Initiator Group "{}": Deleted Id: {}'.format(ig.attrs['name'], ig.attrs['id']), noisy)
    else:
        screen('\tCleanup Initiator Group "{}": Initiator group does not exist'.format(ig_name), noisy)


def create_initiator_group(client, ig_name, noisy):
    ig = client.initiator_groups.get(name=ig_name)
    if ig is None:
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreate Initiator Group "{}": Created Id: {}'.format(ig.attrs['name'], ig.id), noisy)
    else:
        screen('\tCreate Initiator Group "{}": Already exists. Continuing.'.format(ig.attrs['name']), noisy)
    return ig


def cleanup_snapshots(client, vol_name, noisy):
    # Deletes ALL the snapshots on the specified volume
    # screen('\tCleaning up snapshots for volume: {}'.format(vol_name), noisy)
    vol = client.volumes.get(name=vol_name)
    if vol is not None:
        snap_list = client.snapshots.list(vol_name=vol.attrs['name'])
        for snap in snap_list:
            client.snapshots.delete(id=snap.attrs['id'])
            screen('\tCleanup Snapshots of vol "{}": Deleted "{}", Id: {}'.format(vol_name, snap.attrs['name'],
                   snap.attrs['id']), noisy)
    else:
        screen('\tCleanup Snapshots of vol "{}": Volume does not exist.'.format(vol_name), noisy)


def cleanup_snapshot(client, snap_id, noisy):
    snap = client.snapshots.get(id=snap_id)
    if snap is not None:
        client.snapshots.delete(id=snap_id)
        screen('\tCleanup Snapshot "{}": Deleted Id: {}'.format(snap.attrs['name'], snap_id), noisy)
    else:
        screen('\tCleanup Snapshot "{}": Snapshot does not exist.'.format(snap_id), noisy)


def create_snap(client, snap_name, vol_id, noisy):
    snap = None
    snap_list = client.snapshots.list(vol_id=vol_id)
    for item in snap_list:
        if item.attrs['name'] == snap_name:
            snap = client.snapshots.get(item.attrs['id'])
            break
    if snap is None:
        snap = client.snapshots.create(name=snap_name, vol_id=vol_id)
        screen('\tCreate Snapshot "{}": Created Id: {}'.format(snap.attrs['name'], snap.id), noisy)
    else:
        screen('\tCreate Snapshot "{}": Already exists. Continuing.'.format(snap.attrs['name']), noisy)
    return snap


def cleanup_protection_schedule(client, ps_name, noisy):
    ps = client.protection_schedules.get(name=ps_name)
    if ps is not None:
        client.protection_schedules.delete(id=ps.attrs['id'])
        screen('\tCleanup Protection Schedule "{}": Deleted Id: {}'.format(ps.attrs['name'], ps.attrs['id']), noisy)
    else:
        screen('\tCleanup Protection Schedule "{}": Protection Schedule does not exist'.format(ps_name), noisy)


def create_protection_schedule(client, ps_name, volcoll_id, noisy):
    ps = client.protection_schedules.get(name=ps_name)
    if ps is None:
        ps_days = "monday,tuesday,wednesday,thursday,friday"
        ps_info = "just a schedule"
        ps_period = "minutes"
        ps = client.protection_schedules.create(name=ps_name, period=60, period_unit=ps_period,
                                                days=ps_days, description=ps_info,
                                                volcoll_or_prottmpl_id=volcoll_id,
                                                volcoll_or_prottmpl_type='volume_collection',
                                                num_retain=2)
        screen('\tCreate Protection Schedule "{}": Created Id: {}'.format(ps.attrs['name'], ps.id), noisy)
    else:
        screen('\tCreate Protection Schedule "{}": Already exists. Continuing.'.format(ps.attrs['name']), noisy)
    return ps


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
            screen('\tCleanup Volume Collection "{}": Disassociated vol "{}"'.
                   format(vc.attrs['name'], vol['name']), noisy)
    if vc is not None:
        client.volume_collections.delete(id=vc.id)
        screen('\tCleanup Volume Collection "{}": Deleted Volume Collection. Id: {}'.
               format(vc.attrs['name'], vc.attrs['id']), noisy)


def create_volume_collection(client, vc_name, noisy):
    vc = client.volume_collections.get(name=vc_name)
    if vc is None:
        vc = client.volume_collections.create(name=vc_name, description='created by workflow')
        screen('\tCreate Volume Collection "{}": Created Id: {}'.format(vc.attrs['name'], vc.id), noisy)
    else:
        screen('\tCreate Volume Collection "{}": Already exists. Continuing.'.format(vc.attrs['name']), noisy)
    return vc
