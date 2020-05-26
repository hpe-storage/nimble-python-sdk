# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

'''EventsTestCase tests the events object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Events TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Events TestCase *****\n")
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
def test_get_events(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().events.list(
        detail=True, limit=2)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_event_log_query_params(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().events.list(detail=True,
                                                          limit=2)
    assert resp is not None
    resp = nimosclientbase.get_nimos_client().events.get(
        limit=2,
        fields="activity,id,category,severity")
    assert resp is not None
    # assert that those fields are present
    assert resp.attrs.get("activity") is not None
    assert resp.attrs.get("id") is not None
    assert resp.attrs.get("category") is not None
    assert resp.attrs.get("severity") is not None
    # try asserting a value which was not querying
    assert resp.attrs.get("startRow") is None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_query_invalid_params(setup_teardown_for_each_test):
    try:
        queryparam = "junkparam"
        resp = nimosclientbase.get_nimos_client().events.get(
            limit=2,
            fields=queryparam)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_query_param" in str(ex):
            log("Failed as expected. "
                f"Invalid query params provided to query '{queryparam}'")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
