# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest

import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient.v1 import exceptions


'''FCConfigTestCases class tests the fibre channel functionality.
    It covers ports,session,initiator_aliases and interface
    object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for FibreChannel Config TestCases *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for FibreChannel Config TestCases *****\n")
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
def test_get_fc_configs(setup_teardown_for_each_test):
    nimosclientbase.get_nimos_client().fibre_channel_configs.get()


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_fcconfigs_endrow_beyond(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().fibre_channel_configs.get(
            endRow=30)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected.no rows present")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_select_fields_for_fcconfigs(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().fibre_channel_configs.get(
            fields="id,group_leader_array")
        assert resp is not None
        assert resp.attrs.get("id") is not None
        assert resp.attrs.get("group_leader_array") is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            raise ex
