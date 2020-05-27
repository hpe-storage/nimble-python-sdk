# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

'''GroupsTestCase tests the subnet object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Groups TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Groups TestCase *****\n")
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
def test_get_groups(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().groups.list(
        detail=True, limit=2)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_group_discovered_list(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().groups.get()
        assert resp is not None
        resp = nimosclientbase.get_nimos_client(
        ).groups.get_group_discovered_list(id=resp.attrs.get("id"))
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_array_not_found" in str(ex):
            log("Failed as expected. Array id given is invalid")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_test_alert(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().groups.get()
        assert resp is not None
        test_resp = nimosclientbase.get_nimos_client().groups.test_alert(
            id=resp.attrs.get("id"), level="notice")
        test_resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_array_not_found" in str(ex):
            log("Failed as expected. Array id given is invalid")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_group(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().groups.get()
        assert resp is not None
        # save the orig value
        orig_name = resp.attrs.get("name")
        alert_to_email_addrs = resp.attrs.get(
            "alert_to_email_addrs")  # "abc@hpe.com"
        send_alert_to_support = resp.attrs.get("send_alert_to_support")
        isns_enabled = resp.attrs.get("isns_enabled")

        update_resp = nimosclientbase.get_nimos_client().groups.update(
            id=resp.attrs.get("id"),
            name="testname",
            alert_to_email_addrs="alok.ranjxxx@hpe.com",
            send_alert_to_support=False,
            isns_enabled=True)
        update_resp is not None
        # assert the values
        assert update_resp.attrs.get("name") == "testname"
        assert update_resp.attrs.get(
            "alert_to_email_addrs") == "alok.ranjxxx@hpe.com"
        assert update_resp.attrs.get("send_alert_to_support") is False
        assert update_resp.attrs.get("isns_enabled") is True

        # revert to original
        update_resp = nimosclientbase.get_nimos_client().groups.update(
            id=resp.attrs.get("id"),
            name=orig_name,
            alert_to_email_addrs=alert_to_email_addrs,
            send_alert_to_support=send_alert_to_support,
            isns_enabled=isns_enabled)
    except exceptions.NimOSAPIError as ex:
        if "SM_array_not_found" in str(ex):
            log("Failed as expected. Array id given is invalid")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
