# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest

#import test_NimosClientUser
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

    

class ControllerTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ControllerTestCase class test the controller object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for ControllerTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(ControllerTestCase, self).tearDown() 
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_controllers(self):
                
        self.printHeader('test_get_controllers')
        resp = nimosclientBase.getNimosClient().controllers.get()
        self.assertIsNotNone(resp)        
        self.printFooter('test_get_controllers')        
     
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_controllers_endrowBeyond(self):
                
        self.printHeader('test_controllers_endrowBeyond')
        try:       
           resp = nimosclientBase.getNimosClient().controllers.list(endRow=30)
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected.no rows present")
            else:
                print(ex)              
        self.printFooter('test_controllers_endrowBeyond')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_selectFields_for_controllers(self):
                
        self.printHeader('test_selectFields_for_controllers')
        try:           
            resp = nimosclientBase.getNimosClient().controllers.get(fields="name,hostname")
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
        self.printFooter('test_selectFields_for_controllers')
        
        
          

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

