# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

'''PoolTestCase tests the Pool object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Pool TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Pool TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    nimosclientbase.log_footer(request.function.__name__)


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_pools(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().pools.list(
        detail=True, pageSize=2)
    assert resp is not None
    # doc shows it has 13 properties.but in replication setup it is 43.
    # just check the length
    assert resp[0].attrs.__len__() >= 43


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_pools(setup_teardown_for_each_test):
    array_list = [
        {
            "id": "0900000000000004d3000000000000000000000003",
            "array_id": "0900000000000004d3000000000000000000000003"
        }
    ]
    try:
        resp = nimosclientbase.get_nimos_client().pools.create(
            name="pooltest", array_list=array_list)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_array_not_found" in str(ex):
            log("Failed as expected. Array id given is invalid")
        elif "SM_srep_group_unsup" in str(ex):
            log("Failed as expected. Synchronous replication setup "
                "requires a group with exactly two single-array pools")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_pools(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().pools.get()
    assert resp is not None
    desc_name = resp.attrs.get("description")
    name = resp.attrs.get("name")
    # update name
    update_resp = nimosclientbase.get_nimos_client().pools.update(
        resp.attrs.get("id"),
        description="modified by testcase",
        name="testcasename")
    assert update_resp is not None
    # assert it got updated
    assert update_resp.attrs.get("description") == "modified by testcase"
    assert update_resp.attrs.get("name") == "testcasename"
    # rename it back
    update_resp = nimosclientbase.get_nimos_client().pools.update(
        resp.attrs.get("id"),
        description=desc_name,
        name=name)
    assert update_resp is not None
