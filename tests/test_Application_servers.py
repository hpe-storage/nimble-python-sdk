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
APP_SERVER_NAME_1 = nimosclientBase.getUniqueString("AppServerTC-1")

appserver_to_delete = []
#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))




class AppServerTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''AppServerTestCase class test the app servers object functionality '''    
    
    print("**** Running Tests for AppServerTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(AppServerTestCase, self).tearDown()
        self.deleteTestAppservers() 
        
        
    def deleteTestAppservers(self):
        for appserverId in appserver_to_delete:              
             nimosclientBase.getNimosClient().application_servers.delete(appserverId)
        appserver_to_delete.clear()
        
        
    def createTestAppservers(self,appserver,hostname="example.com",**kwargs):
        resp =  nimosclientBase.getNimosClient().application_servers.create(name=appserver,hostname=hostname,**kwargs)
        appserver_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp   
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_appservers(self):
                
        self.printHeader('test_get_appservers') 
        resp = self.createTestAppservers(APP_SERVER_NAME_1)      
        resp =  nimosclientBase.getNimosClient().application_servers.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        self.printFooter('test_get_appservers')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_appservers(self):
                
        self.printHeader('test_create_appservers')
        try:       
           resp = self.createTestAppservers(APP_SERVER_NAME_1,
                                            hostname="example.com")
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            print(ex)              
        self.printFooter('test_create_appservers')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_check_mandatoryparams_appservers(self):
                
        self.printHeader('test_check_mandatoryparams_appservers')
        try:       
           resp =  nimosclientBase.getNimosClient().application_servers.create(name=APP_SERVER_NAME_1)
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_missing_arg" in str(ex):
                print("Failed as expected. missing mandatory arguments.")
            else:
                print(ex)              
        self.printFooter('test_check_mandatoryparams_appservers')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_appservers_endrowBeyond(self):
                
        self.printHeader('test_appservers_endrowBeyond')
        try:       
           resp =  nimosclientBase.getNimosClient().application_servers.get(endRow=30)
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected.no rows present")
            else:
                print(ex)              
        self.printFooter('test_appservers_endrowBeyond')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_selectFields_for_AppServers(self):
                
        self.printHeader('test_selectFields_for_AppServers')
        try:
            resp = self.createTestAppservers(APP_SERVER_NAME_1,hostname="example.com")
            resp =  nimosclientBase.getNimosClient().application_servers.get(fields="name,hostname,port,creation_time")
            self.assertIsNotNone(resp)
            self.assertIsNotNone("name")
            self.assertIsNotNone("hostname")
            self.assertIsNotNone("port")
            self.assertIsNotNone("creation_time")

        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected")
            else:
                print(ex)        
        self.printFooter('test_selectFields_for_AppServers')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_update_AppServers(self):
                
        self.printHeader('test_update_AppServers')
        try:
            resp = self.createTestAppservers(appserver=APP_SERVER_NAME_1)
            self.assertIsNotNone(resp)
            #update few fields
            updateresp =  nimosclientBase.getNimosClient().application_servers.update(id=resp.attrs.get("id"),
                                                                             name="updatedname",
                                                                             description="modified by testcase",
                                                                             username="alok")
            self.assertIsNotNone(updateresp)
            #assert the values got updated
            self.assertEqual(updateresp.attrs.get("name"),"updatedname")
            self.assertEqual(updateresp.attrs.get("description"),"modified by testcase")
            self.assertEqual(updateresp.attrs.get("username"),"alok")

        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected")
            else:
                print(ex)        
        self.printFooter('test_update_AppServers')
        
        
              
          

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
