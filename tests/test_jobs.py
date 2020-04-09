# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest
import threading
import time

#import test_NimosClientUser
nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

import tests.NimbleClientbase as nimosclientBase
from tests.NimbleClientbase import SKIPTEST
from nimbleclient.v1 import exceptions
# below code is needed for debugging.
if __debug__ == True:
    from nimbleclient.v1 import client

#global variables


class JobsTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''JobsTestCase class test the Jobs object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for JobsTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(JobsTestCase, self).tearDown()
        self.printFooter(self.id())
        
        
    def starttempjob(self):        
        resp = nimosclientBase.getNimosClient().software_versions.get()
        self.assertIsNotNone(resp)
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_jobs(self):
                
        #self.printheader('test_get_jobs')
        #start an autosupport job and then call job to check for the sattus
        autosupportthread=threading.Thread(target=self.starttempjob)
        autosupportthread.start()
        time.sleep(4)        
        resp = nimosclientBase.getNimosClient().jobs.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)
        autosupportthread.join()        
        #self.printfooter('test_get_jobs')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)

