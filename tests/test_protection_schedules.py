# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

# global variables
protection_template_to_delete = []
protection_schedule_to_delete = []
prot_template_name1 = nimosclientbase.get_unique_string(
    "unittestcase-protecttemplate1")
prot_schedule_name1 = nimosclientbase.get_unique_string(
    "unittestcase-protectschedule1")


'''protection_schedule TestCase tests the protection_schedule
    object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for protection_schedule TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for protection_schedule TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    global prot_template_name1, prot_schedule_name1
    nimosclientbase.log_header(request.function.__name__)

    prot_template_name1 = nimosclientbase.get_unique_string(
        "unittestcase-protecttemplate1")
    prot_schedule_name1 = nimosclientbase.get_unique_string(
        "unittestcase-protectschedule1")
    resp = create_protection_template(prot_template_name1)
    assert resp is not None
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_protection_template()
    nimosclientbase.log_footer(request.function.__name__)


def delete_protection_template():
    for protection_template_id in protection_template_to_delete:
        try:
            resp = nimosclientbase.get_nimos_client(
            ).protection_templates.delete(id=protection_template_id)
            assert resp is not None
            log("Deleted protection template with "
                f"Id '{protection_template_id}'")
        except exceptions.NimOSAPIError as ex:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
    protection_template_to_delete.clear()


def create_protection_template(protection_template_name):
    resp = nimosclientbase.get_nimos_client().protection_templates.create(
        name=protection_template_name, description="created by testcase")
    protection_template_id = resp.attrs.get("id")
    protection_template_to_delete.append(protection_template_id)
    assert resp is not None
    log("Created protection template with name "
        f"'{protection_template_name}' and Id '{protection_template_id}'")
    return resp


def create_protection_schedule(protection_schedule_name, **kwargs):
    resp = nimosclientbase.get_nimos_client().protection_schedules.create(
        name=protection_schedule_name, **kwargs)
    protection_schedule_id = resp.attrs.get("id")
    protection_schedule_to_delete.append(protection_schedule_id)
    assert resp is not None
    log("Created protection schedule with name "
        f"'{protection_schedule_name}' and Id '{protection_schedule_id}'")
    return resp

@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_protection_schedules(setup_teardown_for_each_test):

    try:
        resp = create_protection_schedule(
            prot_schedule_name1,
            description="created by testcase",
            volcoll_or_prottmpl_id=protection_template_to_delete[0],
            volcoll_or_prottmpl_type="protection_template",
            num_retain=1)
        assert resp is not None
        get_resp = nimosclientbase.get_nimos_client(
        ).protection_schedules.get(id=resp.attrs.get("id"))
        assert get_resp is not None
        assert get_resp.attrs.get("id") == resp.attrs.get("id")

        # retreive all
        getall_resp = nimosclientbase.get_nimos_client(
        ).protection_schedules.list()
        assert getall_resp is not None
        # by default 6 protection schedule are on array
        assert getall_resp.__len__() >= 6
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. template name : {prot_template_name1}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_protection_schedules(
        setup_teardown_for_each_test):
    # create requires "volcoll_or_prottmpl_id" and "volcoll_or_
    # prottmpl_type" for creating schedule
    try:
        resp = create_protection_schedule(prot_schedule_name1)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log(f"Failed as expected. mandatory params missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_protection_schedules(setup_teardown_for_each_test):
    try:
        resp = create_protection_schedule(
            prot_schedule_name1,
            description="created by testcase",
            volcoll_or_prottmpl_id=protection_template_to_delete[0],
            volcoll_or_prottmpl_type="protection_template",
            num_retain=1)
        assert resp is not None
        assert "created by testcase" == resp.attrs.get("description")
        assert prot_schedule_name1 == resp.attrs.get("name")
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. some params missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_protection_schedules(setup_teardown_for_each_test):
    try:
        resp = create_protection_schedule(
            prot_schedule_name1,
            description="created by testcase",
            volcoll_or_prottmpl_id=protection_template_to_delete[0],
            volcoll_or_prottmpl_type="protection_template",
            num_retain=1)
        assert resp is not None
        # update few fields and check it works
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_schedules.update(
            id=resp.attrs.get("id"),
            description="modified by testcase",
            period_unit="hours",
            days="monday",
            num_retain=7)
        assert update_resp is not None
        assert "modified by testcase" == update_resp.attrs.get("description")
        assert 7 == update_resp.attrs.get("num_retain")
        assert update_resp.attrs.get("period_unit") == "hours"
        assert update_resp.attrs.get("days") == "monday"
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex
