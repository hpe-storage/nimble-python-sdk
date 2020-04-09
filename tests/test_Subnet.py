# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest
import logging

nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

import tests.NimbleClientbase as nimosclientBase
from tests.NimbleClientbase import SKIPTEST
from nimbleclient.v1 import exceptions

# below code is needed for debugging.
if __debug__ == True:
    from nimbleclient.v1 import client


class SubnetTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''SubnetTestCase class test the subnet object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for SubnetTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(SubnetTestCase, self).tearDown()
        self.printFooter(self.id())  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_subnetDetails(self):
                
        #self.printheader('test_get_subnetDetails')
        #sdk bug. why is subnet object having functions like create,update delete??? the rest doc does not have these. only read is allowed
        resp = nimosclientBase.getNimosClient().subnets.get()
        self.assertIsNotNone(resp)
        #doc shows it has 13 properties.but in replication setup it is 15.just check the length
        self.assertGreaterEqual(resp.attrs.__len__(),13)
        #self.printfooter('test_get_subnetDetails')
          

def main(out = sys.stdout, verbosity = 2):
    loader = unittest.TestLoader()
    sys.stderr = out
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)

    
  #  main(nimosclientBase.getUnittestlogfile())
    
