# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST,array_version, log_to_file as log
from nimbleclient import exceptions


'''Controller TestCase tests the controller object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Controller TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Controller TestCase *****\n")
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
def test_controllers(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().controllers.get()
    assert resp is not None


# endRow param is supported with array_versions > 5.2
@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_controllers_endrow_beyond(setup_teardown_for_each_test):

    if nimosclientbase.is_array_version_above_or_equal("5.2"):
        try:
            resp = nimosclientbase.get_nimos_client().controllers.list(
                detail=True, endRow=30)
            assert resp is not None
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                log("Failed as expected.no rows present")
            else:
                log(f"Failed with exception message : {str(ex)}")
                raise ex
    else:
        log(f"Skipped this testcase as it is not supported for array version {array_version} ")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_select_fields_for_controllers(setup_teardown_for_each_test):
    if nimosclientbase.is_array_version_above_or_equal("5.2"):
        try:
            resp = nimosclientbase.get_nimos_client().controllers.get(
                fields="name,hostname")
            assert resp is not None
            assert resp.attrs.get("name") is not None
            assert resp.attrs.get("hostname") is not None
            # try asserting a value which was not querying
            assert resp.attrs.get("port") is None
            assert resp.attrs.get("creation_time") is None
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                log("Failed as expected")
            else:
                log(f"Failed with exception message : {str(ex)}")
                raise ex
    else:
        log(f"Skipped this testcase as it is not supported for array version {array_version} ")
