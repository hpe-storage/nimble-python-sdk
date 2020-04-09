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




class SoftwareVersionsTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''SoftwareVersionsTestCase class test the software version object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for SoftwareVersionsTestCase *****")
    def __init__(self, x):
            super().__init__(x)
                
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(SoftwareVersionsTestCase, self).tearDown()  
        self.printFooter(self.id())
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_SoftwareVersionsDetails(self):
                
        #self.printheader('test_get_SoftwareVersionsDetails')
        resp = nimosclientBase.getNimosClient().software_versions.get()
        self.assertIsNotNone(resp)
        #self.printfooter('test_get_SoftwareVersionsDetails')
        
    

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
