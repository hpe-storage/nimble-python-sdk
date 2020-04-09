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

#global variables
CHAP_NAME_1 = nimosclientBase.getUniqueString("ChapUserTC-1")
CHAP_PASSWORD = "password_25-24"
chapuser_to_delete = []


class ArraysTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ArraysTestCase class test the Arrays object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for ArraysTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(ArraysTestCase, self).tearDown()
        self.printFooter(self.id()) 
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_arrays(self):
                
        #self.printheader('test_get_arrays')       
        resp = nimosclientBase.getNimosClient().arrays.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        #self.printfooter('test_get_arrays')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_iterateArrays_EndRowBeyond(self):
                
        #self.printheader('test_iterateArrays_EndRowBeyond')
        try:
            resp = nimosclientBase.getNimosClient().arrays.get(endRow=10)
            self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected")
            else:
                print(ex)        
        #self.printfooter('test_iterateArrays_EndRowBeyond')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_selectFields_forArrays(self):
                
        #self.printheader('test_selectFields_forArrays')
        try:
            resp = nimosclientBase.getNimosClient().arrays.get(fields="name,pool_name,status,serial")
            self.assertIsNotNone(resp)
            self.assertIsNotNone("name")
            self.assertIsNotNone("pool_name")
            self.assertIsNotNone("status")
            self.assertIsNotNone("serial")

        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected")
            else:
                print(ex)        
        #self.printfooter('test_selectFields_forArrays')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_arrays(self):
                
        #self.printheader('test_create_arrays')
     
        nic_list=[
                      {
                          "subnet_label" : "Management",
                          "data_ip" : "127.0.0.23",
                          "name" : "eth1"
                      },
                      {
                          "subnet_label" : "Management",
                          "data_ip" : "127.0.0.24",
                          "name" : "eth2"
                      },
                      {
                          "subnet_label" : "Management",
                          "data_ip" : "127.0.0.25",
                          "name" : "eth3"
                      },
                      {
                          "subnet_label" : "Management",
                          "data_ip" : "127.0.0.26",
                          "name" : "eth4"
                      }
                  ]
        
        serial="g1a2"
        name="g1a2"
        ctrlr_b_support_ip= "127.0.0.22"
        ctrlr_a_support_ip= "127.0.0.21"
        pool_name="default"
        
        try:                                
            resp = nimosclientBase.getNimosClient().arrays.create(name=name,
                                                       ctrlr_a_support_ip=ctrlr_a_support_ip,
                                                       ctrlr_b_support_ip=ctrlr_b_support_ip,
                                                       pool_name=pool_name,
                                                       nic_list=nic_list,
                                                       serial=serial)
            self.assertIsNotNone(resp)
            
            self.assertEqual(resp.attrs.get("description"),"modified by testcase")
        except exceptions.NimOSAPIError as ex:
            if "SM_enoent" in str(ex):
                print("Failed as expected. no suc array object")
            else:
                print(ex)
        #self.printfooter('test_create_arrays')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_check_mandatoryparams_arrays(self):
                
        #self.printheader('test_check_mandatoryparams_arrays')        
        serial="g1a2"
        name="g1a2"
        ctrlr_b_support_ip= "127.0.0.22"
        ctrlr_a_support_ip= "127.0.0.21"
        pool_name="default"
        
        try:                                
            resp = nimosclientBase.getNimosClient().arrays.create(name=name,
                                                       ctrlr_a_support_ip=ctrlr_a_support_ip,
                                                       ctrlr_b_support_ip=ctrlr_b_support_ip,
                                                       pool_name=pool_name,
                                                    #    nic_list=nic_list,
                                                       serial=serial)
            self.assertIsNotNone(resp)
            
            self.assertEqual(resp.attrs.get("description"),"modified by testcase")
        except exceptions.NimOSAPIError as ex:
            if "SM_missing_arg" in str(ex):
                print("Failed as expected. Some Mandatory arguments missing")
            else:
                print(ex)
        #self.printfooter('test_check_mandatoryparams_arrays')
        

          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
