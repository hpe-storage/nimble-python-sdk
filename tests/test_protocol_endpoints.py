# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log

'''ProtocolEndpoints TestCase tests the
        ProtocolEndpoints object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for ProtocolEndpoints TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for ProtocolEndpoints TestCase *****\n")
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
def test_getprotocolendpoints(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client(
    ).protocol_endpoints.list(detail=True, pageSize=2)
    assert resp is not None
