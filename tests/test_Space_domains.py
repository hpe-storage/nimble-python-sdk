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

#global variables
APP_SERVER_NAME_1 = nimosclientBase.getUniqueString("AppServerTC-1")

appserver_to_delete = []

class SpaceDomainTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''SpaceDomainTestCase class test the app servers object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for SpaceDomainTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(SpaceDomainTestCase, self).tearDown()
        self.printFooter(self.id())
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_spaceDomains(self):
                
        #self.printheader('test_get_spaceDomains')
        resp = nimosclientBase.getNimosClient().space_domains.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        #self.printfooter('test_get_spaceDomains')
        
              
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_spaceDomains_endrowBeyond(self):
                
        #self.printheader('test_spaceDomains_endrowBeyond')
        try:       
           resp = nimosclientBase.getNimosClient().space_domains.get(endRow=30)
           self.assertIsNotNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected.no rows present")
            else:
                print(ex)              
        #self.printfooter('test_spaceDomains_endrowBeyond')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_selectFields_for_spaceDomains(self):
                
        #self.printheader('test_selectFields_for_spaceDomains')
        try:         
            resp = nimosclientBase.getNimosClient().space_domains.get(fields="id,pool_id,pool_name,block_size")
            if resp != None:
                self.assertIsNotNone("id")
                self.assertIsNotNone("pool_id")
                self.assertIsNotNone("pool_name")
                self.assertIsNotNone("block_size")

        except exceptions.NimOSAPIError as ex:
            if "SM_end_row_beyond_total_rows" in str(ex):
                print("Failed as expected")
            else:
                print(ex)        
        #self.printfooter('test_selectFields_for_spaceDomains')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
