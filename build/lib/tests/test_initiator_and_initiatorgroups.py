# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

from nimbleclient import exceptions
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
import tests.nimbleclientbase as nimosclientbase
import pytest

'''initiatorgroups tests the Initiator and
     initiatorgroup object funtionality '''

# global variables
initiator_grp_name1 = ""
initiator_grp_name2 = ""
initiator_name1 = ""
initiatorgrp_to_delete = []
initiator_to_delete = []


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for Initiatorgroups Testcase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for initiatorgroups Testcase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    global initiator_grp_name1
    global initiator_grp_name2
    global initiator_name1

    initiator_grp_name1 = nimosclientbase.get_unique_string("IGrpTC-IG1")
    initiator_grp_name2 = nimosclientbase.get_unique_string("IGrpTC-IG2")
    initiator_name1 = nimosclientbase.get_unique_string("IGrpTC-Initiator1")
    yield setup_teardown_for_each_test
    # teardown operations below
    delete_initiatorgroup()
    nimosclientbase.log_footer(request.function.__name__)


def create_initiatorgroup(initiator_grp_name, **kwargs):
    resp = nimosclientbase.get_nimos_client().initiator_groups.create(
        name=initiator_grp_name, **kwargs)
    id = resp.attrs.get("id")
    initiatorgrp_to_delete.append(id)
    assert resp is not None
    log(f"created IG with name '{initiator_grp_name}' and Id '{id}'")
    return resp


def delete_initiatorgroup():
    for ig_id in initiatorgrp_to_delete:
        nimosclientbase.get_nimos_client().initiator_groups.delete(ig_id)
        log(f"Deleted IG with Id '{ig_id}'")
    initiatorgrp_to_delete.clear()


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_create_and_delete_initiatorgroup(setup_teardown_for_each_test):

    ig_resp = create_initiatorgroup(initiator_grp_name1,
                                    access_protocol="iscsi",
                                    description="created by testcase"
                                    )
    # assert the values
    assert ig_resp is not None
    assert ig_resp.attrs.get("description") == "created by testcase"
    assert ig_resp.attrs.get("id") == ig_resp.attrs.get("id")
    assert ig_resp.attrs.get("access_protocol") == "iscsi"
    assert ig_resp.attrs.get("name") == initiator_grp_name1


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_initiatorGroup(
        setup_teardown_for_each_test):

    try:
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase"
                                        )
        # assert the values
        assert ig_resp is not None
        assert ig_resp.attrs.get("description") == "created by testcase"
        assert ig_resp.attrs.get("name") == initiator_grp_name1
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. Missing mandatory param")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_initiatorGroup_with_incorrect_access_protocol(
        setup_teardown_for_each_test):
    try:
        access_protocol = "not a valid param. should be FC or iscsi"
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol
                                        )
        # assert the values
        assert ig_resp is not None
        assert ig_resp.attrs.get("id") == initiatorgrp_to_delete[0]
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. Invalid param value {access_protocol}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_duplicate_initiatorgroup(setup_teardown_for_each_test):
    try:
        access_protocol = "iscsi"
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol
                                        )

        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol
                                        )
        # assert the values
        assert ig_resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_duplicate_initiatorgrp" in str(ex):
            log("Failed as expected. "
                f"IG group already present on array '{initiator_grp_name1}'"
                )

        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_initiatorgroup_with_fc_accesss_protocol(
        setup_teardown_for_each_test):
    try:
        access_protocol = "fc"
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol
                                        )
        # assert the values
        assert ig_resp is not None
        assert ig_resp.attrs.get("id") == initiatorgrp_to_delete[0]
    except exceptions.NimOSAPIError as ex:
        if "SM_fc_svc_not_available" in str(ex):
            log(f"Failed as expected. FC service not available")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_initiatorgroups(setup_teardown_for_each_test):
    try:
        access_protocol = "iscsi"
        iscsi_initiators = [
            {
                "label": "itor1",
                "ip_address": "1.1.1.1",
                "iqn": "iqn.1992-01.com.example:storage.tape1.sys1.xyz"
            }
        ]
        ig_resp1 = create_initiatorgroup(initiator_grp_name1,
                                         description="created by testcase",
                                         access_protocol=access_protocol,
                                         iscsi_initiators=iscsi_initiators
                                         )
        assert ig_resp1 is not None
        assert ig_resp1.attrs.get("id") == initiatorgrp_to_delete[0]

        ig_resp2 = create_initiatorgroup(initiator_grp_name2,
                                         description="created by testcase",
                                         access_protocol=access_protocol,
                                         iscsi_initiators=iscsi_initiators
                                         )
        # assert the values
        assert ig_resp2 is not None
        assert ig_resp2.attrs.get("id") == initiatorgrp_to_delete[1]
        # get all the IG groups and check their initiator
        igrps = nimosclientbase.get_nimos_client(
        ).initiator_groups.list(detail=True, limit=2)

        for igobj in igrps:
            if (igobj.attrs.get("name") == initiator_grp_name1
                    or igobj.attrs.get("name") == initiator_grp_name2):
                assert igobj.attrs.get("description") is not None
                assert igobj.attrs.get("description") == "created by testcase"
                assert igobj.attrs.get("access_protocol") is not None
                assert igobj.attrs.get("access_protocol") == "iscsi"
                assert igobj.attrs.get("iscsi_initiators") is not None
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_update_initiatorgroup(setup_teardown_for_each_test):
    try:
        iscsi_initiators = [
            {
                "label": "itor1",
                "ip_address": "1.1.1.1",
                "iqn": "iqn.1992-01.com.example:storage.tape1.sys1.xyz"
            }
        ]
        description = "modified by testcase"
        access_protocol = "iscsi"
        ig_resp = create_initiatorgroup(
            initiator_grp_name1,
            description="created by testcase",
            access_protocol=access_protocol,
        )
        # assert the values
        assert ig_resp is not None
        # update the target_subnet
        update_resp = nimosclientbase.get_nimos_client(
        ).initiator_groups.update(id=ig_resp.attrs.get("id"),
                                  description=description,
                                  iscsi_initiators=iscsi_initiators)
        assert update_resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. Invalid param value")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_initiatorgroup_naming_iscsi(setup_teardown_for_each_test):
    iscsi_initiators1 = [
        {
            "label": "initiator1",
            "ip_address": "10.1.1.1",
            "iqn": "iqn.1998-01.com.nimblestorage:intiator1"
        }
    ]

    iscsi_initiators2 = [
        {
            "label": "initiator2",
            "ip_address": "10.1.1.2",
            "iqn": "iqn.1998-01.com.nimblestorage:intiator2"
        }
    ]

    iscsi_initiators3 = [
        {
            "label": "initiator3",
            "ip_address": "10.1.1.3",
            "iqn": "iqn.1998-01.com.nimblestorage:intiator3"
        }
    ]
    try:
        access_protocol = "iscsi"
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol,
                                        iscsi_initiators=iscsi_initiators1
                                        )
        # assert the values
        assert ig_resp is not None
        assert ig_resp.attrs.get("name") == initiator_grp_name1
        # create one more initiator
        update_resp = nimosclientbase.get_nimos_client().initiators.create(
            initiator_group_id=ig_resp.attrs.get("id"),
            access_protocol=access_protocol,
            label="initiator2",
            iqn="iqn.1998-01.com.nimblestorage:intiator2"
        )
        # assert the values
        assert update_resp is not None
        ig_resp = create_initiatorgroup(initiator_grp_name2,
                                        description="created by testcase",
                                        access_protocol=access_protocol,
                                        iscsi_initiators=iscsi_initiators3
                                        )

        assert ig_resp is not None
        assert ig_resp.attrs.get("name") == initiator_grp_name2
        count = 0
        # get all the initiators and check
        initiatorlist = nimosclientbase.get_nimos_client(
        ).initiators.list(detail=True)

        for initiatorobj in initiatorlist:
            if (initiatorobj.attrs.get("label") == iscsi_initiators1[0]
                ["label"] or
                    initiatorobj.attrs.get("label") == iscsi_initiators2[0]
                    ["label"] or
                    initiatorobj.attrs.get("label") == iscsi_initiators3[0]
                    ["label"]):
                count += 1
        assert count >= 3
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. Invalid param value")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_suggested_lun(setup_teardown_for_each_test):

    try:
        iscsi_initiators1 = [
            {
                "label": "initiator1",
                "ip_address": "10.1.1.1",
                "iqn": "iqn.1998-01.com.nimblestorage:intiator1"
            }
        ]
        access_protocol = "iscsi"
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol,
                                        iscsi_initiators=iscsi_initiators1
                                        )
        assert ig_resp is not None
        suggest_lunresp = nimosclientbase.get_nimos_client(
        ).initiator_groups.suggest_lun(id=ig_resp.attrs.get("id"))
        assert suggest_lunresp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. Invalid param value")
        elif "SM_not_fc_initiatorgrp" in str(ex):
            log(f"Failed as expected due to invalid array setup. FC array groups are required.")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_validate_lun(setup_teardown_for_each_test):
    try:
        iscsi_initiators1 = [
            {
                "label": "initiator1",
                "ip_address": "10.1.1.1",
                "iqn": "iqn.1998-01.com.nimblestorage:intiator1"
            }
        ]
        access_protocol = "iscsi"
        ig_resp = create_initiatorgroup(initiator_grp_name1,
                                        description="created by testcase",
                                        access_protocol=access_protocol,
                                        iscsi_initiators=iscsi_initiators1
                                        )
        assert ig_resp is not None
        validate_lunresp = nimosclientbase.get_nimos_client(
        ).initiator_groups.validate_lun(id=ig_resp.attrs.get("id"), lun=0)
        assert validate_lunresp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg_value" in str(ex):
            log(f"Failed as expected. Invalid param value")
        elif "SM_not_fc_initiatorgrp" in str(ex):
            log(f"Failed as expected due to inavlid array setup. FC array groups are required")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
