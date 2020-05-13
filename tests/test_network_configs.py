# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alok ranjan
import pytest
import tests.nimbleclientbase as nimosclientbase
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
from nimbleclient import exceptions

'''NetworkconfigTestCase tests the Networkconfig object functionality '''


@pytest.fixture(scope='module')
def before_running_all_testcase(request):
    log("**** Starting Tests for NetworkConfig TestCase *****\n")

    def after_running_all_testcase():
        log("**** Completed Tests for NetworkConfig TestCase *****\n")
    request.addfinalizer(after_running_all_testcase)


@pytest.fixture(scope='function')
def setup_teardown_for_each_test(before_running_all_testcase, request):
    # setup operations before yield is called
    nimosclientbase.log_header(request.function.__name__)
    yield setup_teardown_for_each_test
    # teardown operations below
    nimosclientbase.log_footer(request.function.__name__)


route_list = [
    {
        "gateway": "127.0.0.1",
        "tgt_network": "0.0.0.0",
        "tgt_netmask": "0.0.0.0"
    }
]
subnet_list = [
    {
        "label": "subnet1",
        "network": "127.0.0.0",
        "netmask": "255.0.0.0",
        "type": "mgmt",
        "allow_iscsi": False,
        "allow_group": False,
        "netzone_type": "single",
        "discovery_ip": "127.0.0.102",
        "mtu": 1500,
        "vlan_id": 0
    }
]

array_list = [
    {
        "name": "g1a1",
        # "member_gid": 10,
        "ctrlr_a_support_ip": "127.0.0.11",
        "ctrlr_b_support_ip": "127.0.0.21",
        "nic_list": [
            {
                "name": "eth1",
                "subnet_label": "subnet1",
                "data_ip": "127.0.0.91",
                "tagged": True
            }
        ]
    },
    {
        "name": "g1a2",
        # "member_gid": 11,
        "ctrlr_a_support_ip": "127.0.0.12",
        "ctrlr_b_support_ip": "127.0.0.22",
        "nic_list": [
            {
                "name": "eth1",
                "subnet_label": "subnet1",
                "data_ip": "127.0.0.92",
                "tagged": False
            }
        ]
    }

]


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_get_network_configs_details(setup_teardown_for_each_test):
    resp = nimosclientbase.get_nimos_client().network_configs.list()
    assert resp is not None


@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_check_mandatory_params_network_configs(setup_teardown_for_each_test):
    try:
        resp = nimosclientbase.get_nimos_client().network_configs.create(
            name="draft",
            mgmt_ip="127.0.0.1",
            iscsi_automatic_connection_method=False,
            iscsi_connection_rebalancing=False,
            route_list=route_list,
            subnet_list=subnet_list,
            array_list=array_list
        )
        assert resp is not None
        # the create will in any case fail as the mgmt ip is not correct but
        # atleast we should always get exception "sm_array_not_found"
        # this exception only comes when all the mandatory params are
        # atleast present.values may be incorrect for those param
    except exceptions.NimOSAPIError as ex:
        if "SM_array_not_found" in str(ex):
            log("Failed as expected")
        else:
            log(f"Failed with exception message : {str(ex)}")
            raise ex
