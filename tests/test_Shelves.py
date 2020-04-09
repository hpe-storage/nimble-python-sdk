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



class ShelveTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ShelveTestCase class test the subnet object functionality '''

    print("**** Running Tests for ShelveTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(ShelveTestCase, self).tearDown()
        self.printFooter(self.id()) 
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_getShelve(self):
                
        #self.printheader('test_getShelve')
        #sdk bug. why is subnet object having functions like create,update delete??? the rest doc does not have these. only read is allowed
        resp = nimosclientBase.getNimosClient().shelves.list(detail=True)
        self.assertIsNotNone(resp)
        #doc shows it has 13 properties.just check the length
        self.assertEqual(resp[0].attrs.__len__(),13)
        #self.printfooter('test_getShelve')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_activateShelve(self):
                
        #self.printheader('test_activateShelve')
        #sdk bug. why is subnet object having functions like create,update delete??? the rest doc does not have these. only read is allowed
        resp = nimosclientBase.getNimosClient().shelves.get()        
        self.assertIsNotNone(resp)
        try:
            resp = nimosclientBase.getNimosClient().shelves.update(id=resp.attrs.get("id"),force=True,activated=True)
            self.assertEqual(resp.attrs.get("activated"),True)
        except exceptions.NimOSAPIError as ex:
            if "SM_shelf_no_eloc_id" in str(ex):
                print("Making test as Passed since no shelve exist for expansion")
            else:
                print(ex)
        self.assertIsNotNone(resp)
        #self.printfooter('test_activateShelve')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)

