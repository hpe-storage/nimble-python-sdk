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


class ChapUsersTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ChapUsersTestCase class test the chap users object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for ChapUsersTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(ChapUsersTestCase, self).tearDown() 
        self.deleteTestChapUser()
        self.printFooter(self.id())
        
    
    def deleteTestChapUser(self):
        for chapuserId in chapuser_to_delete:              
           nimosclientBase.getNimosClient().chap_users.delete(chapuserId)
        chapuser_to_delete.clear()
        
        
    def createTestChapUser(self,username,password,**kwargs):
        print(f"Creating Chap User with name '{username}'")
        resp =nimosclientBase.getNimosClient().chap_users.create(name=username,password=password,**kwargs)
        chapuser_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_chapUsers(self):
                
        #self.printheader('test_get_chapUsers')
        resp = self.createTestChapUser(username=CHAP_NAME_1,
                                                     password=CHAP_PASSWORD,
                                                     description="created by testcase"
                                                     )
        resp =nimosclientBase.getNimosClient().chap_users.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        #self.printfooter('test_get_chapUsers')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_chapUser(self):
                
        #self.printheader('test_create_chapUser')
      
        resp = self.createTestChapUser(username=CHAP_NAME_1,
                                                     password=CHAP_PASSWORD,
                                                     description="created by testcase"
                                                     )
        self.assertIsNotNone(resp) 
        self.assertEqual(resp.attrs.get("name"),CHAP_NAME_1)
        self.assertEqual(resp.attrs.get("description"),"created by testcase")
                             
        #self.printfooter('test_create_chapUser')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_chapUser_using_invalid_password(self):
                        
        #self.printheader('test_create_chapUser_using_invalid_password')
        try:
            resp = self.createTestChapUser(username=CHAP_NAME_1,
                                                        password="sadhs",
                                                        description="created by testcase"
                                                        )
            self.assertIsNotNone(resp) 
        except exceptions.NimOSAPIError as ex:
          if "SM_invalid_arg_value" in str(ex):
              print("Failed as expected. Password length short")
          else:
              print(ex)      
        #self.printfooter('test_create_chapUser_using_invalid_password')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_delete_InvalidchapUser(self):
                
        #self.printheader('test_delete_chapUser')      
        resp = self.createTestChapUser(username=CHAP_NAME_1,
                                                     password=CHAP_PASSWORD,
                                                     description="created by testcase"
                                                     )
        self.assertIsNotNone(resp) 
        self.assertEqual(resp.attrs.get("name"),CHAP_NAME_1)
        self.assertEqual(resp.attrs.get("description"),"created by testcase")
        
        try:
            resp=nimosclientBase.getNimosClient().chap_users.delete(id="213812497124712041adhjasjdgjahsdaskdk")
        except exceptions.NimOSAPIError as ex:
            if"SM_invalid_path_variable" in str(ex):
                print("Failed as expected. Invalid Id to delete")
            else:
                print(ex)                             
        #self.printfooter('test_delete_chapUser')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_update_chapUser(self):
                
        #self.printheader('test_update_chapUser')
       
        resp = self.createTestChapUser(username=CHAP_NAME_1,
                                                     password=CHAP_PASSWORD,
                                                     description="created by testcase"
                                                     )
        self.assertIsNotNone(resp) 
        self.assertEqual(resp.attrs.get("name"),CHAP_NAME_1)
        self.assertEqual(resp.attrs.get("description"),"created by testcase")
        
        #update few fields
        updateresp =nimosclientBase.getNimosClient().chap_users.update(id=resp.attrs.get("id"),
                                                           description="modified by testcase",                                                           
                                                           name="updatechapusertestcase")
        self.assertIsNotNone(updateresp) 
        self.assertEqual(updateresp.attrs.get("name"),"updatechapusertestcase")
        self.assertEqual(updateresp.attrs.get("description"),"modified by testcase")        
        #self.printfooter('test_update_folders')
        

          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
