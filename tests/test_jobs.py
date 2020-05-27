# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import threading
import time
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log

# global variables

'''JobsTestCase tests the jobs object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Jobs TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Jobs TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    nimosclientbase.log_footer(request.function.__name__)


def start_temp_job(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().software_versions.get()
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_jobs(setup_teardown_for_each_test):

    # start an autosupport job and then call job to check for the sattus
    autosupport_thread = threading.Thread(target=start_temp_job)
    autosupport_thread.start()
    time.sleep(4)
    resp = nimosclientbase.get_nimos_client().jobs.list(
        detail=True, limit=2)
    assert resp is not None
    autosupport_thread.join()
