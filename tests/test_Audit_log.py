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




class AuditLogTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''AuditLogTestCase class test the audit_log object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for AuditLogTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(AuditLogTestCase, self).tearDown()  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_auditlog(self):
                
        self.printHeader('test_get_auditlog')
       
        resp = nimosclientBase.getNimosClient().audit_log.get(pageSize=2)
        self.assertIsNotNone(resp)
        
        self.printFooter('test_get_auditlog')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_auditlog_queryparams(self):
                
        self.printHeader('test_get_auditlog_queryparams')
       
        resp = nimosclientBase.getNimosClient().audit_log.list(detail=True,
                                                      pageSize=2)
        self.assertIsNotNone(resp)        
        resp = nimosclientBase.getNimosClient().audit_log.get(
                                                      pageSize=2,
                                                      fields="user_name,id,status")
        
        #assert that those fields are present
        self.assertIsNotNone(resp.attrs.get("user_name"))
        self.assertIsNotNone(resp.attrs.get("id"))
        self.assertIsNotNone(resp.attrs.get("status"))       
               
        #try asserting a value which was not querying
        self.assertIsNone(resp.attrs.get("startRow"))        
        self.printFooter('test_get_auditlog_queryparams')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_query_Invalid_params(self):
                
                
        self.printHeader('test_query_Invalid_params')       
        try:
            queryparam="junkparam"
            resp = nimosclientBase.getNimosClient().audit_log.get(
                                                      pageSize=2,
                                                      fields=queryparam) 
            self.assertIsNotNone(resp)
            #assert that those fields are present
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_query_param" in str(ex):
                print(f"Failed as expected. Invalid query params provided to query '{queryparam}'")
            else:
                print(ex)
        self.printFooter('test_query_Invalid_params')
        
          

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
