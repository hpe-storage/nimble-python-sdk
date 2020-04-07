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

#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))




class SubnetTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''SubnetTestCase class test the subnet object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for SubnetTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(SubnetTestCase, self).tearDown()  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_subnetDetails(self):
                
        self.printHeader('test_get_subnetDetails')
        #sdk bug. why is subnet object having functions like create,update delete??? the rest doc does not have these. only read is allowed
        resp = nimosclientBase.getNimosClient().subnets.get()
        self.assertIsNotNone(resp)
        #doc shows it has 13 properties.but in replication setup it is 15.just check the length
        self.assertGreaterEqual(resp.attrs.__len__(),13)
        self.printFooter('test_get_subnetDetails')
          

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
