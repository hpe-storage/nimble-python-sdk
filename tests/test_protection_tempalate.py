# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

# global variables
protection_template_to_delete = []
prot_template_name1 = nimosclientbase.get_unique_string(
    "unittestcase-protection-template1")

'''ProtectionTemplate TestCase tests the
    ProtectionTemplate object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for ProtectionTemplate TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for ProtectionTemplate TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
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


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_protection_template_name(setup_teardown_for_each_test):
    # only . and : and - are allowed as esp characte..
    try:
        resp = create_protection_template(prot_template_name1)
        assert resp is not None
        get_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.get(id=resp.attrs.get("id"))
        assert get_resp is not None
        assert get_resp.attrs.get("id") == resp.attrs.get("id")
        # retreive all
        getall_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.list(detail=True)
        assert getall_resp is not None
        # by default 3 protection tempalate are on array
        assert getall_resp.__len__() >= 3
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. template name : {prot_template_name1}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_invalid_protection_template_name(setup_teardown_for_each_test):
    try:
        resp = create_protection_template(prot_template_name1+"_")
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. template name : {prot_template_name1}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_invalidlength_protection_template_name(setup_teardown_for_each_test):
    try:
        resp = create_protection_template(
            prot_template_name1+prot_template_name1)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log("Failed as expected. template name : "
                f"{prot_template_name1+prot_template_name1}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_protection_template_name(setup_teardown_for_each_test):
    try:
        resp = create_protection_template(prot_template_name1)
        assert resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. template name : {prot_template_name1}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_protection_template_for_vss_using_insufficient_arguments(
        setup_teardown_for_each_test):
    try:
        resp = create_protection_template(prot_template_name1)
        assert resp is not None
        # for vss all 3 fields app_sync, app_id and app_server is needed
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.update(id=resp.attrs.get("id"),
                                      app_sync='vss',
                                      app_id='sql2005'
                                      )
        assert update_resp is not None
    except exceptions.NimOSAPIError as ex:
        # fiji and below throws SM_http_bad_request as exception
        if "SM_protpol_not_specified" in str(ex) or "SM_http_bad_request" in str(ex):
            log(f"Failed as expected. App server not specifed")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex

@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_protection_template_for_vss_using_required_arguments(
        setup_teardown_for_each_test):
    try:
        resp = create_protection_template(prot_template_name1)
        assert resp is not None
        # for vss all 3 fields app_sync, app_id and app_server is needed
        update_resp = nimosclientbase.get_nimos_client(

        ).protection_templates.update(id=resp.attrs.get("id"),
                                      app_sync='vss',
                                      app_id='sql2016',
                                      app_server="appserver.ns.com"
                                      )
        assert update_resp is not None
        # verify
        assert update_resp.attrs.get("app_server") == "appserver.ns.com"
        assert update_resp.attrs.get("app_id") == "sql2016"
        assert update_resp.attrs.get("app_sync") == "vss"
        assert update_resp.attrs.get("id") == resp.attrs.get("id")

    except exceptions.NimOSAPIError as ex:
        if "SM_protpol_not_specified" in str(ex):
            log("Failed as expected.app server not specifed")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_sql_combination_value_for_vss(setup_teardown_for_each_test):
    try:
        resp = create_protection_template(prot_template_name1)
        assert resp is not None
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.update(
            id=resp.attrs.get("id"),
            app_sync='vss',
            app_id='sql2016',
            app_server="appserver.ns.com"
        )
        assert update_resp is not None
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.update(id=resp.attrs.get("id"),
                                      app_sync='vss',
                                      app_id='sql2014',
                                      app_server="appserver.ns.com"
                                      )
        assert update_resp is not None
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.update(id=resp.attrs.get("id"),
                                      app_sync='vss',
                                      app_id='sql2012',
                                      app_server="appserver.ns.com"
                                      )
        assert update_resp is not None
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.update(id=resp.attrs.get("id"),
                                      app_sync='vss',
                                      app_id='sql2008',
                                      app_server="appserver.ns.com"
                                      )
        assert update_resp is not None
    # now try with sql 2019 as app_sync
        update_resp = nimosclientbase.get_nimos_client(
        ).protection_templates.update(id=resp.attrs.get("id"),
                                      app_sync='vss',
                                      app_id='sql2019',
                                      app_server="appserver.ns.com"
                                      )
        assert update_resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log("Failed as expected.correct sql server not provided")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
