import sys
from nimbleclient.v1 import NimOSClient
from nimbleclient.exceptions import NimOSAuthenticationError, NimOSAPIError
from workflow_common import read_config, KEY_HNAME, KEY_UNAME, KEY_PWD, create_vol, create_initiator_group,\
     create_access_control_rec, cleanup_vol, create_master_key, cleanup_initiator_group,\
     cleanup_master_key, create_snap, cleanup_snapshot, cleanup_access_control_rec

hostname = 'brian-va.vlab.nimblestorage.com'
username = 'admin'
password = 'admin'


def analyze(myobj, name=''):
    if (name != ''):
        print('\tMembers of class: {}'.format(name))
    else:
        print('\tAnalysis:')
    obj_list = dir(myobj)
    for num, val in enumerate(obj_list):
        print('\t\t{}) {}'.format(num, val))


def print_attrs(myobj, prefix=''):
    print('{}Fields in attrs dictionary:'.format(prefix))
    for key, val in myobj.attrs.items():
        print('{}\t {} : {}'.format(prefix, key, val))


def access_control_record_create(client, acr_name, prefix):
    vol_name = acr_name + 'testvol'
    ig_name = acr_name + 'testig'
    vol = create_vol(client, vol_name, noisy=True)
    ig = create_initiator_group(client, ig_name, noisy=True)
    acr = create_access_control_rec(client, ig.attrs['id'], vol.attrs['id'], noisy=True)
    if acr is None:
        print('ERROR: Failed to create ACR. Id: {}'.format(acr.attrs['id']))
        return None
    return acr.attrs['id']


def access_control_record_delete(client, acr_id, query, prefix):
    try:
        acr = client.access_control_records.get(acr_id)
    except NimOSAPIError:
        acr = None
    if acr is None:
        print('{}ERROR: ACR {} does not exist.'.format(prefix, acr_id))
        return False
    cleanup_access_control_rec(client, acr_id, noisy=True)
    if query:
        answer = input('\tDelete Associated Initiator Group "{}" and Volume "{}": '.
                       format(acr.attrs['initiator_group_name'], acr.attrs['vol_name']))
    else:
        answer = 'y'
    if answer.lower() == 'y' or answer.lower() == 'yes':
        cleanup_initiator_group(client, acr.attrs['initiator_group_name'], noisy=True)
        cleanup_vol(client, acr.attrs['vol_name'], noisy=True)


def show_object_type(client, cur_num, obj_type, obj_list, obj_dict):
    obj_num = 0
    for obj in obj_list:
        obj_num += 1
        obj_dict[obj_type] += 1
        pnum = obj_num+cur_num
        if 'name' in obj.attrs:
            print('\t\t{}) {}: {}, Id: {}'.format(pnum, obj_type.upper(), obj.attrs['name'], obj.attrs['id']))
        else:
            print('\t\t{}) {}: Id: {}'.format(pnum, obj_type.upper(), obj.attrs['id']))
    return obj_num


def show_all_objects(client):
    objs = {'volumes': 0, 'snapshots': 0, 'volume collections': 0, 'initiator groups': 0, 'acrs': 0,
            'protection schedules': 0, 'master keys': 0}

    print('\n\tObjects on Array:')
    num = 0
    vol_list = client.volumes.list()
    for vol in vol_list:
        num += 1
        objs['volumes'] += 1
        print('\t\t{}) VOLUME: {}, Id: {}'.format(num, vol.attrs['name'], vol.attrs['id']))
        snap_list = client.snapshots.list(vol_name=vol.attrs['name'])
        for snap in snap_list:
            num += 1
            objs['snapshots'] += 1
            print('\t\t{}) \tSNAPSHOT: {}, Id: {}'.format(num, snap.attrs['name'], snap.attrs['id']))
    obj_list = client.volume_collections.list()
    num += show_object_type(client, num, 'volume collections', obj_list, objs)
    obj_list = client.initiator_groups.list()
    num += show_object_type(client, num, 'initiator groups', obj_list, objs)
    obj_list = client.access_control_records.list()
    num += show_object_type(client, num, 'acrs', obj_list, objs)
    obj_list = client.protection_schedules.list()
    num += show_object_type(client, num, 'protection schedules', obj_list, objs)
    obj_list = client.master_key.list()
    num += show_object_type(client, num, 'master keys', obj_list, objs)

    print('\n\tFound {} total objects:'.format(num))
    for key in objs:
        print('\t\t{} {}'.format(objs[key], key))


def cleanup(client):
    print('\tDoing CLEANUP!')
    print('\tAll volumes, clones, snapshots, volume collection, initiator groups,')
    print('\tencryption keys and access control records will be removed from the system.')
    answer = input('\n\tAre you sure you want to proceded? [y/N] : ')
    if answer.lower() != 'y' and answer.lower() != 'yes':
        return
    print('\tDoing cleanup...\n')
    # Disassociate volumes from volcolls and delete volcolls
    volcolls = client.volume_collections.list()
    for vc_short in volcolls:
        vc_long = client.volume_collections.get(id=vc_short.id)
        if vc_long.attrs['volume_list'] is not None:
            # print(vc_long.attrs)
            for vol in vc_long.attrs['volume_list']:
                # print(vol['id'])
                client.volumes.dissociate(id=vol['id'])
                print('\tDisassociated vol {} from volume collection {}'.format(vol['name'], vc_long.attrs['name']))
        client.volume_collections.delete(id=vc_short.id)
        print('\tDeleted volume collection {}'.format(vc_long.attrs['name']))

    # Delete all volumes
    vols = client.volumes.list()
    # First delete all the clones
    for vol in vols:
        lvol = client.volumes.get(id=vol.attrs['id'])
        if lvol.attrs['clone'] is not False:
            cleanup_vol(client, lvol.attrs['name'], noisy=True)
    # Then delete all the snapshots for each volume
    vols = client.volumes.list()
    for vol in vols:
        # Delete all Snapshots
        snap_list = client.snapshots.list(vol_name=vol.attrs['name'])
        for snap in snap_list:
            cleanup_snapshot(client, snap.id, noisy=True)
        # Then delete the volumes
        cleanup_vol(client, vol.attrs['name'], noisy=True)

    # Delete all initiator groups
    ig_list = client.initiator_groups.list()
    for ig in ig_list:
        cleanup_initiator_group(client, ig.attrs['name'], noisy=True)
    # Delete all ACRs
    acr_list = client.access_control_records.list()
    for acr in acr_list:
        access_control_record_delete(client, acr.attrs['id'], False, '\t')
    # Delete all Master Keys
    key_list = client.master_key.list()
    for key in key_list:
        cleanup_master_key(client, key.attrs['name'], noisy=True)


if __name__ == '__main__':
    config = read_config()
    try:
        client = NimOSClient(config[KEY_HNAME], config[KEY_UNAME], config[KEY_PWD])
    except NimOSAuthenticationError:
        print('ERROR: Invalid credentials.')
        sys.exit(1)
    choice = -1
    while choice != 0:
        print('\n\n\n_____________________')
        print('                     NIMBLE SDK HELPER MENU:')

        print('00) EXIT')
        print('01) Cleanup')
        print('02) Show all objects')
        print('03) Client: Show attributes')

        print('10) ACR: Show client attributes')
        print('11) ACR: Show instance attributes')
        print('12) ACR: Create')
        print('13) ACR: Delete')
        print('14) ACR: Get All')

        # print('\t20) Clone: Do Delete')
        print('20) Groups: Show client attributes')
        print('21) Groups: Show instance attributes')
        print('22) Groups: Get All')

        print('30) Initiator Groups: Show client attributes')
        print('31) Initiator Groups: Show instance attributes')
        print('32) Initiator Groups: Create')
        print('33) Initiator Groups: Delete')
        print('34) Initiator Groups: Get All')

        print('40) Master Key: Show client attributes')
        print('41) Master Key: Show instance attributes')
        print('42) Master Key: Show All')
        print('43) Master Key: Create')
        print('44) Master Key: Delete')

        print('50) Snapshots: Show client attributes')
        print('51) Snapshots: Show instance attributes')
        print('52) Snapshots: Get All')
        print('53) Snapshots: Create')
        print('54) Snapshots: Delete')

        print('70) Volume: Show client attributes')
        print('71) Volume: Show instance attributes')
        print('72) Volume: Create')
        print('73) Volume: Delete')
        print('74) Volume: Get All')
        print('75) Volume: Get Attributes')
        choice = int(input('_____________________CHOICE: '))
        print('')
        if choice == 1:
            cleanup(client)
        elif choice == 2:
            show_all_objects(client)
        elif choice == 3:
            analyze(client, 'Client:')
        elif choice == 10:  # ACR: Show client attributes
            analyze(client.access_control_records, 'client.access_control_records:')
        elif choice == 11:  # ACR: Show instance attributes
            acr_id = access_control_record_create(client, 'wfacr', '\t')
            if acr_id is not None:
                acr = client.access_control_records.get(acr_id)
                print('')
                analyze(acr, 'access_control_record:')
                print('')
                print_attrs(acr, prefix='\t')
                print('')
                access_control_record_delete(client, acr_id, False, '\t')
        elif choice == 12:  # ACR: Do Create
            acr_id = access_control_record_create(client, 'wfacr', '\t')
        elif choice == 13:  # ACR: Do Create
            acr_id = input('\tDelete ACR Id: ')
            access_control_record_delete(client, acr_id, True, '\t')
        elif choice == 14:  # ACR: Do Get All
            print('\tAll Access Control Records:')
            res = client.access_control_records.list()
            for i in range(len(res)):
                print('\t\t{}) {}'.format(i+1, res[i].attrs['id']))

        elif choice == 20:  # Groups: Show client attributes
            analyze(client.groups, 'client.groups:')
        elif choice == 21:  # Groups: Show instance attributes
            grp_list = client.groups.list()
            if len(grp_list) > 0:
                grp = client.groups.get(grp_list[0].attrs['id'])
                analyze(grp, 'groups instance:')
                print('')
                print_attrs(grp, '\t\t')
        elif choice == 22:  # Groups: Do Get All
            grp_list = client.groups.list()
            print('\tAll Groups:')
            for i in range(len(grp_list)):
                print('\t\t{}) {} - {}'.format(i+1, grp_list[i].attrs['name'], grp_list[i].attrs['id']))

        elif choice == 30:  # initiator Groups: Show client attributes
            analyze(client.initiator_groups, 'client.initiator_groups:')
        elif choice == 31:  # initiator Groups: Show instance attributes
            ig = create_initiator_group(client, 'igz', noisy=True)
            print('')
            analyze(ig, 'initiator_group instance')
            print('')
            print_attrs(ig, prefix='\t\t')
            print('')
            cleanup_initiator_group(client, 'igz', noisy=True)
        elif choice == 32:  # initiator Groups: Do Create
            ig_name = input('\tCreate Initiator Group Name: ')
            ig = create_initiator_group(client, ig_name, noisy=True)
        elif choice == 33:  # initiator Groups: Do Delete'
            ig_name = input('\tDelete Initiator Group Name: ')
            cleanup_initiator_group(client, ig_name, noisy=True)
        elif choice == 34:
            print('\tAll Initiator Groups:')
            ig_list = client.initiator_groups.list()
            for i in range(len(ig_list)):
                print('\t\t{}) {} - {}'.format(i+1, ig_list[i].attrs['name'], ig_list[i].attrs['id']))

        elif choice == 40:  # Master Key: Show client attributes
            analyze(client.master_key, 'client.initiator_groups:')
        elif choice == 41:  # Master Key: Show instance attributes
            mk_name = 'default'
            mk = create_master_key(client, mk_name, 'onetwothreefourfive', noisy=True)
            print('')
            analyze(mk, 'master_key instance')
            print('')
            print_attrs(mk, prefix='\t\t')
            print('')
            cleanup_master_key(client, mk_name, noisy=True)
        elif choice == 42:  # Master Key: Show All
            print('\tMaster Keys:')
            key_list = client.master_key.list()
            for i in range(len(key_list)):
                print('\t\t{}) {} - {}'.format(i+1, key_list[i].attrs['name'], key_list[i].attrs['id']))
        elif choice == 43:  # Master Key: Do Create
            mk_name = input('\tCreate Master Key Name: ')
            mk_phrase = 'onetwothreefour'
            try:
                mk = create_master_key(client, mk_name, mk_phrase, noisy=True)
            except NimOSAPIError:
                print('\tMaster Key creation failed. Try a Master Key named "default".')
        elif choice == 44:  # Master Key: Do Delete
            mk_name = input('\tDelete Master Key Name: ')
            cleanup_master_key(client, mk_name, noisy=True)
        elif choice == 50:  # Snapshots: Show client attributes
            analyze(client.snapshots, 'client.snapshots:')
        elif choice == 51:  # Snapshots: Show instance attributes
            vol_name = 'wfhelpervol'
            vol = create_vol(client, vol_name, noisy=True)
            snap = create_snap(client, vol_name + 'snap', vol.attrs['id'], noisy=True)
            print('')
            analyze(snap, 'client.snapshots:')
            print('')
            print_attrs(snap, prefix='\t\t')
            print('')
            cleanup_snapshot(client, snap.attrs['id'], noisy=True)
            cleanup_vol(client, vol_name, noisy=True)
        elif choice == 52:
            vol_name = input('\tGet Snapshots for Vol: ')
            snap_list = client.snapshots.list(vol_name=vol_name)
            for i in range(len(snap_list)):
                print('\t\t{}) {} - {}'.format(i+1, snap_list[i].attrs['name'], snap_list[i].attrs['id']))
        elif choice == 53:
            snap_name = input('\tCreate Snapshot Name: ')
            vol_name = 'wfhelpervol'
            vol = create_vol(client, vol_name, noisy=True)
            snap = create_snap(client, snap_name, vol.attrs['id'], noisy=True)
        elif choice == 54:
            snap_id = input('\tDelete Snapshot Id: ')
            try:
                snap = client.snapshots.get(id=snap_id)
                if snap is not None:
                    cleanup_snapshot(client, snap.attrs['id'], noisy=True)
                    answer = input('\tDelete Associated Snapshot Volume "{}": '.format(snap.attrs['vol_name']))
                    if answer.lower() == 'y' or answer.lower() == 'yes':
                        cleanup_vol(client, snap.attrs['vol_name'], noisy=True)
            except NimOSAPIError:
                print('\tERROR: Failed to delete snapshot.')
            # snap_id = snapshot_delete(client, vol_name)
            # print('Success = %s' % ('True' if snap_id is not None else 'False'))

        elif choice == 70:  # Volume: Show client attributes
            analyze(client.volumes, 'client.volumes:')
        elif choice == 71:  # Volume: Show instance attributes
            vol_name = 'wftempvol'
            vol = create_vol(client, vol_name, noisy=True)
            print('')
            analyze(vol, 'volumes instance attributes:')
            print('')
            print_attrs(vol, '\t\t')
            print('')
            cleanup_vol(client, vol_name, noisy=True)
        elif choice == 72:  # Volume: Do Create
            vol_name = input('\tCreate Volume Name: ')
            # vol_id = volume_create(client, vol_name)
            vol = create_vol(client, vol_name, noisy=True)
        elif choice == 73:
            vol_name = input('\tDelete Volume Name: ')
            cleanup_vol(client, vol_name, noisy=True)
        elif choice == 74:  # Volume: Do Get All
            print('\tAll Volumes:')
            vol_list = client.volumes.list()
            for i in range(len(vol_list)):
                print('\t\t{}) {} - {}'.format(i+1, vol_list[i].attrs['name'], vol_list[i].attrs['id']))
        elif choice == 75:
            vol_name = input('\tVolume Name: ')
            vol = client.volumes.get(name=vol_name)
            if vol is not None:
                print_attrs(vol, prefix='\t')
                print('')
            else:
                print('\tVolume "{}" does not exist'.format(vol_name))
