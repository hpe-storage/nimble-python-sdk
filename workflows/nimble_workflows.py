import sys
import getpass
import traceback
from nimbleclient.v1 import Client, NimOSAuthenticationError, NimOSAPIError


hostname = 'brian-va.vlab.nimblestorage.com'
username = 'admin'
password = 'admin'


def screen(msg, noisy, end='\n'):
    if noisy:
        print(msg, end=end)


def usage(noisy):
    screen('workflows.py [--login]', noisy)


def initiator_group_lifecycle(client, ig_name, noisy):
    try:
        screen('\nWorkflow: Initiator Group Lifecycle:', noisy)
        # Create an initiatior group
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Add initiators
        initiators = [
                {
                    "label": "itor1",
                    "ip_address": "1.1.1.1",
                    "iqn": "iqn.1992-01.com.example:storage.tape1.sys1.xyz"
                }
            ]
        # Note that we re-assign ig so as to capture the update
        ig = client.initiator_groups.update(id=ig.attrs['id'], description='add initiators',
                                            iscsi_initiators=initiators)
        screen('\tAdded initiator: {}'.format(ig.attrs['iscsi_initiators'][0]['label']), noisy)
        # Delete an initiatior group
        client.initiator_groups.delete(id=ig.id)
        screen('\tDeleted initiatior group: {}'.format(ig.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def volume_clone_lifecycle(client, vol_name, noisy):
    try:
        screen('\nWorkflow: Volume/Clone Lifecycle:', noisy)
        # Create a volume
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        # Create a snapshot
        snap_name = vol_name + 'snap'
        snap = client.snapshots.create(name=snap_name, vol_id=vol.attrs['id'])
        screen('\tCreated snapshot: {}'.format(snap.attrs['name']), noisy)
        # Create a clone from a snapshot
        clone_name = vol_name + 'clone'
        clone = client.volumes.create(name=clone_name, base_snap_id=snap.attrs['id'], clone=True)
        screen('\tCreated clone: {}'.format(clone.attrs['name']), noisy)
        # Delete a clone
        client.volumes.offline(clone.attrs['id'])
        client.volumes.delete(clone.attrs['id'])
        screen('\tDeleted clone: {}'.format(clone.attrs['name']), noisy)
        # Delete a snapshot
        client.snapshots.delete(id=snap.attrs['id'])
        screen('\tDeleted snapshot: {}'.format(snap.attrs['name']), noisy)
        # Delete a volume
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tDeleted volume: {}'.format(vol.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def acess_control_record_lifecycle(client, vol_name, ig_name, noisy):
    try:
        screen('\nWorkflow: Access Control Record Lifecycle:', noisy)
        # Create a volume
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        # Create an initiatior group
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Create the ACR
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig.attrs['id'],
                                                   vol_id=vol.attrs['id'])
        screen('\tCreated access control record: {}'.format(acr.attrs['id']), noisy)
        # Cleanup
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tDeleted access control record: {}'.format(acr.attrs['id']), noisy)
        client.initiator_groups.delete(id=ig.attrs['id'])
        screen('\tDeleted initiator group: {}'.format(ig.attrs['name']), noisy)
        client.volumes.offline(id=vol.attrs['id'])
        client.volumes.delete(id=vol.attrs['id'])
        screen('\tDeleted volume: {}'.format(vol.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def create_volume(client, vol_name, noisy):
    try:
        screen('\nWorkflow: Create Volume - {}'.format(vol_name), noisy)
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        return vol.id
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def publish_volume(client, vol_id, noisy):
    try:
        screen('\nWorkflow: Publish Volume - {}'.format(vol_id), noisy)
        vol = client.volumes.get(id=vol_id)
        vol_name = vol.attrs['name']
        # Create an initiatior group
        ig_name = vol_name + 'ig'
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Create the ACR
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig.attrs['id'],
                                                   vol_id=vol.attrs['id'])
        screen('\tCreated access control record: {}'.format(acr.attrs['id']), noisy)
        return acr.attrs['id']
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def detach_volume(client, acr_id, noisy):
    try:
        screen('\nWorkflow: Detach Volume for ACR - {}'.format(acr_id), noisy)
        acr = client.access_control_records.get(acr_id)
        if acr is None:
            screen('ERROR: ACR {} does not exist.'.format(acr_id), noisy)
            return False
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tDeleted ACR: {}'.format(acr.attrs['id']), noisy)
        client.initiator_groups.delete(id=acr.attrs['initiator_group_id'])
        screen('\tDeleted initiator group: {}'.format(acr.attrs['initiator_group_name']), noisy)
        client.volumes.offline(id=acr.attrs['vol_id'])
        client.volumes.delete(id=acr.attrs['vol_id'])
        screen('\tDeleted volume: {}'.format(acr.attrs['vol_name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def create_snapshot(client, vol_name, noisy):
    try:
        screen('\nWorkflow: Create Snapshot for Volume - {}'.format(vol_name), noisy)
        res = client.volumes.list()
        vol = None
        for item in res:
            if item.attrs['name'] == vol_name:
                vol = item
                break
        if vol is None:
            screen('ERROR: Volume {} does not exist.'.format(vol_name), noisy)
            return None
        # Create a snapshot
        snap = client.snapshots.create(name=vol_name + 'snap', vol_id=vol.attrs['id'])
        screen('\tCreated a snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.id), noisy)
        return snap.attrs['id']
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def delete_snapshot(client, snap_id, noisy):
    try:
        screen('\nWorkflow: Delete Snapshot - {}'.format(snap_id), noisy)
        snap = client.snapshots.get(id=snap_id)
        if snap is None:
            screen('ERROR: Snapshot does not exist: {}'.format(snap_id), noisy)
            return
        # Delete snapshot
        client.snapshots.delete(id=snap_id)
        screen('\tDeleted snapshot: {}, Id: {}'.format(snap.attrs['name'], snap.id), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def clone_volume(client, vol_name, noisy):
    try:
        screen('\nWorkflow: Clone Volume - {}'.format(vol_name), noisy)
        snap_id = create_snapshot(client, vol_name, noisy=False)
        clone_name = vol_name + 'clone'
        clone = client.volumes.create(name=clone_name, base_snap_id=snap_id, clone=True)
        screen('\tCloned volume: {}, Id: {}'.format(clone.attrs['name'], clone.id), noisy)
        clone_acr_id = publish_volume(client, clone.attrs['id'], noisy=False)
        screen('\tPublished cloned volume: {}'.format(clone_name), noisy)
        detach_volume(client, clone_acr_id, noisy=False)
        screen('\tDeleted cloned volume: {}'.format(clone_name), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def protect_volume(client, vol_id, noisy):
    try:
        screen('\nWorkflow: Protect Volume - {}'.format(vol_id), noisy)
        # Get the volume
        vol = client.volumes.get(vol_id)
        # Create a volume volume_collection
        volcoll_name = vol.attrs['name'] + 'coll'
        volcoll1 = client.volume_collections.create(name=volcoll_name, description="created by workflow")
        screen('\tCreated volume collection: {}, Id: {}'.format(volcoll1.attrs['name'], volcoll1.id), noisy)
        # Associate a volume with the volume collection
        asoc = client.volumes.associate(id=vol.attrs['id'], volcoll=volcoll1)
        screen('\tAssociated volume: {}, with volume vollection: {}'.format(
               asoc['access_control_records'][0]['vol_name'], asoc['volcoll_name']), noisy)
        # Create a protection schedule
        ps_name = "ps1"
        ps_days = "monday,tuesday,wednesday,thursday,friday"
        ps_info = "just a schedule"
        ps = client.protection_schedules.create(name=ps_name, period=60, period_unit="minutes",
                                                days=ps_days, description=ps_info,
                                                volcoll_or_prottmpl_id=volcoll1.id,
                                                volcoll_or_prottmpl_type='volume_collection',
                                                num_retain=2)
        screen('\tCreated protection schedule: {}, Id: {}'.format(ps.attrs['name'], ps.id), noisy)
        client.protection_schedules.delete(id=ps.attrs['id'])
        screen('\tDeleted protection schedule: {}'.format(ps.attrs['name']), noisy)
        # Disssociate a volume with the volume collection and delete to volume collection
        client.volumes.dissociate(id=vol.attrs['id'])
        screen('\tDisaocciated volume: {}, with volume vollection: {}'.
               format(vol.attrs['name'], volcoll1.attrs['name']), noisy)
        client.volume_collections.delete(id=volcoll1.id)
        screen('\tDeleted volume collection: {}'.format(volcoll1.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


def configure_encryption(client, noisy):
    try:
        screen('\nWorkflow: Configure Encryption', noisy)
        # Get the group
        grp_id = client.groups.list()[0].attrs['id']
        grp = client.groups.get(grp_id)
        screen('\tGot group: {}, Id: {}'.format(grp.attrs['name'], grp.id), noisy)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
        # Create a master key
        mk_name = 'default'
        mk_phrase = 'test-phrase11'
        mk = client.master_key.create(name=mk_name, passphrase=mk_phrase)
        screen('\tCreated a master key: {}, Id: {}'.format(mk.attrs['name'], mk.attrs['id']), noisy)
        # Create an encrypted volume
        vol_name = 'encryptedvol'
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000, encryption_cipher='aes_256_xts')
        screen('\tCreated an encrypted volume: {}, Id: {}'.format(vol.attrs['name'], vol.attrs['id']), noisy)
        # Get the group
        grp = client.groups.get(grp_id)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
        # Update encryption
        new_encryption = {"mode": "secure",   # Vals: none, available, secure
                          "scope": "volume",  # Vals: none, volume, pool, group
                          "cipher": "none"}   # Vals: none, aes_256_xts
        ue = client.groups.update(id=grp.id, encryption_config=new_encryption)
        screen('\tUpdated encryption: {}'.format(ue.attrs['encryption_config']), noisy)
        # Delete encrypted volume and master_key
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tDeleted volume: {}'.format(vol_name), noisy)
        client.master_key.delete(mk.attrs['id'])
        screen('\tDeleted master key: {}'.format(mk_name), noisy)
        grp = client.groups.get(grp_id)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    if len(sys.argv) == 2 and sys.argv[1] == '--login':
        hostname = input('Enter the hostname: ')
        username = input('Enter the username: ')
        password = getpass.getpass(prompt='Enter the password: ', stream=None)
    elif len(sys.argv) == 1:
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
        # Execute Workflows
        vol_name = 'wfvol'
        initiatior_group_name = 'wfig'
        initiator_group_lifecycle(client, initiatior_group_name, noisy)
        volume_clone_lifecycle(client, vol_name, noisy)
        acess_control_record_lifecycle(client, vol_name, initiatior_group_name, noisy)
        vol_id = create_volume(client, vol_name, noisy)
        acr_id = publish_volume(client, vol_id, noisy)
        snap_id = create_snapshot(client, vol_name, noisy)
        delete_snapshot(client, snap_id, noisy)
        clone_volume(client, vol_name, noisy)
        protect_volume(client, vol_id, noisy)
        configure_encryption(client, noisy)
        detach_volume(client, acr_id, noisy)
    else:
        usage()
