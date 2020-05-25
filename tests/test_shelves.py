# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions


'''ShelveTestCase class tests the subnet object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Shelves TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Shelves TestCase *****\n")
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
def test_get_shelve(setup_teardown_for_each_test):
    # sdk bug. why is subnet object having functions like create,
    # update delete??? the rest doc does not have these. only read is allowed
    resp = nimosclientbase.get_nimos_client().shelves.list(detail=True)
    assert resp is not None
    # doc shows it has 13 properties.just check the length
    assert resp[0].attrs.__len__() == 13


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_activateshelve(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().shelves.get()
    assert resp is not None
    try:
        resp = nimosclientbase.get_nimos_client().shelves.update(
                id=resp.attrs.get("id"), force=True, activated=True)
        assert resp.attrs.get("activated") is True
    except exceptions.NimOSAPIError as ex:
        if "SM_shelf_no_eloc_id" in str(ex):
            log("making test as passed since no shelve exist for expansion")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
    assert resp is not None
