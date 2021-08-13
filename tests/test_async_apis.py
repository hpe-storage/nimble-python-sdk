# import pytest
# import tests.nimbleclientbase as nimosclientbase
# from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import NimOSClient
import os, sys, time
import spur

IP = os.getenv("SDK_TARGET_HOST")
USER = os.getenv("SDK_TARGET_USER")
PASSWORD = os.getenv("SDK_TARGET_PASSWORD")

'''
Setup
'''

if IP == None or USER == None or PASSWORD == None:
    print("ERROR: Missing one of these environment variables: SDK_TARGET_HOST, SDK_TARGET_USER, SDK_TARGET_PASSWORD, SDK_TARGET_TENANT_USER, SDK_TARGET_TENANT_PASSWORD, SDK_TARGET_TENANT_FOLDER")
    print("Usage:")
    print("SDK_TARGET_HOST - Management hostname or IP of array")
    print("SDK_TARGET_USER - User (non-tenant) username")
    print("SDK_TARGET_PASSWORD - User (non-tenant) password")
    sys.exit(1)

api = NimOSClient(IP, USER, PASSWORD)

shell = spur.SshShell(hostname="c8-array7.lab.nimblestorage.com", username="root", password="admin")

volume = api.volumes.get(name="test-volume")
if volume == None:
    volume = api.volumes.create(name="test-volume", size=1024)
volume_id = volume.attrs['id']

ig = api.initiator_groups.get(name="test-ig")
if ig == None:
    ig = api.initiator_groups.create(name="test-ig", access_protocol="iscsi")
ig_id = ig.attrs['id']
snap = api.snapshots.get(vol_id=volume_id)
if snap == None:
    snap = api.snapshots.create(name="test-snapshot", vol_id=volume_id)

'''
The test
'''

'''
('edit_vol'), ('snap_vol', 'edit_snap'), ('add_vol_acl', 'remove_vol_acl'),
('create_initiator_grp', 'delete_initiator_grp', 'edit_initiator_grp')
'add_fc_vol_acl', ('add_initiator', 'remove_initiator')
'''

# This test is not working at the moment.
# API calls are expected to run into exception
# but in reality, they succeed immediately
def testSnapshotCreationException():
    snapshot = None
    try:
        shell.run(["nsproc", "--stop", "dsd"])
        # Create snap
        try:
            snapshot = api.snapshots.create(name="test-snapshot", vol_id=volume_id)
            print("Fail: snapshot creation should not succeed immediately")
        except Exception as e:
            failed_snap_vol = e.args[0]['id']
            shell.run(["nsproc", "--start", "dsd"])
            time.sleep(5)
            snapshot = api.snapshots.get(name="test-snapshot")
            if snapshot != None:
                print("Success -- confirmed snap_vol is async")
                print("job id:", failed_snap_vol)
    except Exception as e:
        print("testInitiatorGroupInProgressException: err: ", e)
        shell.run(["nsproc", "--start", "dsd"])

# This test is not working at the moment.
# API calls are expected to run into exception
# but in reality, they succeed immediately
def testSnapshotUpdateException():
    try:
        shell.run(["nsproc", "--stop", "dsd"])
        # Update snap
        try:
            api.snapshots.update(id=snap.attrs['id'], description="test-update-snap-description")
            print("Fail: snap update should not succeed immediately")
        except Exception as e:
            failed_edit_snap = e.args[0]['id']
            print("Success -- confirmed edit_snap is async")
            print("job id:", failed_edit_snap)
            shell.run(["nsproc", "--start", "dsd"])

    except Exception as e:
        print("testInitiatorGroupInProgressException: err: ", e)
        shell.run(["nsproc", "--start", "dsd"])


# These test is not working at the moment.
# API calls are expected to run into exception
# but in reality, they succeed immediately
def testInitiatorGroupInProgressException():
    igroup = None
    try:
        shell.run(["nsproc", "--stop", "dsd"])
        # Create initiator group
        try:
            igroup = api.initiator_groups.create(name="test-create-igroup", access_protocol="iscsi")
            print("Fail: initator group assignment should not succeed immediately")
        except Exception as e:
            failed_create_initiator_grp = e.args[0]['id']
            shell.run(["nsproc", "--start", "dsd"])
            time.sleep(5)
            igroup = api.initiator_groups.get(name="test-create-igroup")
            if igroup != None:
                print("Success -- confirmed create_initiator_grp is async")
                print("job id:", failed_create_initiator_grp)

        shell.run(["nsproc", "--stop", "dsd"])
        # Update initator group
        try:
            api.initiator_groups.update(id=igroup.attrs['id'], description="test-update-igroup-description")
            print("Fail: initiator group update should not succeed immediately")
        except Exception as e:
            failed_edit_initiator_grp = e.args[0]['id']
            print("Success -- confirmed edit_initiator_grp is async")
            print("job id:", failed_edit_initiator_grp)
            shell.run(["nsproc", "--start", "dsd"])

        shell.run(["nsproc", "--stop", "dsd"])
        # Delete initiator group
        try:
            api.initiator_groups.delete(id=igroup.attrs['id'])
            print("Fail: initiator group deletion should not succeed immediately")
        except Exception as e:
            failed_delete_initiator_group = e.args[0]['id']
            shell.run(["nsproc", "--start", "dsd"])
            time.sleep(5)
            igroup = api.initiator_groups.get(id=igroup.attrs['id'])
            if igroup == None:
                print("Success -- confirmed acl_vol is async")
                print("job id:", failed_delete_initiator_group)

    except Exception as e:
        print("testInitiatorGroupInProgressException: err: ", e)
        shell.run(["nsproc", "--start", "dsd"])


def testAclInProgressException():
    acl = None
    try:
        shell.run(["nsproc", "--stop", "dsd"])
        try:
            acl = api.access_control_records.create(vol_id=volume_id, initiator_group_id=ig_id)
            print("Fail: ACL assignment should not succeed immediately")
        except Exception as e:
            failed_add_vol_acl = e.args[0]['id']
            shell.run(["nsproc", "--start", "dsd"])
            time.sleep(5)
            acl = api.access_control_records.get(vol_id=volume_id, initiator_group_id=ig_id)
            if acl != None:
                print("Success -- confirmed acl_vol is async")
                print("job id:", failed_add_vol_acl)

        shell.run(["nsproc", "--stop", "dsd"])
        try:
            api.access_control_records.delete(id=acl.attrs['id'])
        except Exception as e:
            failed_remove_vol_acl = e.args[0]['id']
            shell.run(["nsproc", "--start", "dsd"])
            time.sleep(5)
            acl = api.access_control_records.get(vol_id=volume_id, initiator_group_id=ig_id)
            if acl == None:
                print("Success -- confirmed acl_vol is async")
                print("job id:", failed_remove_vol_acl)

    except Exception as e:
        print("testAclInProgressException: err: ", e)
        shell.run(["nsproc", "--start", "dsd"])


# This test is not working at the moment.
# API calls are expected to run into exception
# but in reality, they succeed immediately
def testInitiatorInProgressException():
    shell.run(["nsproc", "--stop", "dsd"])

    try:
        init = api.initiators.create(label="test-label", iqn="iqn.1992-01.com.example:storage.tape1.sys1.xyz", ip_address=IP, initiator_group_id=ig_id, access_protocol="iscsi")
        print("Initiator creation should not succeed immediately")
    except Exception as e:
        shell.run(["nsproc", "--start", "dsd"])

        failed_add_initiator = e.args[0]['id']
        init = api.initiators.get(label="test-label")
        time.sleep(5)
        if e.args[0]['state'] == "done":
            print("Success -- confirmed add_initator is async")
            print("job id:", failed_add_initiator)

    shell.run(["nsproc", "--stop", "dsd"])
    try:
        api.initiators.delete(id="0b1687ff771a5ea81900000000000000000000000d")
        print("Initiator creation should not succeed immediately")
    except Exception as e:
        shell.run(["nsproc", "--start", "dsd"])

        failed_remove_initiator = e.args[0]['id']
        time.sleep(5)
        if e.args[0]['state'] == "done":
            print("Success -- confirmed remove_initator is async")
            print("job id:", failed_remove_initiator)
    shell.run(["nsproc", "--start", "dsd"])


def testVolumeInProgressException():
    shell.run(["nsproc", "--stop", "dsd"])
    try:
        api.volumes.update(id=volume_id, size=2048)
        print("testVolumeInProgressException: Fail. Resize should not succeed immediately")
    except Exception as e:
        failed_edit_vol = e.args[0]['id']
        print("Success -- confirmed edit_vol is async.")
        print("Job id:", failed_edit_vol)
        shell.run(["nsproc", "--start", "dsd"])


# testVolumeInProgressException()
# testAclInProgressException()

'''
Break down
'''
volume.offline()
volume.delete()


