# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

# global variables
perf_policy_name1 = ""
performancepolicy_to_delete = []

'''PerformancePoliciesTestCase tests the Performance
     Policies object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Performance Policies TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for Performance Policies TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    global perf_policy_name1
    # setup operations before yield is called
    perf_policy_name1 = nimosclientbase.get_unique_string(
        "unittestcase-perfpolicy1")
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_perf_policy()
    nimosclientbase.log_footer(request.function.__name__)


def delete_perf_policy():
    for perf_policy_id in performancepolicy_to_delete:
        try:
            resp = nimosclientbase.get_nimos_client(
            ).performance_policies.delete(id=perf_policy_id)
            assert resp is not None
            log("Deleted performance policy with Id '{perf_policy_id}'")
        except exceptions.NimOSAPIError as ex:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
    performancepolicy_to_delete.clear()


def create_perf_policy(perf_policy_name, **kwargs):
    resp = nimosclientbase.get_nimos_client().performance_policies.create(
        name=perf_policy_name, **kwargs)
    perf_policy_id = resp.attrs.get("id")
    performancepolicy_to_delete.append(perf_policy_id)
    assert resp is not None
    log("Created performance policy with name "
        f"'{perf_policy_name}' and Id '{perf_policy_id}'")
    assert resp is not None
    return resp


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_perf_policies(setup_teardown_for_each_test):
    # only . and : and - are allowed as esp characte..
    try:
        # first get the default ones
        getall_resp = nimosclientbase.get_nimos_client(
        ).performance_policies.list()
        assert getall_resp is not None
        # create one
        resp = create_perf_policy(
            perf_policy_name1,
            description="created by testcase",
            block_size=8192,
        )
        assert resp is not None
        # match the value
        get_resp = nimosclientbase.get_nimos_client().performance_policies.get(
            id=resp.attrs.get("id"))
        assert get_resp is not None
        assert get_resp.attrs.get("id") == performancepolicy_to_delete[0]
        assert get_resp.attrs.get("description") == "created by testcase"
        assert get_resp.attrs.get("block_size") == 8192
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_perf_policies_using_invalid_app_category(
        setup_teardown_for_each_test):
    try:
        # create one
        resp = create_perf_policy(
            perf_policy_name1,
            description="created by testcase",
            block_size=8192,
            app_category="test"  # invalid app category
        )
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_perfpol_invalid_app_category" in str(ex):
            log("Failed as expected. Invalid app category provided.")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_perf_policies_using_invalid_name(setup_teardown_for_each_test):
    try:
        # create one
        perf_name = perf_policy_name1 + "-;,"
        resp = create_perf_policy(
            perf_name,
            description="created by testcase",
            block_size=8192,
            app_category="test"  # invalid app category
        )
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. Invalid name provided {perf_name}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_perf_policies(setup_teardown_for_each_test):
    try:
        # create one
        resp = create_perf_policy(
            perf_policy_name1,
            description="created by testcase",
            block_size=8192,
            app_category="db2"
        )
        assert resp is not None
        # match the value
        get_resp = nimosclientbase.get_nimos_client(
        ).performance_policies.get(id=resp.attrs.get("id"))
        assert get_resp is not None
        assert get_resp.attrs.get("id") == performancepolicy_to_delete[0]
        assert get_resp.attrs.get("description") == "created by testcase"
        assert get_resp.attrs.get("block_size") == 8192
        assert get_resp.attrs.get("app_category") == "db2"

        # update the app category field
        update_resp = nimosclientbase.get_nimos_client(
        ).performance_policies.update(id=resp.attrs.get("id"),
                                      description="modified by testcase",
                                      app_category="exchange")
        assert update_resp is not None
        assert update_resp .attrs.get("id") == performancepolicy_to_delete[0]
        assert update_resp .attrs.get("description") == "modified by testcase"
        assert update_resp .attrs.get("app_category") == "exchange"

    except exceptions.NimOSAPIError as ex:
        if "SM_perfpol_invalid_app_category" in str(ex):
            log("Failed as expected. Invalid app category provided.")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_delete_perf_policies(setup_teardown_for_each_test):
    try:
        # create one
        resp = create_perf_policy(perf_policy_name1,
                                  description="created by testcase",
                                  block_size=8192,
                                  app_category="db2"
                                  )
        assert resp is not None
        # match the value
        get_resp = nimosclientbase.get_nimos_client(
            ).performance_policies.get(id=resp.attrs.get("id"))
        assert get_resp is not None
        assert get_resp.attrs.get("id") == performancepolicy_to_delete[0]
        assert get_resp.attrs.get("description") == "created by testcase"
        assert get_resp.attrs.get("block_size") == 8192
        assert get_resp.attrs.get("app_category") == "db2"

        # delete the policy
        delete_resp = nimosclientbase.get_nimos_client(
                ).performance_policies.delete(id=get_resp.attrs.get("id"))
        assert delete_resp . __len__() == 0
        performancepolicy_to_delete.remove(resp.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        if "SM_perfpol_invalid_app_category" in str(ex):
            log("Failed as expected. Invalid app category provided.")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
