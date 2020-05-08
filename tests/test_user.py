# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

user_name1 = "TestCaseUser"
user_to_delete = []

'''ClientUserTestCase tests the user object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for ClienttUser TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for ClientUser TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_user()
    nimosclientbase.log_footer(request.function.__name__)


def delete_user():
    for user_id in user_to_delete:
        try:
            resp = nimosclientbase.get_nimos_client().users.delete(id=user_id)
            assert resp is not None
            log(f" Deleted user with id '{user_id}'")
        except exceptions.NimOSAPIError as ex:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
    user_to_delete.clear()


def create_user(user_name1, **kwargs):
    resp = nimosclientbase.get_nimos_client().users.create(
        name=user_name1, **kwargs)
    user_id = resp.attrs.get("id")
    user_to_delete.append(user_id)
    assert resp is not None
    log(f"Creating testuser with name '{user_name1}' and ID '{user_id}'")
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_user_name_with_unsupported_char(setup_teardown_for_each_test):
    # invalid char present in user_name1.
    try:
        create_user(user_name1, password="password-91")
    except exceptions.NimOSAPIError:
        log(f"Failed as expected. Invalid user_name : {user_name1}")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_user_name_with_more_than_allowed_characters(
        setup_teardown_for_each_test):
    # only 32 char is allowed for user_name1.
    try:
        username = user_name1+user_name1+user_name1+user_name1 + \
            user_name1+user_name1+user_name1+user_name1
        create_user(username, password="password-91")
    except exceptions.NimOSAPIError:
        log(f"Failed as expected. invalid user_name : {username}")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_user_name_with_valid_details(setup_teardown_for_each_test):
    try:
        resp = create_user(user_name1, password="password-91",
                           full_name="alok ranjan",
                           role="administrator",
                           disabled=True)

        # check the role
        assert resp.attrs.get("role") == "administrator"
        # change the role to guest
        resp = nimosclientbase.get_nimos_client().users.update(
            resp.attrs.get("id"), role="guest")
        assert resp.attrs.get("role") == "guest"
    except exceptions.NimOSAPIError:
        log(f"Failed as expected. Invalid user_name : {user_name1}")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_user_password_length(setup_teardown_for_each_test):
    try:
        password = "pass91*"  # minimum length should be 8 excluding & and [];'
        create_user(user_name1, password=password,
                    full_name="alok ranjan",
                    role="administrator",
                    disabled=True)
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. password length is short : {password}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_user_password_invalid_character(setup_teardown_for_each_test):
    try:
        password = "pass91*asda&"
        create_user(user_name1, password=password,
                    full_name="alok ranjan",
                    role="administrator",
                    disabled=True)
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log("Failed as expected. "
                f"Invalid character in password : '{password}'")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
