# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient.v1 import exceptions


# global variables
vol_name1 = nimosclientbase.get_unique_string("volumetc-vol1")
initiator_grp_name1 = nimosclientbase.get_unique_string("igrptc-ig1")

'''ACLTestCase tests the acl object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for ACL TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for ACL TestCase *****\n")
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
def test_create_and_delete_acl(setup_teardown_for_each_test):
    try:
        # first create a volume.
        vol_resp = nimosclientbase.get_nimos_client().volumes.create(
            name=vol_name1, size=10)
        assert vol_resp is not None
        # create an initiator group
        ig_resp = nimosclientbase.get_nimos_client().initiator_groups.create(
            name=initiator_grp_name1,
            description="created by testcase",
            access_protocol="iscsi")
        ig_resp is not None
        # create the acl
        acl_resp = nimosclientbase.get_nimos_client(
        ).access_control_records.create(
            apply_to="both",
            initiator_group_id=ig_resp.attrs.get("id"),
            vol_id=vol_resp.attrs.get("id"))
        assert acl_resp is not None
        # assert that it has been applied
        assert acl_resp.attrs.get("vol_id") == vol_resp.attrs.get("id")
        assert acl_resp.attrs.get("initiator_group_name"
                                  ) == ig_resp.attrs.get("name")
        assert acl_resp.attrs.get("apply_to") == "both"

        # cleanup
        acl_resp = nimosclientbase.get_nimos_client(
        ).access_control_records.delete(id=acl_resp.attrs.get("id"))
        ig_resp = nimosclientbase.get_nimos_client().initiator_groups.delete(
            id=ig_resp.attrs.get("id"))
        assert ig_resp is not None
        vol_resp = nimosclientbase.get_nimos_client().volumes.offline(
            id=vol_resp.attrs.get("id"))
        vol_resp = nimosclientbase.get_nimos_client().volumes.delete(
            id=vol_resp.get("id"))
        assert vol_resp is not None
    except exceptions.NimOSAPIError as ex:
        raise ex
