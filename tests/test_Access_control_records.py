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
VOL_NAME1 = nimosclientBase.getUniqueString("VolumeTC-Vol1")
INITIATOR_GRP_NAME1 = nimosclientBase.getUniqueString("IGrpTC-IG1")
class ACLTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ACLTestCase class test the ACL object functionality '''
  
    print("**** Running Tests for ACLTestCase *****")

    def __init__(self, x):
                super().__init__(x)

    def setUp(self):
                self.printHeader(self.id())

    def tearDown(self):
        # very last, tear down base class
        super(ACLTestCase, self).tearDown()
        self.printFooter(self.id())  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createAndDeleteAcl(self):
                
        #self.printheader('test_createAndDeleteAcl') 
        try:            
            #first creat a volume.
            volresp= nimosclientBase.getNimosClient().volumes.create(name=VOL_NAME1,size=10)
            self.assertIsNotNone(volresp)
            #create an initiator group
            igresp= nimosclientBase.getNimosClient().initiator_groups.create(name=INITIATOR_GRP_NAME1,
                                                            description="created by testcase",
                                                            access_protocol="iscsi")
            self.assertIsNotNone(igresp)
            #create the ACL
            aclresp= nimosclientBase.getNimosClient().access_control_records.create(apply_to="both",
                                                                     initiator_group_id=igresp.attrs.get("id"),
                                                                     vol_id=volresp.attrs.get("id"))
            self.assertIsNotNone(aclresp)
            #assert that it has been applied
            self.assertEqual(aclresp.attrs.get("vol_id"),volresp.attrs.get("id"))
            self.assertEqual(aclresp.attrs.get("initiator_group_name"),igresp.attrs.get("name"))
            self.assertEqual(aclresp.attrs.get("apply_to"),"both")
            
            #cleanup
            aclresp= nimosclientBase.getNimosClient().access_control_records.delete(id=aclresp.attrs.get("id"))
            igresp= nimosclientBase.getNimosClient().initiator_groups.delete(id=igresp.attrs.get("id"))
            self.assertIsNotNone(igresp)
            volresp= nimosclientBase.getNimosClient().volumes.offline(id=volresp.attrs.get("id"))
            volresp= nimosclientBase.getNimosClient().volumes.delete(id=volresp.get("id"))
            self.assertIsNotNone(volresp)
            
        except exceptions.NimOSAPIError as ex:
            print(ex)          
        #self.printfooter('test_createAndDeleteAcl')
        
     
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    sys.stderr = out 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
     
if __name__ == '__main__':       
        unittest.main(module=sys.modules[__name__] , verbosity=2)
    
  #  main(nimosclientBase.getUnittestlogfile())
    #main(sl)
