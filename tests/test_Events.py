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


class EventsTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''EventsTestCase class test the events object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for EventsTestCase *****")
    def __init__(self, x):
            super().__init__(x)
            
    def setUp(self):
            self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(EventsTestCase, self).tearDown()
        self.printFooter(self.id())  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_events(self):
                
        #self.printheader('test_get_events')
       
        resp = nimosclientBase.getNimosClient().events.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        #self.printfooter('test_get_events')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_eventlog_queryparams(self):
                
        #self.printheader('test_get_eventlog_queryparams')
       
        resp = nimosclientBase.getNimosClient().events.list(detail=True,
                                                      pageSize=2)
        self.assertIsNotNone(resp)        
        resp = nimosclientBase.getNimosClient().events.get(
                                                      pageSize=2,
                                                      fields="activity,id,category,severity") 
        self.assertIsNotNone(resp)
        #assert that those fields are present
        self.assertIsNotNone(resp.attrs.get("activity"))
        self.assertIsNotNone(resp.attrs.get("id"))
        self.assertIsNotNone(resp.attrs.get("category"))       
        self.assertIsNotNone(resp.attrs.get("severity"))
        
        #try asserting a value which was not querying
        self.assertIsNone(resp.attrs.get("startRow"))

        #self.printfooter('test_get_eventlog_queryparams')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_query_Invalid_params(self):
                
        #self.printheader('test_query_Invalid_params')       
        try:
            queryparam="junkparam"
            resp = nimosclientBase.getNimosClient().events.get(
                                                      pageSize=2,
                                                      fields=queryparam) 
            self.assertIsNotNone(resp)
            #assert that those fields are present
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_query_param" in str(ex):
                print(f"Failed as expected. Invalid query params provided to query '{queryparam}'")
            else:
                print(ex)
        #self.printfooter('test_query_Invalid_params')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
    
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
