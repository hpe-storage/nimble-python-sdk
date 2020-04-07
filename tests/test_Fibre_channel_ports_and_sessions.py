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




class FCTestCases(nimosclientBase.NimosClientbaseTestCase):
    '''FCTestCases class test the fibre channel functionality. It covers ports,Session,Initiator_aliases and Interface object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for FCTestCases *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(FCTestCases, self).tearDown()  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Ports(self):
                
        self.printHeader('test_get_FC_Ports')
        nimosclientBase.getNimosClient().fibre_channel_ports.get()                
        self.printFooter('test_get_FC_Ports')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Sessions(self):
                
        self.printHeader('test_get_FC_Sessions')
        nimosclientBase.getNimosClient().fibre_channel_sessions.get()                
        self.printFooter('test_get_FC_Sessions')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Interfaces(self):
                
        self.printHeader('test_get_FC_Interfaces')
        nimosclientBase.getNimosClient().fibre_channel_interfaces.get()                
        self.printFooter('test_get_FC_Interfaces')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Initiators_aliases(self):
                
        self.printHeader('test_get_FC_Initiators_aliases')
        nimosclientBase.getNimosClient().fibre_channel_initiator_aliases.get()                
        self.printFooter('test_get_FC_Initiators_aliases')
          

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
