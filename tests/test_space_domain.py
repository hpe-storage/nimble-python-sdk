# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

# global variables
app_server_name_1 = nimosclientbase.get_unique_string("appservertc-1")
appserver_to_delete = []

'''SpaceDomainTestCase tests the SpaceDomain object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for SpaceDomain TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for SpaceDomain TestCase *****\n")
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
def test_get_spacedomains(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().space_domains.list(
        detail=True, pageSize=200)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_spacedomains_endrow_beyond(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().space_domains.get(endRow=30)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected. no rows present")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_selectfields_for_spacedomains(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().space_domains.get(
            fields="id,pool_id,pool_name,block_size")
        if resp is not None:
            assert resp.attrs.get("id") is not None
            assert resp.attrs.get("pool_id") is not None
            assert resp.attrs.get("pool_name") is not None
            assert resp.attrs.get("block_size") is not None

    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
