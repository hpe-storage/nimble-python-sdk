# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

# global variables
app_server_name_1 = nimosclientbase.get_unique_string("appservertc-1")
app_server_to_delete = []


'''Appserver TestCase tests the app server object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for app_server  TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for app_server  TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    global app_server_name_1
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_app_server()
    # create a new unique name for next test case
    app_server_name_1 = nimosclientbase.get_unique_string("appservertc-1")
    nimosclientbase.log_footer(request.function.__name__)


def delete_app_server():
    for app_server_id in app_server_to_delete:
        nimosclientbase.get_nimos_client().application_servers.delete(
            app_server_id)
        log(f" Deleted app server user with id '{app_server_id}'")
    app_server_to_delete.clear()


def create_app_server(app_server, hostname="example.com", **kwargs):
    resp = nimosclientbase.get_nimos_client().application_servers.create(
        name=app_server, hostname=hostname, **kwargs)
    app_server_id = resp.attrs.get("id")
    app_server_to_delete.append(app_server_id)
    assert resp is not None
    log("Created app server with name "
        f"'{app_server}' with Id '{app_server_id}'")
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_app_server(setup_teardown_for_each_test):
    resp = create_app_server(app_server_name_1)
    resp = nimosclientbase.get_nimos_client().application_servers.list(
        detail=True, limit=1)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_app_server(setup_teardown_for_each_test):
    try:
        resp = create_app_server(
            app_server_name_1,
            hostname="example.com")
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_app_server(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().application_servers.create(
            name=app_server_name_1)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. missing mandatory arguments.")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_app_servers_endrow_beyond(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().application_servers.get(
            endRow=30)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected.no rows present")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_select_fields_for_app_server(setup_teardown_for_each_test):
    try:
        resp = create_app_server(app_server_name_1, hostname="example.com")
        resp = nimosclientbase.get_nimos_client().application_servers.get(
            fields="name,hostname,port,creation_time")
        assert resp is not None
        assert resp.attrs.get("name") is not None
        assert resp.attrs.get("hostname") is not None
        assert resp.attrs.get("port") is not None
        assert resp.attrs.get("creation_time") is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_app_server(setup_teardown_for_each_test):
    try:
        resp = create_app_server(app_server=app_server_name_1)
        assert resp is not None
        # update few fields
        update_resp = nimosclientbase.get_nimos_client(
        ).application_servers.update(
            id=resp.attrs.get("id"),
            name="updatedname",
            description="modified by testcase",
            username="abc")
        update_resp is not None
        # assert the values got updated
        assert update_resp.attrs.get("name") == "updatedname"
        assert update_resp.attrs.get("description") == "modified by testcase"
        assert update_resp.attrs.get("username") == "abc"
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
