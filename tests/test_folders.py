# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log

# global variables
folders_name_1 = nimosclientbase.get_unique_string("foldertc-1")
folders_to_delete = []

'''FoldersTestCase tests the folders object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Folders TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Folders TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_folders()
    nimosclientbase.log_footer(request.function.__name__)


def delete_folders():
    for folder_id in folders_to_delete:
        nimosclientbase.get_nimos_client().folders.delete(folder_id)
        log(f"Deleted folders with Id '{folder_id}'")
    folders_to_delete.clear()


def create_folders(folder_name, **kwargs):
    resp = nimosclientbase.get_nimos_client().folders.create(
        name=folder_name, **kwargs)
    folder_id = resp.attrs.get("id")
    folders_to_delete.append(folder_id)
    assert resp is not None
    log("Created folder with name "
        f"'{folder_name}' and Id '{folder_id}'")
    assert resp is not None
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_folders(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().folders.list(
        detail=True, pageSize=200)
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_folders(setup_teardown_for_each_test):
    # folder creation requires pool_id. hence first get the ppol id
    pool_resp = nimosclientbase.get_nimos_client().pools.get()
    resp = create_folders(
        folder_name=folders_name_1,
        pool_id=pool_resp.attrs.get("id"),
        description="created by testcase",
        limit_bytes=2000)
    assert resp is not None
    assert resp.attrs.get("name") == folders_name_1
    assert resp.attrs.get("description") == "created by testcase"
    assert resp.attrs.get("limit_bytes") == 2000


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_folders(setup_teardown_for_each_test):
    # folder creation requires pool_id. hence first get the ppol id
    pool_resp = nimosclientbase.get_nimos_client().pools.get()
    resp = create_folders(
        folder_name=folders_name_1,
        pool_id=pool_resp.attrs.get("id"),
        description="created by testcase",
        limit_bytes=2000)
    assert resp is not None
    assert resp.attrs.get("name") == folders_name_1
    assert resp.attrs.get("description") == "created by testcase"
    assert resp.attrs.get("limit_bytes") == 2000

    # update few fields
    update_resp = nimosclientbase.get_nimos_client().folders.update(
        id=resp.attrs.get("id"),
        description="modified by testcase",
        limit_bytes=4000,
        name="folderupdatetestcase")
    update_resp is not None
    assert update_resp.attrs.get("name") == "folderupdatetestcase"
    assert update_resp.attrs.get("description") == "modified by testcase"
    assert update_resp.attrs.get("limit_bytes") == 4000
