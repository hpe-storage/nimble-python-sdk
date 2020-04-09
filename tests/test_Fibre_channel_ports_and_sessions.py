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


class FCTestCases(nimosclientBase.NimosClientbaseTestCase):
    '''FCTestCases class test the fibre channel functionality. It covers ports,Session,Initiator_aliases and Interface object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for FCTestCases *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(FCTestCases, self).tearDown()
        self.printFooter(self.id())  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Ports(self):
                
        #self.printheader('test_get_FC_Ports')
        nimosclientBase.getNimosClient().fibre_channel_ports.get()                
        #self.printfooter('test_get_FC_Ports')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Sessions(self):
                
        #self.printheader('test_get_FC_Sessions')
        nimosclientBase.getNimosClient().fibre_channel_sessions.get()                
        #self.printfooter('test_get_FC_Sessions')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Interfaces(self):
                
        #self.printheader('test_get_FC_Interfaces')
        nimosclientBase.getNimosClient().fibre_channel_interfaces.get()                
        #self.printfooter('test_get_FC_Interfaces')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Initiators_aliases(self):
                
        #self.printheader('test_get_FC_Initiators_aliases')
        nimosclientBase.getNimosClient().fibre_channel_initiator_aliases.get()                
        #self.printfooter('test_get_FC_Initiators_aliases')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
