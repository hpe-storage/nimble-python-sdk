# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient.v1 import exceptions

# global variables
key_name_1 = "default"
passphrase = "passphrase-91"
master_key_to_delete = []

'''master_keyTestCase tests the master key object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for master_key TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for master_key TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_master_key()
    nimosclientbase.log_footer(request.function.__name__)


def delete_master_key():
    for master_key_id in master_key_to_delete:
        nimosclientbase.get_nimos_client().master_key.delete(master_key_id)
        log(f"Deleted master key with Id '{master_key_id}'")
    master_key_to_delete.clear()


def create_master_key(master_key, **kwargs):
    resp = nimosclientbase.get_nimos_client().master_key.create(
        name=master_key, **kwargs)
    master_key_id = resp.attrs.get("id")
    master_key_to_delete.append(master_key_id)
    assert resp is not None
    log("Created master key with name "
        f"'{master_key}' and Id '{master_key_id}'")
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_master_key(setup_teardown_for_each_test):
    resp = create_master_key(key_name_1,
                             passphrase=passphrase)
    resp = nimosclientbase.get_nimos_client().master_key.list(
        detail=True, pageSize=2)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_master_key(setup_teardown_for_each_test):
    try:
        resp = create_master_key(key_name_1,
                                 passphrase=passphrase)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_master_key(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().master_key.create(
            name=key_name_1)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. missing mandatory arguments.")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_master_key_endrow_beyond(setup_teardown_for_each_test):
    try:
        resp = create_master_key(key_name_1,
                                 passphrase=passphrase)
        resp = nimosclientbase.get_nimos_client().master_key.get(endRow=30)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected.no rows present")
        else:
            raise ex

@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_select_fields_for_master_key(setup_teardown_for_each_test):
    try:
        resp = create_master_key(key_name_1,
                                 passphrase=passphrase)
        resp = nimosclientbase.get_nimos_client().master_key.get(
            fields="name,id,active")
        assert resp is not None
        assert resp.attrs.get("name") is not None
        assert resp.attrs.get("id") is not None
        assert resp.attrs.get("active") is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_master_key(setup_teardown_for_each_test):
    try:
        resp = create_master_key(key_name_1,
                                 passphrase=passphrase)
        assert resp is not None
        # update few fields
        update_resp = nimosclientbase.get_nimos_client().master_key.update(
            id=resp.attrs.get("id"),
            name=key_name_1,
            passphrase=passphrase,
            active=False)
        assert update_resp is not None
        # assert the values got updated
        assert update_resp.attrs.get("name") == key_name_1
        assert update_resp.attrs.get("active") is False
        assert update_resp.attrs.get("id") == resp.attrs.get("id")
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected")
        else:
            raise ex
