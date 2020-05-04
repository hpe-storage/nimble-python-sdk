# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions
import tests.test_volume as volume
import tests.test_volume_collection as volcoll

# global variables
volcoll_name1 = nimosclientbase.get_unique_string("snapcolltc-volcoll1")
snapcoll_name1 = nimosclientbase.get_unique_string("snapcolltc-snapcoll1")
vol_name1 = nimosclientbase.get_unique_string("snapcolltc-vol1")
snapcoll_to_delete = []

'''SnapCollTestCase class tests the snapshot collection object functionality'''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Snapcoll TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Snapcoll TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    global vol_name1, snapcoll_name1, volcoll_name1

    volcoll_name1 = nimosclientbase.get_unique_string("snapcolltc-volcoll1")
    snapcoll_name1 = nimosclientbase.get_unique_string("snapcolltc-snapcoll1")
    vol_name1 = nimosclientbase.get_unique_string("snapcolltc-vol1")
    # 1st create a volcoll and 2nd associate a volume to volcoll
    volcoll_resp = volcoll.create_volcoll(volcoll_name1)
    assert volcoll_resp is not None
    # save the volcoll_id here
    volcoll_resp.attrs.get("id")
    # create and associate a volume
    volresp = volume.create_volume(vol_name1)
    try:
        nimosclientbase.get_nimos_client().volumes.update(
            id=volresp.attrs.get("id"),
            volcoll_id=volcoll_resp.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_snapcoll()
    volume.delete_volume()
    volcoll.delete_volcoll()
    nimosclientbase.log_footer(request.function.__name__)


def delete_snapcoll():
    for snapcoll_id in snapcoll_to_delete:
        try:
            resp = nimosclientbase.get_nimos_client(
            ).snapshot_collections.delete(id=snapcoll_id)
            assert resp is not None
            log(f"Deleted snapcoll with id '{snapcoll_id}'")
        except exceptions.NimOSAPIError as ex:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
    snapcoll_to_delete.clear()


def create_snapcoll(snapcoll_name, **kwargs):
    resp = nimosclientbase.get_nimos_client().snapshot_collections.create(
        name=snapcoll_name, **kwargs)
    snapcoll_id = resp.attrs.get("id")
    snapcoll_to_delete.append(snapcoll_id)
    assert resp is not None
    log(f"Created snapcoll with name '{snapcoll_name}' and Id '{snapcoll_id}'")
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_snapcoll(setup_teardown_for_each_test):
    snapcoll_resp = create_snapcoll(
        snapcoll_name1,
        volcoll_id=volcoll.volcoll_to_delete[0],
        description="created by testcase",
        replicate=False,
        start_online=False)
    assert snapcoll_resp is not None
    assert snapcoll_name1 == snapcoll_resp.attrs.get("name")
    assert "created by testcase" == snapcoll_resp.attrs.get("description")
    assert snapcoll_resp.attrs.get("replicate") is False
    # make the snapcoll offline
    resp = nimosclientbase.get_nimos_client().snapshot_collections.update(
        snapcoll_resp.attrs.get("id"), description="modified by testcase")
    assert resp is not None
    assert "modified by testcase" == resp.attrs.get("description")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_snapcoll_with_onlinesnapshot(setup_teardown_for_each_test):

    snapcoll_resp = create_snapcoll(
        snapcoll_name1,
        volcoll_id=volcoll.volcoll_to_delete[0],
        description="created by testcase",
        replicate=False,
        start_online=True)
    assert snapcoll_resp is not None
    assert snapcoll_name1 == snapcoll_resp.attrs.get("name")
    assert "created by testcase" == snapcoll_resp.attrs.get("description")
    assert snapcoll_resp.attrs.get("replicate") is False
    # get the snapcoll
    snapcoll_resp = nimosclientbase.get_nimos_client(
    ).snapshot_collections.get(id=snapcoll_resp.attrs.get("id"))
    assert snapcoll_resp
    # check whether snapcoll has snapshots created
    # assert snapcoll_resp.attrs.get("start_online"),true) may be array bug
    # as doc says this field should be there
    assert len(snapcoll_resp.attrs.get("snapshots_list")) == 1
    # offline the snapshot
    snapshotlist = snapcoll_resp.attrs.get("snapshots_list")
    for snapid in snapshotlist:
        nimosclientbase.get_nimos_client().snapshots.update(
            id=snapid["id"], online=False)


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_delete_snapcoll_with_onlinesnapshot(setup_teardown_for_each_test):
    # should throw ex "SM_vol_has_online_snap"
    snapcoll_resp = create_snapcoll(
        snapcoll_name1,
        volcoll_id=volcoll.volcoll_to_delete[0],
        description="created by testcase",
        replicate=False,
        start_online=True)  # online snapshot
    assert snapcoll_resp is not None
    assert snapcoll_name1 == snapcoll_resp.attrs.get("name")
    assert "created by testcase" == snapcoll_resp.attrs.get("description")
    assert snapcoll_resp.attrs.get("replicate") is False
    # get the snapcoll
    snapcoll_resp = nimosclientbase.get_nimos_client(
    ).snapshot_collections.get(id=snapcoll_resp.attrs.get("id"))
    assert snapcoll_resp
    # try deleting it should throw exception
    try:
        delete_snapcoll()
        volume.delete_volume()
    except exceptions.NimOSAPIError as ex:
        if "SM_vol_has_online_snap" in str(ex):
            log("Failed as expected with exception : 'SM_vol_has_online_snap'")
            # offilne the snapshot
            snapshotlist = snapcoll_resp.attrs.get("snapshots_list")
            for snapid in snapshotlist:
                snapresp = nimosclientbase.get_nimos_client(
                ).snapshots.update(id=snapid["id"], online=False)
                assert snapresp is not None
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_sync_replication_partner_for_snapcoll(setup_teardown_for_each_test):
    # this tescase only works for sync repl
    try:
        snapcoll_resp = create_snapcoll(
            snapcoll_name1,
            volcoll_id=volcoll.volcoll_to_delete[0],
            description="Created by testcase",
            replicate=True,
            start_online=False)
        assert snapcoll_resp is not None
        assert snapcoll_name1 == snapcoll_resp.attrs.get("name")
        assert "created by testcase" == snapcoll_resp.attrs.get("description")
        assert snapcoll_resp.attrs.get("start_online") is True
        assert snapcoll_resp.attrs.get("replicate") is True
    except exceptions.NimOSAPIError as ex:
        if "SM_repl_no_partner_avail" in str(ex):
            log("Failed as expected. no replication partner available")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
