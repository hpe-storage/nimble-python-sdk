# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest

#import test_NimosClientUser
nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

import tests.NimbleClientbase as nimosclientBase
from tests.NimbleClientbase import SKIPTEST
from nimbleclient.v1 import exceptions
# below code is needed for debugging.
if __debug__ == True:
    from nimbleclient.v1 import client


class ControllerTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ControllerTestCase class test the controller object functionality '''

    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for ControllerTestCase *****")
    
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(ControllerTestCase, self).tearDown()
        self.printFooter(self.id())         
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_controllers(self):                
        #self.printheader('test_get_controllers')
        resp = nimosclientBase.getNimosClient().controllers.get()
        self.assertIsNotNone(resp)        
        #self.printfooter('test_get_controllers')        
     
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_controllers_endrowBeyond(self):
                
        #self.printheader('test_controllers_endrowBeyond')
        try:       
           resp = nimosclientBase.getNimosClient().controllers.list(endRow=30)
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected.no rows present")
            else:
                print(ex)              
        #self.printfooter('test_controllers_endrowBeyond')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_selectFields_for_controllers(self):
                
        #self.printheader('test_selectFields_for_controllers')
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
        #self.printfooter('test_selectFields_for_controllers')
        
        
          

# def main(out = sys.stdout, verbosity = 2): 
#     loader = unittest.TestLoader() 
  
#     suite = loader.loadTestsFromModule(sys.modules[__name__]) 
#     unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)

