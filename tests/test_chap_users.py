# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

# global variables
chap_name_1 = nimosclientbase.get_unique_string("chapusertc-1")
chap_password = "password_25-24"
chap_user_to_delete = []

'''Chapusers TestCase tests the chap users object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for chap_users TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for chap_users TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_chap_user()
    nimosclientbase.log_footer(request.function.__name__)


def delete_chap_user():
    for chap_user_id in chap_user_to_delete:
        nimosclientbase.get_nimos_client().chap_users.delete(chap_user_id)
        log(f" Deleted chap user with id '{chap_user_id}'")
    chap_user_to_delete.clear()


def create_chap_user(user_name, password, **kwargs):
    resp = nimosclientbase.get_nimos_client().chap_users.create(
        name=user_name, password=password, **kwargs)
    chap_user_id = resp.attrs.get("id")
    chap_user_to_delete.append(chap_user_id)
    assert resp is not None
    log(f"Created chap user with name '{user_name} ' and Id '{chap_user_id}'")
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_chap_users(setup_teardown_for_each_test):
    resp = create_chap_user(
        user_name=chap_name_1,
        password=chap_password,
        description="created by testcase"
    )
    resp = nimosclientbase.get_nimos_client().chap_users.list(
        detail=True, pageSize=2)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_chap_users(setup_teardown_for_each_test):
    resp = create_chap_user(
        user_name=chap_name_1,
        password=chap_password,
        description="created by testcase"
    )
    assert resp is not None
    assert resp.attrs.get("name") == chap_name_1
    assert resp.attrs.get("description") == "created by testcase"


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_chap_users_using_invalid_password(setup_teardown_for_each_test):
    try:
        resp = create_chap_user(
            user_name=chap_name_1,
            password="sadhs",
            description="created by testcase"
        )
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log("Failed as expected. password length short")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_delete_invalid_chap_users(setup_teardown_for_each_test):
    resp = create_chap_user(
        user_name=chap_name_1,
        password=chap_password,
        description="created by testcase"
    )
    assert resp is not None
    assert resp.attrs.get("name") == chap_name_1
    assert resp.attrs.get("description") == "created by testcase"
    try:
        resp = nimosclientbase.get_nimos_client().chap_users.delete(
            id="213812497124712041adhjasjdgassqqwjahsdaskdk")
    except exceptions.NimOSAPIError as ex:
        if"SM_invalid_path_variable" in str(ex):
            log("Failed as expected. Invalid Id to delete")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_chap_users(setup_teardown_for_each_test):
    resp = create_chap_user(
        user_name=chap_name_1,
        password=chap_password,
        description="created by testcase"
    )
    assert resp is not None
    assert resp.attrs.get("name") == chap_name_1
    assert resp.attrs.get("description") == "created by testcase"
    # update few fields
    update_resp = nimosclientbase.get_nimos_client().chap_users.update(
        id=resp.attrs.get("id"),
        description="modified by testcase",
        name="updatechapusertestcase")
    update_resp is not None
    assert update_resp.attrs.get("name") == "updatechapusertestcase"
    assert update_resp.attrs.get("description") == "modified by testcase"
