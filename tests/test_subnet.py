# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

from tests.nimbleclientbase import SKIPTEST, log_to_file as log
import tests.nimbleclientbase as nimosclientbase
import pytest

'''SubnetTestCase tests the subnet object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Subnet Testcase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Subnet Testcase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture
def setup_teardown(before_running_all_testcase, request):
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown  # provide the fixture value
    # teardown operations below
    nimosclientbase.log_footer(request.function.__name__)


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_subnet_details(setup_teardown):
    # sdk bug. why is subnet object having functions like create,update
    # delete??? the rest doc does not have these. only read is allowed
    resp = nimosclientbase.get_nimos_client().subnets.get()
    assert resp is not None
    # doc shows it has 13 properties.but in replication setup it is 15.
    # just check the length
    assert(resp.attrs.__len__() >= 13)
