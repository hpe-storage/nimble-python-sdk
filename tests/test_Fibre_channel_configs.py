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


class FCConfigTestCases(nimosclientBase.NimosClientbaseTestCase):
    '''FCConfigTestCases class test the fibre channel functionality. It covers ports,Session,Initiator_aliases and Interface object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for FCConfigTestCases *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(FCConfigTestCases, self).tearDown() 
        self.printFooter(self.id()) 
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_FC_Configs(self):
                
        #self.printheader('test_get_FC_Configs')
        nimosclientBase.getNimosClient().fibre_channel_configs.get()                
        #self.printfooter('test_get_FC_Configs')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_FCConfigs_endrowBeyond(self):
                
        #self.printheader('test_FCConfigs_endrowBeyond')
        try:       
           resp = nimosclientBase.getNimosClient().fibre_channel_configs.get(endRow=30)
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected.no rows present")
            else:
                print(ex)              
        #self.printfooter('test_FCConfigs_endrowBeyond')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_selectFields_for_FCConfigs(self):
                
        #self.printheader('test_selectFields_for_FCConfigs')
        try:         
            resp = nimosclientBase.getNimosClient().fibre_channel_configs.get(fields="id,group_leader_array")
            self.assertIsNotNone(resp)
            self.assertIsNotNone("id")
            self.assertIsNotNone("group_leader_array")         

        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected")
            else:
                print(ex)        
        #self.printfooter('test_selectFields_for_FCConfigs')
        
        
  
            

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)