# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

'''SoftwareVersionsTestCase tests the software version object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Software version TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for  Software version  TestCase *****\n")
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
def test_get_softwareversionsdetails(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().software_versions.get()
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex
