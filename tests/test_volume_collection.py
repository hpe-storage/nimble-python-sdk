# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient.v1 import exceptions
import tests.test_volume as volume
import threading

# global variables
volcoll_name1 = nimosclientbase.get_unique_string("volcolltc-volcoll1")
volcoll_to_delete = []
volcoll_lock = threading.Lock()

'''VolumeCollectionTestCase tests the volumecollection object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for VolumeCollectionTestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for VolumeCollectionTestCase "
            "Testcase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    global volcoll_name1
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    volume.delete_volume()
    delete_volcoll()
    volcoll_name1 = nimosclientbase.get_unique_string("volcolltc-volcoll1")
    nimosclientbase.log_footer(request.function.__name__)


def delete_volcoll():
    volcoll_lock.acquire()
    for volcoll_id in volcoll_to_delete:
        try:
            resp = nimosclientbase.get_nimos_client(
            ).volume_collections.delete(id=volcoll_id)
            assert resp is not None
            log(f" Deleted volcoll with id '{volcoll_id}'")
        except exceptions.NimOSAPIError as ex:
            volcoll_lock.release()
            raise ex
    volcoll_to_delete.clear()
    volcoll_lock.release()


def create_volcoll(volcollname):
    try:
        volcoll_lock.acquire()
        resp = nimosclientbase.get_nimos_client().volume_collections.create(
            name=volcollname, description="created by testcase")
        volcoll_id = resp.attrs.get("id")
        volcoll_to_delete.append(volcoll_id)
        assert resp is not None
        log(f"Created volcoll with name '{volcollname}' and Id '{volcoll_id}'")
        volcoll_lock.release()
        return resp
    except Exception as ex:
        volcoll_lock.release()
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_volcoll(setup_teardown_for_each_test):
    resp = create_volcoll(volcoll_name1)
    assert resp is not None
    assert volcoll_name1 == resp.attrs.get("name")
    assert "created by testcase" == resp.attrs.get("description")

    # change the description and test it works
    resp = nimosclientbase.get_nimos_client().volume_collections.update(
        resp.attrs.get("id"), description="modified by testcase")
    assert resp is not None
    assert "modified by testcase" == resp.attrs.get("description")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_add_volume_to_volcoll(setup_teardown_for_each_test):
    volcoll_resp = create_volcoll(volcoll_name1)
    voloume_name = nimosclientbase.get_unique_string(
        "VolumeCollectionTestCase-addtovolcoll")

    vol_resp = nimosclientbase.get_nimos_client().volumes.create(
        voloume_name, size=50)
    volume.vol_to_delete.append(vol_resp.attrs.get("id"))
    assert volcoll_resp is not None

    # associate the volume to volcoll
    vol_associate_resp = nimosclientbase.get_nimos_client().volumes.associate(
        id=vol_resp.attrs.get("id"), volcoll=volcoll_resp)
    assert vol_resp is not None
    # check
    assert vol_associate_resp.get("volcoll_name") == volcoll_name1
    assert vol_associate_resp.get("volcoll_id") == volcoll_resp.attrs.get("id")
    # disassociate
    nimosclientbase.get_nimos_client().volumes.dissociate(
        id=vol_resp.attrs.get("id"))
    # get vol coll and confirm has no volumes
    volcoll_resp = nimosclientbase.get_nimos_client(
    ).volume_collections.get(id=volcoll_resp.attrs.get("id"))
    assert volcoll_resp.attrs.get("volume_count") == 0


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_delete_volcoll_before_disassociating_volume(
        setup_teardown_for_each_test):
    volcoll_resp = create_volcoll(volcoll_name1)
    voloume_name = nimosclientbase.get_unique_string(
        "VolumeCollectionTestCase-addtovolcoll")

    vol_resp = nimosclientbase.get_nimos_client().volumes.create(
        voloume_name, size=50)
    volume.vol_to_delete.append(vol_resp.attrs.get("id"))
    assert volcoll_resp is not None

    # associate the volume to volcoll
    vol_associate_resp = nimosclientbase.get_nimos_client().volumes.associate(
        id=vol_resp.attrs.get("id"), volcoll=volcoll_resp)
    assert vol_resp is not None
    # check
    assert vol_associate_resp.get("volcoll_name") == volcoll_name1
    assert vol_associate_resp.get("volcoll_id") == volcoll_resp.attrs.get("id")
    # try deleting the volcoll . this should fail as volume has
    # not been disassocited
    try:
        nimosclientbase.get_nimos_client().volume_collections.delete(
            id=volcoll_resp.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        if"SM_ebusy" in str(ex):
            log("Failed as expected. disaasociate volume first")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_promote_volcoll(setup_teardown_for_each_test):
    volcoll_resp = create_volcoll(volcoll_name1)
    voloume_name = nimosclientbase.get_unique_string(
        "VolumeCollectionTestCase-addtovolcoll")

    vol_resp = nimosclientbase.get_nimos_client().volumes.create(
        voloume_name, size=50)
    volume.vol_to_delete.append(vol_resp.attrs.get("id"))
    assert volcoll_resp is not None

    # associate the volume to volcoll
    vol_associate_resp = nimosclientbase.get_nimos_client().volumes.associate(
        id=vol_resp.attrs.get("id"), volcoll=volcoll_resp)
    assert vol_resp is not None
    # check
    assert vol_associate_resp.get("volcoll_name") == volcoll_name1
    assert vol_associate_resp.get("volcoll_id") == volcoll_resp.attrs.get("id")
    # try deleting the volcoll .this should fail as
    # volume has not been disassocited
    try:
        nimosclientbase.get_nimos_client().volume_collections.promote(
            id=volcoll_resp.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        if"SM_ealready" in str(ex):
            log("Failed as expected. volcoll is already promoted")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_demote_volcoll(setup_teardown_for_each_test):
    volcoll_resp = create_volcoll(volcoll_name1)
    assert volcoll_resp is not None
    try:
        nimosclientbase.get_nimos_client().volume_collections.demote(
            id=volcoll_resp.attrs.get("id"),
            replication_partner_id="1264126491231239123hgghsjhd")
    except exceptions.NimOSAPIError as ex:
        if"SM_invalid_arg_value" in str(ex):
            log("Failed as expected. "
                "Invalid value provided for replication_partner_id")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_handover_volcoll(setup_teardown_for_each_test):
    volcoll_resp = create_volcoll(volcoll_name1)
    assert volcoll_resp is not None
    try:
        nimosclientbase.get_nimos_client().volume_collections.handover(
            id=volcoll_resp.attrs.get("id"),
            replication_partner_id="1264126491231239123hgghsjhd")
    except exceptions.NimOSAPIError as ex:
        if"SM_invalid_arg_value" in str(ex):
            log("Failed as expected. "
                "Invalid value provided for replication_partner_id")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_delete_volume_in_volcoll_before_disassociating(
        setup_teardown_for_each_test):

    volcoll_resp = create_volcoll(volcoll_name1)
    voloume_name = nimosclientbase.get_unique_string(
        "VolumeCollectionTestCase-addtovolcoll")

    vol_resp = nimosclientbase.get_nimos_client().volumes.create(
        voloume_name, size=50)
    volume.vol_to_delete.append(vol_resp.attrs.get("id"))
    assert volcoll_resp is not None

    # associate the volume to volcoll
    vol_associate_resp = nimosclientbase.get_nimos_client().volumes.associate(
        id=vol_resp.attrs.get("id"), volcoll=volcoll_resp)
    assert vol_resp is not None
    # check
    assert vol_associate_resp.get("volcoll_name") == volcoll_name1
    assert vol_associate_resp.get("volcoll_id") == volcoll_resp.attrs.get("id")
    # try deleting the volcoll . this should fail as
    # volume has not been disassocited
    try:
        nimosclientbase.get_nimos_client().volumes.offline(
            id=vol_resp.attrs.get("id"))
        nimosclientbase.get_nimos_client().volumes.delete(
            id=vol_resp.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        if"SM_vol_assoc_volcoll" in str(ex):
            log("Failed as expected with exception SM_vol_assoc_volcoll")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_edit_delete_protection_schedule(setup_teardown_for_each_test):
    # check if this array has any previous volcoll
    allvolcoll_resp = nimosclientbase.get_nimos_client(
    ).volume_collections.list()
    total_volcoll = allvolcoll_resp.__len__()

    protection_sched_name = "testcaseprotectionschedule"
    days = "monday,tuesday,wednesday,thursday,friday"
    description = "super cool schedule"

    volcoll_resp = create_volcoll(volcoll_name1)
    assert volcoll_resp is not None
    # create a protection schedule
    protect_sched_resp = nimosclientbase.get_nimos_client(
    ).protection_schedules.create(
        name=protection_sched_name,
        days=days, description=description,
        volcoll_or_prottmpl_id=volcoll_resp.attrs.get("id"),
        volcoll_or_prottmpl_type='volume_collection',
        num_retain=2)
    assert protect_sched_resp is not None
    assert protect_sched_resp.attrs.get("days") == days
    assert protect_sched_resp.attrs.get("description") == description
    assert protect_sched_resp.attrs.get("name") == protection_sched_name
    # check if volcoll is present
    allvolcoll_resp = nimosclientbase.get_nimos_client(
    ).volume_collections.list()
    assert allvolcoll_resp.__len__() == total_volcoll + 1

    # update the schedule
    resp = nimosclientbase.get_nimos_client().protection_schedules.update(
        id=protect_sched_resp.attrs.get("id"), period_unit="minutes")
    assert resp is not None
    assert "minutes" == resp.attrs.get("period_unit")
    # delete the schedule
    resp = nimosclientbase.get_nimos_client().protection_schedules.delete(
        id=protect_sched_resp.attrs.get("id"))
    # check if volcoll has schedule
    volcoll_resp = nimosclientbase.get_nimos_client().volume_collections.get(
        id=volcoll_resp.attrs.get("id"))
    assert volcoll_resp.attrs.get("schedule_list") is None
