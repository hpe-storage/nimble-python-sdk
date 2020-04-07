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
INITIATOR_GRP_NAME1 = nimosclientBase.getUniqueString("IGrpTC-IG1")
INITIATOR_GRP_NAME2 = nimosclientBase.getUniqueString("IGrpTC-IG2")
INITIATOR_NAME1 = nimosclientBase.getUniqueString("IGrpTC-Initiator1")

initiatorgrp_to_delete = []
initiator_to_delete = []

#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))



class InitiatorGroupsTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''InitiatorGroupsTestCase class test the Initiator and InitiatorGroup object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for InitiatorGroupsTestCase *****")
    def __init__(self, x):
            super().__init__(x)

                     

    def tearDown(self):
        # very last, tear down base class
        super(InitiatorGroupsTestCase, self).tearDown()
        self.deleteInitiatorGroup()        
        
    
    def createTestInitiatorGroup(self,initiatorgrpName,**kwargs):
        resp =nimosclientBase.getNimosClient().initiator_groups.create(name=initiatorgrpName,**kwargs)
        initiatorgrp_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp 
    
    
    def deleteInitiatorGroup(self):
        for igId in initiatorgrp_to_delete:              
               nimosclientBase.getNimosClient().initiator_groups.delete(igId)
        initiatorgrp_to_delete.clear()
            
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createAndDelete_InitiatorGroup(self):
                
        self.printHeader('test_createAndDelete_InitiatorGroup')        
        igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,
                                                access_protocol="iscsi",
                                                description="created by testcase"
                                                )
        #assert the values
        self.assertIsNotNone(igresp)
        self.assertEqual(igresp.attrs.get("description"),"created by testcase")
        self.assertEqual(igresp.attrs.get("id"),igresp.attrs.get("id"))
        self.assertEqual(igresp.attrs.get("access_protocol"),"iscsi")
        self.assertEqual(igresp.attrs.get("name"),INITIATOR_GRP_NAME1)
        
        self.printFooter('test_createAndDelete_InitiatorGroup')
        
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_check_mandatoryparams_InitiatorGroup(self):               
        self.printHeader('test_check_mandatoryparams_InitiatorGroup')
        try:
                    
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase"
                                                    )
            #assert the values
            self.assertIsNotNone(igresp)
            self.assertEqual(igresp.attrs.get("description"),"created by testcase")            
            self.assertEqual(igresp.attrs.get("name"),INITIATOR_GRP_NAME1)
        except exceptions.NimOSAPIError as ex:
            if "SM_missing_arg" in str(ex):
                print("Failed as expected. Missing mandatory param")
            else:
                print(ex)       
        self.printFooter('test_check_mandatoryparams_InitiatorGroup')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_InitiatorGroup_With_IncorrectAccessProtocol(self):               
        self.printHeader('test_create_InitiatorGroup_With_IncorrectAccessProtocol')
        try:
            access_protocol="not a valid param. should be FC or iscsi"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol
                                                    )
            #assert the values
            self.assertIsNotNone(igresp)
            self.assertEqual(igresp.attrs.get("id"),initiatorgrp_to_delete[0])
                       
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. Invalid param value {access_protocol}")
            else:
                print(ex)       
        self.printFooter('test_create_InitiatorGroup_With_IncorrectAccessProtocol')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_duplicate_Initiatorgroup(self):               
        self.printHeader('test_create_duplicate_Initiatorgroup')
        try:
            access_protocol="iscsi"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol
                                                    )
            
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol
                                                    )
            #assert the values
            self.assertIsNotNone(igresp)          
        except exceptions.NimOSAPIError as ex:
            if "SM_duplicate_initiatorgrp" in str(ex):
                print(f"Failed as expected. IG group already present on array {INITIATOR_GRP_NAME1}")
            else:
                print(ex)       
        self.printFooter('test_create_duplicate_Initiatorgroup')
                
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_InitiatorGroup_With_FCAccesssProtocol(self):               
        self.printHeader('test_create_InitiatorGroup_With_IncorrectAccessProtocol')
        try:
            access_protocol="fc"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol
                                                    )
            #assert the values
            self.assertIsNotNone(igresp)
            self.assertEqual(igresp.attrs.get("id"),initiatorgrp_to_delete[0])
                       
        except exceptions.NimOSAPIError as ex:
            if "SM_fc_svc_not_available" in str(ex):
                print(f"Failed as expected. FC service not available")
            else:
                print(ex)       
        self.printFooter('test_create_InitiatorGroup_With_IncorrectAccessProtocol')
        
        
    
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_InitiatorGroups(self):               
        self.printHeader('test_get_InitiatorGroups')
        try:
            access_protocol="iscsi" 
            iscsi_initiators= [
         {
            "label":"itor1",
            "ip_address":"1.1.1.1",
            "iqn":"iqn.1992-01.com.example:storage.tape1.sys1.xyz"
         }
      ]      
            igresp1 = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                    iscsi_initiators=iscsi_initiators
                                                    )
            self.assertIsNotNone(igresp1)
            self.assertEqual(igresp1.attrs.get("id"),initiatorgrp_to_delete[0])
            
            igresp2 = self.createTestInitiatorGroup(INITIATOR_GRP_NAME2,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                    iscsi_initiators=iscsi_initiators
                                                    )
            #assert the values
            self.assertIsNotNone(igresp2)
            self.assertEqual(igresp2.attrs.get("id"),initiatorgrp_to_delete[1])
            
            #get all the IG groups and check their initiator
            igrps =nimosclientBase.getNimosClient().initiator_groups.list(detail=True,pageSize=2)
            
            for igobj in igrps:
                if (igobj.attrs.get("name") == INITIATOR_GRP_NAME1) or  (igobj.attrs.get("name") == INITIATOR_GRP_NAME2):
                    self.assertIsNotNone(igobj.attrs.get("description"))
                    self.assertEqual(igobj.attrs.get("description"),"created by testcase")
                    self.assertIsNotNone(igobj.attrs.get("access_protocol"))
                    self.assertEqual(igobj.attrs.get("access_protocol"),"iscsi")
                    self.assertIsNotNone(igobj.attrs.get("iscsi_initiators"))
                       
        except exceptions.NimOSAPIError as ex:         
                print(ex)       
        self.printFooter('test_get_InitiatorGroups')
    
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_update_InitiatorGroup(self):                       
        self.printHeader('test_update_InitiatorGroup')        
  
        iscsi_initiators= [
         {
            "label":"itor1",
            "ip_address":"1.1.1.1",
            "iqn":"iqn.1992-01.com.example:storage.tape1.sys1.xyz"
         }
      ]
        description= "modified by testcase"
        try:
            access_protocol="iscsi"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                    )
            #assert the values
            self.assertIsNotNone(igresp)
            #update the target_subnet
            updateresp =nimosclientBase.getNimosClient().initiator_groups.update(id=igresp.attrs.get("id"),
                                                                   description=description,
                                                                   iscsi_initiators=iscsi_initiators)
            self.assertIsNotNone(updateresp)
                      
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. Invalid param value")
            else:
                print(ex)       
        self.printFooter('test_update_InitiatorGroup')
    

    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_InitiatorGroupNaming_Iscsi(self):                       
        self.printHeader('test_InitiatorGroupNaming_Iscsi')        
  
        iscsi_initiators1= [
         {
            "label":"initiator1",
            "ip_address":"10.1.1.1",
            "iqn":"iqn.1998-01.com.nimblestorage:intiator1"
         }
      ]
        
        iscsi_initiators2= [
         {
            "label":"initiator2",
            "ip_address":"10.1.1.2",
            "iqn":"iqn.1998-01.com.nimblestorage:intiator2"
         }
      ]
        
        iscsi_initiators3= [
         {
            "label":"initiator3",
            "ip_address":"10.1.1.3",
            "iqn":"iqn.1998-01.com.nimblestorage:intiator3"
         }
      ]        
       # description= "created by testcase"
        try:
            access_protocol="iscsi"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                     iscsi_initiators=iscsi_initiators1
                                                    )
            #assert the values
            self.assertIsNotNone(igresp)
            self.assertEqual(igresp.attrs.get("name"),INITIATOR_GRP_NAME1)
            
            #add one more initiator
            updateresp =nimosclientBase.getNimosClient().initiators.create(
                                                                    initiator_group_id=igresp.attrs.get("id"),                                                                   
                                                                    access_protocol=access_protocol,
                                                                    label="initiator2",
                                                                    iqn="iqn.1998-01.com.nimblestorage:intiator2",
                                                                    #ip_address = "10.1.1.2"
                                                                    
                                                                    )
            
            #assert the values
            self.assertIsNotNone(updateresp)
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME2,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                    iscsi_initiators=iscsi_initiators3
                                                    )
         
            self.assertIsNotNone(igresp)
            self.assertEqual(igresp.attrs.get("name"),INITIATOR_GRP_NAME2)
            count = 0
            #get all the initiators and check
            initiatorlist =nimosclientBase.getNimosClient().initiators.list(detail=True)
            for initiatorobj in initiatorlist:
                if (initiatorobj.attrs.get("label") == iscsi_initiators1[0]["label"]) or (initiatorobj.attrs.get("label") == iscsi_initiators2[0]["label"]) or (initiatorobj.attrs.get("label") == iscsi_initiators3[0]["label"]):
                    count+=1
            self.assertGreaterEqual(count,3)
                      
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. Invalid param value")
            else:
                print(ex)       
        self.printFooter('test_InitiatorGroupNaming_Iscsi')        
        
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_suggested_lun(self):                       
        self.printHeader('test_get_suggested_lun')        
  
        iscsi_initiators1= [
         {
            "label":"initiator1",
            "ip_address":"10.1.1.1",
            "iqn":"iqn.1998-01.com.nimblestorage:intiator1"
         }
      ]
         
       # description= "created by testcase"
        try:
            access_protocol="iscsi"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                     iscsi_initiators=iscsi_initiators1
                                                    )
            self.assertIsNotNone(igresp)
            suggest_lunresp =nimosclientBase.getNimosClient().initiator_groups.suggest_lun(id=igresp.attrs.get("id"))
            self.assertIsNotNone(suggest_lunresp)         
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. Invalid param value")
            else:
                print(ex)       
        self.printFooter('test_get_suggested_lun')        
        
        


    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_validate_lun(self):                       
        self.printHeader('test_validate_lun')        
  
        iscsi_initiators1= [
         {
            "label":"initiator1",
            "ip_address":"10.1.1.1",
            "iqn":"iqn.1998-01.com.nimblestorage:intiator1"
         }
      ]
         
       # description= "created by testcase"
        try:
            access_protocol="iscsi"       
            igresp = self.createTestInitiatorGroup(INITIATOR_GRP_NAME1,                                              
                                                    description="created by testcase",
                                                    access_protocol=access_protocol,
                                                     iscsi_initiators=iscsi_initiators1
                                                    )
            self.assertIsNotNone(igresp)
            validate_lunresp =nimosclientBase.getNimosClient().initiator_groups.validate_lun(id=igresp.attrs.get("id"),lun=0)
            self.assertIsNotNone(validate_lunresp)         
        except exceptions.NimOSAPIError as ex:
            if "SM_invalid_arg_value" in str(ex):
                print(f"Failed as expected. Invalid param value")
            else:
                print(ex)       
        self.printFooter('test_validate_lun')
               
        
          

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
