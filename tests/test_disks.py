# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions


'''DisksTestCase tests the disks object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Disks TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Disks TestCase *****\n")
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
def test_get_disks(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().disks.get()
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_disks_mandatory_params(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().disks.get()
    assert resp is not None
    # update
    try:
        nimosclientbase.get_nimos_client().disks.update(
            id=resp.attrs.get("id"),
            force=False)
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. mandatory param 'disk_op' not provided")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_disks_query_params(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().disks.list()
    assert resp is not None
    resp = nimosclientbase.get_nimos_client().disks.get(
        array_id=resp[0].attrs.get("array_id"))
    assert resp is not None
    # assert that those fields are present
    assert resp.attrs.get("array_id") is not None
    # try asserting a value which was not querying
    assert resp.attrs.get("startRow") is None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_query_invalid_params(setup_teardown_for_each_test):
    try:
        query_param = "activity"
        resp = nimosclientbase.get_nimos_client().disks.get(
            limit=2,
            fields=query_param)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_unexpected_query_param" in str(ex):
            log("Failed as expected. "
                f"Invalid query params provided to query: '{query_param }'")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
