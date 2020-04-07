# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest

nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

from testcase import NimbleClientbase as nimosclientBase
from nimbleclient.v1 import exceptions

# below code is needed for debugging.
if __debug__ == True:
    from nimbleclient.v1 import client

#global variables

#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))




class GroupsTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''GroupsTestCase class test the subnet object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for GroupsTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(GroupsTestCase, self).tearDown()  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_groups(self):
                
        self.printHeader('test_get_groups')
        #sdk bug. why is subnet object having functions like create,update delete??? the rest doc does not have these. only read is allowed
        resp = nimosclientBase.getNimosClient().groups.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        self.printFooter('test_get_groups')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_group_discovered_list(self):
                
        self.printHeader('test_get_group_discovered_list')
        try:
            resp = nimosclientBase.getNimosClient().groups.get()
            self.assertIsNotNone(resp)
            resp = nimosclientBase.getNimosClient().groups.get_group_discovered_list(id=resp.attrs.get("id"))
            self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
           if "SM_array_not_found" in str(ex):
               print("Failed as expected. Array id given is invalid")
           else:
               print(ex)
        self.printFooter('test_get_group_discovered_list')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_test_alert(self):
                
        self.printHeader('test_test_alert')
        try:
            resp = nimosclientBase.getNimosClient().groups.get()
            self.assertIsNotNone(resp)
            testresp = nimosclientBase.getNimosClient().groups.test_alert(id=resp.attrs.get("id"),level="notice")
            self.assertIsNotNone(testresp)
            
        except exceptions.NimOSAPIError as ex:
           if "SM_array_not_found" in str(ex):
               print("Failed as expected. Array id given is invalid")
           else:
               print(ex)
        self.printFooter('test_test_alert')
        
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_update_group(self):
                
        self.printHeader('test_update_group')
        try:
            resp = nimosclientBase.getNimosClient().groups.get()
            self.assertIsNotNone(resp)
            #save the orig value
            origname=resp.attrs.get("name")
            alert_to_email_addrs=resp.attrs.get("alert_to_email_addrs")#"alok.ranjan2@hpe.com"
            send_alert_to_support=resp.attrs.get("send_alert_to_support")
            isns_enabled=resp.attrs.get("isns_enabled")
            
            updateresp = nimosclientBase.getNimosClient().groups.update(id=resp.attrs.get("id"),
                                                            name="testname",
                                                            alert_to_email_addrs="alok.ranjan2@hpe.com",
                                                            send_alert_to_support=False,
                                                            isns_enabled=True)
            self.assertIsNotNone(updateresp)
            #assert the values
            self.assertEqual(updateresp.attrs.get("name"),"testname")
            self.assertEqual(updateresp.attrs.get("alert_to_email_addrs"),"alok.ranjan2@hpe.com")
            self.assertEqual(updateresp.attrs.get("send_alert_to_support"),False)
            self.assertEqual(updateresp.attrs.get("isns_enabled"),True)
            
            #revert to original
            updateresp = nimosclientBase.getNimosClient().groups.update(id=resp.attrs.get("id"),
                                                            name=origname,
                                                            alert_to_email_addrs=alert_to_email_addrs,
                                                            send_alert_to_support=send_alert_to_support,
                                                            isns_enabled=isns_enabled)            

        except exceptions.NimOSAPIError as ex:
           if "SM_array_not_found" in str(ex):
               print("Failed as expected. Array id given is invalid")
           else:
               print(ex)
        self.printFooter('test_update_group')
        

          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':
        #print("from main ")             
        if nimosclientBase.CONSOLELOG == False:
            #means the test was run using python -m 
            main(nimosclientBase.getUnittestlogfile())
        else:
            unittest.main()
else:
    #means the test was run using python -m 
    main(nimosclientBase.getUnittestlogfile())
