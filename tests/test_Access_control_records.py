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
VOL_NAME1 = nimosclientBase.getUniqueString("VolumeTC-Vol1")
INITIATOR_GRP_NAME1 = nimosclientBase.getUniqueString("IGrpTC-IG1")

#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))



class ACLTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''ACLTestCase class test the ACL object functionality '''
  
    print("**** Running Tests for ACLTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(ACLTestCase, self).tearDown()  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createAndDeleteAcl(self):
                
        self.printHeader('test_createAndDeleteAcl') 
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
        self.printFooter('test_createAndDeleteAcl')
          

def main(out = sys.stdout, verbosity = 2): 
    loader = unittest.TestLoader() 
  
    suite = loader.loadTestsFromModule(sys.modules[__name__]) 
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':
        print("from main ")
             
        if nimosclientBase.CONSOLELOG == False:
            #means the test was run using python -m 
            main(nimosclientBase.getUnittestlogfile())
        else:
            unittest.main()
else:   
    #means the test was run using python -m
    main(nimosclientBase.getUnittestlogfile())
