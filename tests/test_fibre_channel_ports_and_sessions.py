# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log


'''FCTestCases tests the fibre channel functionality. it covers
    ports,session, initiator_aliases and interface object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for FibreChannel ports and "
        "session TestCases *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for FibreChannel ports "
            "and session TestCases *****\n")
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
def test_get_fc_ports(setup_teardown_for_each_test):
    nimosclientbase.get_nimos_client().fibre_channel_ports.get()


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_fc_sessions(setup_teardown_for_each_test):
    nimosclientbase.get_nimos_client().fibre_channel_sessions.get()


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_fc_interfaces(setup_teardown_for_each_test):
    nimosclientbase.get_nimos_client().fibre_channel_interfaces.get()


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_fc_initiators_aliases(setup_teardown_for_each_test):
    nimosclientbase.get_nimos_client().fibre_channel_initiator_aliases.get()
