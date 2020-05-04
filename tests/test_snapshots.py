# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions
import tests.test_volume as volume
import threading

# global variables
snapshot_name1 = nimosclientbase.get_unique_string("snapshottc-snapshot1")
vol_name1 = nimosclientbase.get_unique_string("snapshottc-vol1")
snapshot_to_delete = []
snapshot_lock = threading.Lock()

'''SnapshotsTestCase class tests the snapshots object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Snapshots TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Snapshot TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    global vol_name1
    nimosclientbase.log_header(request.function.__name__)
    vol_name1 = nimosclientbase.get_unique_string("snapshottc-vol1")
    vol_resp = volume.create_volume(vol_name1)
    assert vol_resp is not None
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_snapshot()
    volume.delete_volume()
    nimosclientbase.log_footer(request.function.__name__)


def delete_snapshot():
    snapshot_lock.acquire()
    for snapshot_id in snapshot_to_delete:
        try:
            resp = nimosclientbase.get_nimos_client().snapshots.delete(
                id=snapshot_id)
            assert resp is not None
            log(f"Deleted snapshot with id '{snapshot_id}'")
        except exceptions.NimOSAPIError as ex:
            snapshot_lock.release()
            log(f"Failed with exception message : {str(ex)}")
            raise ex
    snapshot_to_delete.clear()
    snapshot_lock.release()


def create_snapshot(snapshot_name, **kwargs):
    try:
        snapshot_lock.acquire()
        resp = nimosclientbase.get_nimos_client().snapshots.create(
            name=snapshot_name, **kwargs)
        snapshot_id = resp.attrs.get("id")
        snapshot_to_delete.append(snapshot_id)
        assert resp is not None
        log(f"Created snapshot with name '{snapshot_name}' and Id "
            f"'{snapshot_id}'")
        snapshot_lock.release()
        return resp
    except Exception as ex:
        snapshot_lock.release()
        log(f"Failed with exception message : {str(ex)}")
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_snapshot(setup_teardown_for_each_test):
    snapshot_resp = create_snapshot(snapshot_name1,
                                    vol_id=volume.vol_to_delete[0],
                                    description="created by testcase",
                                    online=False,
                                    writable=False)
    assert snapshot_resp is not None
    assert snapshot_name1 == snapshot_resp.attrs.get("name")
    assert "created by testcase" == snapshot_resp.attrs.get("description")
    assert snapshot_resp.attrs.get("online") is False
    assert snapshot_resp.attrs.get("writable") is False
    # test update
    resp = nimosclientbase.get_nimos_client().snapshots.update(
        snapshot_resp.attrs.get("id"), description="modified by testcase")
    assert resp is not None
    assert "modified by testcase" == resp.attrs.get("description")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_snapshot_with_invalid_name(setup_teardown_for_each_test):
    try:
        snap_name = "-;" + snapshot_name1
        create_snapshot(snap_name,
                        vol_id=volume.vol_to_delete[0],
                        description="created by testcase",
                        online=False,
                        writable=False)
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg" in str(ex):
            log(f"Failed as expected. Invalid snapshot name {snap_name}")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_delete_onlinesnapshot(setup_teardown_for_each_test):
    # should fail with exception
    snapshot_resp = create_snapshot(snapshot_name1,
                                    vol_id=volume.vol_to_delete[0],
                                    description="created by testcase",
                                    online=True,
                                    writable=False)
    assert snapshot_resp is not None
    assert snapshot_name1 == snapshot_resp.attrs.get("name")
    assert "created by testcase" == snapshot_resp.attrs.get("description")
    assert snapshot_resp.attrs.get("online") is True
    assert snapshot_resp.attrs.get("writable") is False
    delete_snapshot()


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_bulk_create_snapshot(setup_teardown_for_each_test):
    snap_vol_list = [
        {"vol_id": "0600000000000004d3000000000000000000000007",
         "snap_name": "",
         "snap_description": "",
         "cookie": "",
         "online": False,
         "writable": True},
        {"vol_id": "0600000000000004d3000000000000000000000008",
         "snap_name": "",
         "snap_description": "",
         "cookie": "",
         "online": False,
         "writable": True}
    ]

    try:
        snapshot_resp = nimosclientbase.get_nimos_client(
        ).snapshots.bulk_create(replicate=False,
                                snap_vol_list=snap_vol_list,
                                vss_snap=False)
        assert snapshot_resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_http_not_found" in str(ex):
            # this testcase will fail as wrong vol_id is passed.intention
            # is to make sure teh correct call goes through sdk
            log("Failed as expected. wrong vol id passed")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
