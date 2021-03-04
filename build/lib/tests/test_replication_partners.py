# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan

import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient.v1 import client as nimclient
from nimbleclient import exceptions
import tests.test_protection_schedules as prot_sched
import tests.test_snapshots as snapshot
import tests.test_volume as volume
import tests.test_volume_collection as volcoll
import time

# global variables
volcoll_name1 = nimosclientbase.get_unique_string("replicationtc-volcoll1")
# snapcoll_name1 = nimosclientbase.get_unique_string("replicationtc-snapcoll1")
snapshot_name1 = nimosclientbase.get_unique_string("replicationtc-snapshot1")
vol_name1 = nimosclientbase.get_unique_string("replicationtc-vol1")
downstream_partner_id = ""
# constants
REPLICATION_ARRAY_CREDENTIALS = "ReplicationPartnerArrayCredentials"

'''ReplicationPartnerTestCase tests the replication partner
    object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for ReplicationPartner TestCase  *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for ReplicationPartner TestCase  *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    global volcoll_name1, snapshot_name1, vol_name1
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    snapshot.delete_snapshot()
    volume.delete_volume()
    volcoll.delete_volcoll()
    remove_replication_partner()
    # create new name for next test
    volcoll_name1 = nimosclientbase.get_unique_string("replicationtc-volcoll1")
    # snapcoll_name1 = nimosclientbase.get_unique_string(
    #     "replicationtc-snapcoll1")
    snapshot_name1 = nimosclientbase.get_unique_string(
        "replicationtc-snapshot1")
    vol_name1 = nimosclientbase.get_unique_string("replicationtc-vol1")
    nimosclientbase.log_footer(request.function.__name__)


# get the replication partner (downstream) client from config file
def get_downstream_client():
    # read the config which contains array credentials
    arraydetail = nimosclientbase.get_config_section_detail(
        REPLICATION_ARRAY_CREDENTIALS)
    if(arraydetail.__len__() == 3):
        rep_osclient = nimclient.NimOSClient(
            arraydetail[nimosclientbase.ARRAY_HOSTNAME],
            arraydetail[nimosclientbase.ARRAY_USERNAME],
            arraydetail[nimosclientbase.ARRAY_PASSWORD])
    else:
        raise Exception("replication Array credentials "
                        "not present in config file.")
    return rep_osclient


def is_snapshot_replicated(vol_resp):
    snapshot_list_resp = nimosclientbase.get_nimos_client().snapshots.list(
        detail=True, vol_name=vol_resp.attrs.get("name"))
    assert snapshot_list_resp is not None
    for snapshot_obj in snapshot_list_resp:
        # check for replicated flag
        if snapshot_obj.attrs.get("replication_status") == "complete":
            return True
    return False


def get_hostname(config_section_name):
    # read the config which contains array credentials
    arraydetail = nimosclientbase.get_config_section_detail(
        config_section_name)
    if(arraydetail.__len__() == 3):
        return arraydetail[nimosclientbase.ARRAY_HOSTNAME]
    else:
        raise Exception("Replication Array credentials not present in "
                        "config file.")


def get_downstream_partner_detail():
    # get the group name of the downstream array
    downstream_repl_partner = get_downstream_client().groups.get()
    assert downstream_repl_partner is not None
    return downstream_repl_partner


def get_downstream_partner_id():
    downstream_id = None
    downstream_grp_repl_partner = get_downstream_partner_detail()
    # get the upstream repl partner list and check if the list
    # has downstream array details.
    upstream_repl_partner_list = nimosclientbase.get_nimos_client(
        ).replication_partners.list()

    for upstream_repl_partner_obj in upstream_repl_partner_list:
        if upstream_repl_partner_obj.attrs.get(
                "name") == downstream_grp_repl_partner.attrs.get("name"):
            downstream_grp_id = downstream_grp_repl_partner.attrs.get("id")
            grp_name = downstream_grp_repl_partner.attrs.get("name")
            log("Found downstream group Replication: "
                f" {grp_name} with id '{downstream_grp_id}'")
            # we got a  match.
            downstream_id = upstream_repl_partner_obj.attrs.get("id")
            break
    return downstream_id


def test_replication_partner_connection():
    try:

        downstream_partner_id = get_downstream_partner_id()
        if downstream_partner_id is None:
            return

        # we got a  match.
        # test the connection to downstream array.
        nimosclientbase.get_nimos_client(
        ).replication_partners.test(id=downstream_partner_id)

        upstream_grp_resp = nimosclientbase.get_nimos_client().groups.get()
        # get the downstream repl partner list and check if the list
        # has upstream array details.
        downstream_repl_partner_list = get_downstream_client(
            ).replication_partners.list()

        for downstream_repl_partner_obj in downstream_repl_partner_list:
            if downstream_repl_partner_obj.attrs.get(
               "name") == upstream_grp_resp.attrs.get("name"):
                # we got a  match.
                # test the connection to the upstream array.
                id = upstream_grp_resp.attrs.get("id")
                grp_name = upstream_grp_resp.attrs.get("name")
                log("Found upstream group Replication partner for testing "
                    f"connection {grp_name} with id '{id}'")

                get_downstream_client().replication_partners.test(
                    id=downstream_repl_partner_obj.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. mandatory arguments missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


def add_replication_partner():
    try:
        downstream_repl_partner = get_downstream_partner_detail()
        id = downstream_repl_partner.attrs.get("id")
        grp_name = downstream_repl_partner.attrs.get("name")
        log("downstream Replication array details  "
            f"{grp_name} with id '{id}'")

        assert downstream_repl_partner is not None
        try:
            # add the details of downstream in the upstream array
            nimosclientbase.get_nimos_client(
            ).replication_partners.create(
                name=downstream_repl_partner.attrs.get("name"),
                secret="password-91",
                hostname=get_hostname(REPLICATION_ARRAY_CREDENTIALS),
                subnet_label="mgmt-data"
            )
        except exceptions.NimOSAPIError as ex:
            if "SM_eexist" in str(ex):
                log("Replication Array already added. Ignoring this step")

        # get the group name of the upstream array
        upstream_resp = nimosclientbase.get_nimos_client().groups.get()
        assert upstream_resp is not None

        # add the details of upstream to downstream array
        upstream_grp_name = upstream_resp.attrs.get("name")
        get_downstream_client(
        ).replication_partners.create(
            name=upstream_grp_name,
            secret="password-91",
            hostname=get_hostname(nimosclientbase.NIMBLE_ARRAY_CREDENTIALS),
            subnet_label="mgmt-data"
        )
        # test the connection
        test_replication_partner_connection()

    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. mandatory arguments missing")
        elif "SM_eexist" in str(ex):
            log("Replication Partner already added from before")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


def remove_replication_partner():
    try:
        downstream_repl_partner = get_downstream_partner_detail()
        if downstream_repl_partner is None:
            return
        # get the upstream group array name.
        upstream_resp = nimosclientbase.get_nimos_client(
        ).groups.get()

        # get the upstream repl partner list and check if the list
        # has downstream array details.
        upstream_repl_partner_list = nimosclientbase.get_nimos_client(
            ).replication_partners.list()
        for upstream_repl_partner_obj in upstream_repl_partner_list:
            if upstream_repl_partner_obj.attrs.get(
               "name") == downstream_repl_partner.attrs.get("name"):
                id = downstream_repl_partner.attrs.get("id")
                grp_name = downstream_repl_partner.attrs.get("name")
                log("Removing downstream group Replication partner "
                    f"{grp_name} with id '{id}'")
                # we got a  match.
                # remove the details of downstream from the upstream array.
                nimosclientbase.get_nimos_client(
                ).replication_partners.delete(
                    id=upstream_repl_partner_obj.attrs.get("id"))

        # get the downstream repl partner list and check if the list
        # has upstream array details.
        downstream_repl_partner_list = get_downstream_client(
            ).replication_partners.list()
        for downstream_repl_partner_obj in downstream_repl_partner_list:
            if downstream_repl_partner_obj.attrs.get(
               "name") == upstream_resp.attrs.get("name"):
                id = upstream_resp.attrs.get("id")
                grp_name = upstream_resp.attrs.get("name")
                log("Removing upstream group Replication partner "
                    f"{grp_name} with id '{id}'")
                # we got a  match.
                # remove the details of upstream from the downstream array.
                get_downstream_client().replication_partners.delete(
                    id=downstream_repl_partner_obj.attrs.get("id"))
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. mandatory arguments missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_replication_partner_using_invalid_params(
        setup_teardown_for_each_test):
    try:
        create_resp = nimosclientbase.get_nimos_client(
            ).replication_partners.create(
            name="tcreppartner",
            secret="1234566786",
            hostname="10.18.161.229",
            subnet_label="subnet1")
        assert create_resp is not None
    except exceptions.NimOSAPIError:
        log("Failed as expected. rep partner cannot be "
            "created from testcase as no valid data present")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_replication_partner(
        setup_teardown_for_each_test):

    try:
        create_resp = nimosclientbase.get_nimos_client(
        ).replication_partners.create(name="tcreppartner")
        assert create_resp is not None
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. mandatory arguments missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_add_remove_replication_partner(setup_teardown_for_each_test):
    try:
        add_replication_partner()
        remove_replication_partner()
    except exceptions.NimOSAPIError as ex:
        if "SM_missing_arg" in str(ex):
            log("Failed as expected. mandatory arguments missing")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_replication_partner(setup_teardown_for_each_test):
    try:
        get_resp = nimosclientbase.get_nimos_client(
                    ).replication_partners.get()
        if get_resp is None:
            log("ignoring this testcase.this testcase should be run "
                "only on replication setup")
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_replication_partners_endrow_beyond(setup_teardown_for_each_test):
    try:
        nimosclientbase.get_nimos_client().replication_partners.get(endRow=30)
    except exceptions.NimOSAPIError as ex:
        if "SM_end_row_beyond_total_rows" in str(ex):
            log("Failed as expected.no rows present")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


# @pytest.mark.skipif(SKIPTEST is True,
#                     reason="skipped this test as SKIPTEST variable is true")
# def test_select_fields_for_replicationpartners(setup_teardown_for_each_test):

#     try:
#         resp = nimosclientbase.get_nimos_client().replication_partners.get(
#             fields="name,hostname,repl_hostname,pool_name")
#         if resp is not None:
#             assert "name" is not None
#             assert "hostname" is not None
#             assert "repl_hostname" is not None
#             assert "pool_name" is not None
#         else:
#             log("ignoring this testcase.this testcase should be run only "
#                 "on replication setup")
#     except exceptions.NimOSAPIError as ex:
#         if "SM_end_row_beyond_total_rows" in str(ex):
#             log("Failed as expected")
#         else:
#             log(f"Failed with exception message : {str(ex)}")


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_pause_resume_for_replicationpartners(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().replication_partners.get(
            fields="id,name,hostname,repl_hostname,pool_name")
        if resp is not None:
            # pause
            pause_resp = nimosclientbase.get_nimos_client(
                ).replication_partners.pause(id=resp.attrs.get("id"))
            assert pause_resp is not None
            # resume the operation
            resume_resp = nimosclientbase.get_nimos_client(
                ).replication_partners.resume(id=resp.attrs.get("id"))
            assert resume_resp is not None
        else:
            log("Ignoring this testcase.this testcase should be "
                "run only on replication setup")

    except exceptions.NimOSAPIError as ex:
        if "SM_pool_partner_pause_unsup" in str(ex):
            log("Failed as expected.Pool partner does not "
                "support pause and resume operation")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_connectivity_for_replicationpartners(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().replication_partners.get(
            fields="id,name,hostname,repl_hostname,pool_name")
        if resp is not None:
            # tests the connection
            nimosclientbase.get_nimos_client().replication_partners.test(
                id=resp.attrs.get("id"))
        else:
            log("Ignoring this testcase."
                "This testcase should be run only on replication setup")
    except exceptions.NimOSAPIError as ex:
        log(f"Failed with exception message : {str(ex)}")
        raise ex


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_async_replication_workflow(setup_teardown_for_each_test):

    # steps involved.
    # 1.check if we have replication setup.
    # 2.create a volume, volcoll and snapcoll on upstream array
    # 3.create a periodic snapshot schedule for the volcoll
    # 4.see if the snapshot got replicated
    try:
        # step 1.
        log("Creating replication setup")
        add_replication_partner()
        # step 2
        log("Creating a volume, volcoll and snapcoll on upstream array")
        volcoll_resp = volcoll.create_volcoll(volcoll_name1)
        assert volcoll_resp is not None
        vol_resp = volume.create_volume(vol_name1, size=5)
        assert vol_resp is not None
        # associate the volume to volcoll
        vol_associate_resp = nimosclientbase.get_nimos_client(
        ).volumes.associate(
            id=vol_resp.attrs.get("id"), volcoll=volcoll_resp)
        assert vol_associate_resp is not None
        # step 3
        log("Creating Replicated periodic snapshot schedule for the volcoll")
        downstream_partner_id = get_downstream_partner_id()
        log(f"Got downstream_partner_id as '{downstream_partner_id}'")
        resp = prot_sched.create_protection_schedule(
            prot_sched.prot_schedule_name1,
            description="created by testcase for replication",
            volcoll_or_prottmpl_id=volcoll_resp.attrs.get("id"),
            volcoll_or_prottmpl_type="volume_collection",
            period=1,
            period_unit="minutes",
            at_time=0,
            until_time=86399,
            days="all",
            num_retain=1,
            downstream_partner="group-alokr8-va",
            downstream_partner_id=get_downstream_partner_id(),
            replicate_every=1,
            num_retain_replica=1
        )
        assert resp is not None
        # step 4 verify if the snapshot got replicated
        # sleep for sometime and then check if snapshot is replicated
        log("Waiting for 2 minutes for snapshot to be replicated")
        time.sleep(121)
        max_retry = 3
        retry = 1
        while is_snapshot_replicated(vol_resp) is False and retry < max_retry:
            time.sleep(30)
            retry += 1
        if retry == max_retry:
            raise Exception("Snapshot was not replicated")
        else:
            log("Snapshot Successfully replicated.")
    except exceptions.NimOSAPIError as ex:
        if "SM_invalid_arg" in str(ex):
            log(f"Failed as expected . snapshot name {ex}")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
