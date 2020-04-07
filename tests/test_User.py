# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest
# need this path to search modules when debugging from editor
nimosClientPackagePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..\\")
sys.path.append(nimosClientPackagePath)

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

USER_NAME1 = "TestCaseUser"
#VOLCOLL_NAME2 = nimosclientBase.getUniqueString("UnitTestcase-Vol2")
user_to_delete = []


class ClienttUserTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ClienttUserTestCase class test the User object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for ClienttUserTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(ClienttUserTestCase, self).tearDown()        
        self.deleteUser()        
    
 
    def deleteUser(self):
        for userId in user_to_delete:
            try:
                resp = nimosclientBase.getNimosClient().users.delete(id=userId)
                self.assertIsNotNone(resp)
            except exceptions.NimOSAPIError as ex:
                print(ex)
        user_to_delete.clear()
       
            
    def createTestUser(self,userName,**kwargs):
        resp = nimosclientBase.getNimosClient().users.create(name=userName,**kwargs)
        user_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp       
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createUsername_with_unsupportedChar(self):
                
        self.printHeader('test_createUsername_with_unsupportedChar')
        #Invalid char present in username.
        try:
            username = USER_NAME1
            self.createTestUser(username,password="password-91")
        except exceptions.NimOSAPIError:
            print(f"Failed as expected. invalid username : {username}")
            #print(ex)
        self.printFooter('test_createUsername_with_unsupportedChar')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createUsername_with_morethan_allowedcharacters(self):
                
        self.printHeader('test_createUsername_with_morethan_allowedcharacters')
         #only 32 char is allowed for username.
        try:
            username = USER_NAME1+USER_NAME1+USER_NAME1+USER_NAME1+USER_NAME1+USER_NAME1+USER_NAME1+USER_NAME1
            self.createTestUser(username,password="password-91")
        except exceptions.NimOSAPIError :
            print(f"Failed as expected. invalid username : {username}")
            #print(ex)
        self.printFooter('test_createUsername_with_morethan_allowedcharacters')
        
             
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createUserName_with_validDetails(self):
                
        self.printHeader('test_createUserName_with_validDetails')
         #only 32 char is allowed for username.
        try:
            username = USER_NAME1
            resp = self.createTestUser(username,password="password-91",full_name="alok ranjan",role="administrator",disabled=True)
            
            #check the role
            self.assertEqual(resp.attrs.get("role"),"administrator")
            #change the role to guest
            resp = nimosclientBase.getNimosClient().users.update(resp.attrs.get("id"),role="guest")
            self.assertEqual(resp.attrs.get("role"),"guest")
        except exceptions.NimOSAPIError :
            print(f"Failed as expected. invalid username : {username}")
            #print(ex)
        self.printFooter('test_createUserName_with_validDetails')  
        
    
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_userPassword_length(self):
                
        self.printHeader('test_userPassword_length')
         #only 32 char is allowed for username.
        try:
            username = USER_NAME1
            password = "pass91*"#minimum length should be 8 excluding & and [];'
            self.createTestUser(username,password=password,full_name="alok ranjan",role="administrator",disabled=True)
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. invalid password : {password}")
            else:
                print(ex)        
        self.printFooter('test_userPassword_length')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_userPassword_invalidcharacter(self):
           #check with invalid char in password       
        self.printHeader('test_userPassword_invalidcharacter')
         #only 32 char is allowed for username.
        try:
            username = USER_NAME1
            password = "pass91*asda&"#minimum length should be 8 excluding & and [];'
            self.createTestUser(username,password=password,full_name="alok ranjan",role="administrator",disabled=True)
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. invalid password : {password}")
            else:
                print(ex)        
        self.printFooter('test_userPassword_invalidcharacter')
        
        
          

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
