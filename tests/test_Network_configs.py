# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest

nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

import tests.NimbleClientbase as nimosclientBase
from tests.NimbleClientbase import SKIPTEST
from nimbleclient.v1 import exceptions

# below code is needed for debugging.
if __debug__ == True:
    from nimbleclient.v1 import client


class NetworkconfigTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''NetworkconfigTestCase class test the subnet object functionality '''
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
                     #   "member_gid": 10,
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
        
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for NetworkconfigTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(NetworkconfigTestCase, self).tearDown()  
        self.printFooter(self.id()) 
         
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_networkconfigsDetails(self):
                
        #self.printheader('test_get_networkconfigsDetails')       
        resp = nimosclientBase.getNimosClient().network_configs.list()
        self.assertIsNotNone(resp)      
        #self.printfooter('test_get_networkconfigsDetails')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_checkmandatoryParams_networkconfigs(self):
                
        #self.printheader('test_create_checkmandatoryParams_networkconfigs') 
        
        try:            
            resp = nimosclientBase.getNimosClient().network_configs.create(name="draft",
                                                                    mgmt_ip="127.0.0.1",
                                                                    iscsi_automatic_connection_method=False,
                                                                    iscsi_connection_rebalancing=False,
                                                                    route_list=NetworkconfigTestCase.route_list,
                                                                    subnet_list=NetworkconfigTestCase.subnet_list,
                                                                    array_list=NetworkconfigTestCase.array_list
                                                                    )
            self.assertIsNotNone(resp)
            #the create will in any case fail as the mgmt ip is not correct but atleast we should always get exception "sm_array_not_found"
            #this exception only comes when all the mandatory params are atleast present.values may be incorrect for those param
        except exceptions.NimOSAPIError as ex:
            if "SM_array_not_found" in str(ex):
                print("Failed as expected")
            else:
                print(ex)      
        #self.printfooter('test_create_checkmandatoryParams_networkconfigs')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
