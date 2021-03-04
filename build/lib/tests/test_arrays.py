# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

'''ArraysTestCase tests the Arrays object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Arrays TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Arrays TestCase *****\n")
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
def test_get_arrays(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().arrays.list(
        detail=True, limit=2)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_iterate_arrays_endRow_beyond(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().arrays.get(endRow=10)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_select_fields_for_arrays(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().arrays.get(
            fields="name,pool_name,status,serial")
        assert resp is not None
        assert resp.attrs.get("name") is not None
        assert resp.attrs.get("pool_name") is not None
        assert resp.attrs.get("status") is not None
        assert resp.attrs.get("serial") is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_arrays(setup_teardown_for_each_test):
    nic_list = [
        {
            "subnet_label": "management",
            "data_ip": "127.0.0.23",
            "name": "eth1"
        },
        {
            "subnet_label": "management",
            "data_ip": "127.0.0.24",
            "name": "eth2"
        },
        {
            "subnet_label": "management",
            "data_ip": "127.0.0.25",
            "name": "eth3"
        },
        {
            "subnet_label": "management",
            "data_ip": "127.0.0.26",
            "name": "eth4"
        }
    ]

    serial = "g1a2"
    name = "g1a2"
    ctrlr_b_support_ip = "127.0.0.22"
    ctrlr_a_support_ip = "127.0.0.21"
    pool_name = "default"

    try:
        resp = nimosclientbase.get_nimos_client().arrays.create(
            name=name,
            ctrlr_a_support_ip=ctrlr_a_support_ip,
            ctrlr_b_support_ip=ctrlr_b_support_ip,
            pool_name=pool_name,
            nic_list=nic_list,
            serial=serial)
        assert resp is not None
        assert resp.attrs.get("description") == "modified by testcase"
    except exceptions.NimOSAPIError as ex:
        if "SM_enoent" in str(ex) or "SM_http_not_found" in str(ex):
            log("Failed as expected. no suc array object")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_arrays(setup_teardown_for_each_test):
    serial = "g1a2"
    name = "g1a2"
    ctrlr_b_support_ip = "127.0.0.22"
    ctrlr_a_support_ip = "127.0.0.21"
    pool_name = "default"

    try:
        resp = nimosclientbase.get_nimos_client().arrays.create(
            name=name,
            ctrlr_a_support_ip=ctrlr_a_support_ip,
            ctrlr_b_support_ip=ctrlr_b_support_ip,
            pool_name=pool_name,
            # nic_list=nic_list,
            serial=serial)
        assert resp is not None
        assert resp.attrs.get("description") == "modified by testcase"
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. some mandatory arguments missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
