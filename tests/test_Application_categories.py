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


class AppCategoryTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''AppCategoryTestCase class test the app category object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for AppCategoryTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(AppCategoryTestCase, self).tearDown()
        self.printFooter(self.id())  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_appcategoryDetails(self):
                
        #self.printheader('test_get_appcategoryDetails')       
        resp = nimosclientBase.getNimosClient().application_categories.list()
        self.assertIsNotNone(resp)
        #atleast 10 default app category are there
        self.assertGreaterEqual(resp.__len__(),10)           
        #self.printfooter('test_get_appcategoryDetails')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
    
