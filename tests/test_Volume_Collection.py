# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 
 
import sys
import os
import unittest

# need this path to search modules when debugging from editor
nimosClientPackagePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..\\")
sys.path.append(nimosClientPackagePath)

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

VOLCOLL_NAME1 = nimosclientBase.getUniqueString("VolcollTC-VolColl1")
volcoll_to_delete = []
vol_to_delete = []


class VolumeCollectionTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''VolumeCollectionTestCase class test the volumeCollection object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for VolumeCollectionTestCase *****")
  
    def __init__(self, x):
            super().__init__(x)           

    def tearDown(self):
        # very last, tear down base class
        super(VolumeCollectionTestCase, self).tearDown()        
        self.deleteVolume()
        self.deleteVolColl()
        
    
    def deleteVolume(self):
       #first disassciate volume and then delte the volume and volcoll
        for volid in vol_to_delete:
             nimosclientBase.getNimosClient().volumes.update(id=volid,volcoll_id="")
             nimosclientBase.getNimosClient().volumes.offline(id=volid)
             nimosclientBase.getNimosClient().volumes.delete(volid)
        vol_to_delete.clear()
        
    def deleteVolColl(self):
        for volCollId in volcoll_to_delete:
            try:
                resp = nimosclientBase.getNimosClient().volume_collections.delete(id=volCollId)
                self.assertIsNotNone(resp)
            except exceptions.NimOSAPIError as ex:
                print(ex)
        volcoll_to_delete.clear() 
       
            
    def createTestVolColl(self,volCollName):
        resp = nimosclientBase.getNimosClient().volume_collections.create(name=volCollName,description="created by testcase")
        volcoll_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp      
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_VolColl(self):
                
        self.printHeader('test_1_create_VolColl')
        resp = self.createTestVolColl(VOLCOLL_NAME1)
        self.assertIsNotNone(resp)
        self.assertEqual(VOLCOLL_NAME1,resp.attrs.get("name"))
        self.assertEqual("created by testcase",resp.attrs.get("description"))
        
        #change the description and test it works
        resp = nimosclientBase.getNimosClient().volume_collections.update(resp.attrs.get("id"),description="modified by testcase")
        self.assertIsNotNone(resp)
        self.assertEqual("modified by testcase",resp.attrs.get("description"))
        
        self.printFooter('test_1_create_VolColl')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_addVolumeToVolColl(self):
                
        self.printHeader('test_addVolumeToVolColl')
        volcollresp = self.createTestVolColl(VOLCOLL_NAME1)
        volumeName= nimosclientBase.getUniqueString("VolumeCollectionTestCase-addtovolcoll")
        
        volresp = nimosclientBase.getNimosClient().volumes.create(volumeName, size=50)
        vol_to_delete.append(volresp.attrs.get("id"))
        self.assertIsNotNone(volcollresp)
        
        #associate the volume to volcoll
        volassociateresp = nimosclientBase.getNimosClient().volumes.associate(id=volresp.attrs.get("id"),volcoll=volcollresp)
        self.assertIsNotNone(volresp)
        #check
        self.assertEqual(volassociateresp.get("volcoll_name"),VOLCOLL_NAME1)
        self.assertEqual(volassociateresp.get("volcoll_id"),volcollresp.attrs.get("id"))
        #disassociate
        nimosclientBase.getNimosClient().volumes.dissociate(id=volresp.attrs.get("id"))
        #get vol coll and confirm has no volumes
        volcollresp = nimosclientBase.getNimosClient().volume_collections.get(id=volcollresp.attrs.get("id"))
        self.assertEqual(volcollresp.attrs.get("volume_count"),0)
        self.printFooter('test_addVolumeToVolColl')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_delete_VolCollBeforeDisassociatingVolume(self):
                
        self.printHeader('test_delete_VolCollBeforeDisassociatingVolume')
        volcollresp = self.createTestVolColl(VOLCOLL_NAME1)
        volumeName= nimosclientBase.getUniqueString("VolumeCollectionTestCase-addtovolcoll")
        
        volresp = nimosclientBase.getNimosClient().volumes.create(volumeName, size=50)
        vol_to_delete.append(volresp.attrs.get("id"))
        self.assertIsNotNone(volcollresp)
        
        #associate the volume to volcoll
        volassociateresp = nimosclientBase.getNimosClient().volumes.associate(id=volresp.attrs.get("id"),volcoll=volcollresp)
        self.assertIsNotNone(volresp)
        #check
        self.assertEqual(volassociateresp.get("volcoll_name"),VOLCOLL_NAME1)
        self.assertEqual(volassociateresp.get("volcoll_id"),volcollresp.attrs.get("id"))
        #try deleting the volcoll . this should fail as volume has not been disassocited
        try:
            resp = nimosclientBase.getNimosClient().volume_collections.delete(id=volcollresp.attrs.get("id"))
        except exceptions.NimOSAPIError as ex:
            if"SM_ebusy" in str(ex):
                print("Failed as expected")
            else:
                raise ex
        self.printFooter('test_delete_VolCollBeforeDisassociatingVolume')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_Promote_VolColl(self):
                
        self.printHeader('test_Promote_VolColl')
        volcollresp = self.createTestVolColl(VOLCOLL_NAME1)
        volumeName= nimosclientBase.getUniqueString("VolumeCollectionTestCase-addtovolcoll")
        
        volresp = nimosclientBase.getNimosClient().volumes.create(volumeName, size=50)
        vol_to_delete.append(volresp.attrs.get("id"))
        self.assertIsNotNone(volcollresp)
        
        #associate the volume to volcoll
        volassociateresp = nimosclientBase.getNimosClient().volumes.associate(id=volresp.attrs.get("id"),volcoll=volcollresp)
        self.assertIsNotNone(volresp)
        #check
        self.assertEqual(volassociateresp.get("volcoll_name"),VOLCOLL_NAME1)
        self.assertEqual(volassociateresp.get("volcoll_id"),volcollresp.attrs.get("id"))
        #try deleting the volcoll . this should fail as volume has not been disassocited
        try:
            nimosclientBase.getNimosClient().volume_collections.promote(id=volcollresp.attrs.get("id"))
        except exceptions.NimOSAPIError as ex:
            if"SM_ealready" in str(ex):
                print("Failed as expected. volcoll is already promoted")
            else:
                print(ex)
        self.printFooter('test_Promote_VolColl')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_Demote_VolColl(self):
                
        self.printHeader('test_Demote_VolColl')
        volcollresp = self.createTestVolColl(VOLCOLL_NAME1)        
        self.assertIsNotNone(volcollresp)
        try:
            nimosclientBase.getNimosClient().volume_collections.demote(id=volcollresp.attrs.get("id"),replication_partner_id="1264126491231239123hgghsjhd")
        except exceptions.NimOSAPIError as ex:
            if"SM_invalid_arg_value" in str(ex):
                print("Failed as expected. Invalid value provided for replication_partner_id")
            else:
                print(ex)
        self.printFooter('test_Demote_VolColl')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_Handover_VolColl(self):
                
        self.printHeader('test_Handover_VolColl')
        volcollresp = self.createTestVolColl(VOLCOLL_NAME1)        
        self.assertIsNotNone(volcollresp)
        try:
            nimosclientBase.getNimosClient().volume_collections.handover(id=volcollresp.attrs.get("id"),replication_partner_id="1264126491231239123hgghsjhd")
        except exceptions.NimOSAPIError as ex:
            if"SM_invalid_arg_value" in str(ex):
                print("Failed as expected. Invalid value provided for replication_partner_id")
            else:
                print(ex)
        self.printFooter('test_Handover_VolColl')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_delete_VolumeInVolCollBeforeDisassociating(self):
                
        self.printHeader('test_delete_VolumeInVolCollBeforeDisassociating')
        volcollresp = self.createTestVolColl(VOLCOLL_NAME1)
        volumeName= nimosclientBase.getUniqueString("VolumeCollectionTestCase-addtovolcoll")
        
        volresp = nimosclientBase.getNimosClient().volumes.create(volumeName, size=50)
        vol_to_delete.append(volresp.attrs.get("id"))
        self.assertIsNotNone(volcollresp)
        
        #associate the volume to volcoll
        volassociateresp = nimosclientBase.getNimosClient().volumes.associate(id=volresp.attrs.get("id"),volcoll=volcollresp)
        self.assertIsNotNone(volresp)
        #check
        self.assertEqual(volassociateresp.get("volcoll_name"),VOLCOLL_NAME1)
        self.assertEqual(volassociateresp.get("volcoll_id"),volcollresp.attrs.get("id"))
        #try deleting the volcoll . this should fail as volume has not been disassocited
        try:
            nimosclientBase.getNimosClient().volumes.offline(id=volresp.attrs.get("id"))
            nimosclientBase.getNimosClient().volumes.delete(id=volresp.attrs.get("id"))
        except exceptions.NimOSAPIError as ex:
            if"SM_vol_assoc_volcoll" in str(ex):
                print("Failed as expected")             
            else:
                raise ex
        self.printFooter('test_delete_VolumeInVolCollBeforeDisassociating')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_createEditDeleteProtectionSchedule(self):
                
        self.printHeader('test_createEditDeleteProtectionSchedule')
        #check if this array has any previous volcoll
        volcollresp=nimosclientBase.getNimosClient().volume_collections.list()
        totalvolcoll = volcollresp.__len__()
        
        PROTECTION_SCHED_NAME = "testcaseprotectionschedule"
        days = "monday,tuesday,wednesday,thursday,friday"
        description = "super cool schedule"
        
        resp = self.createTestVolColl(VOLCOLL_NAME1)
        self.assertIsNotNone(resp)
        #create a protection schedule
        protect_sched_resp = nimosclientBase.getNimosClient().protection_schedules.create(name=PROTECTION_SCHED_NAME,days=days,description=description,
                                                                               volcoll_or_prottmpl_id=resp.attrs.get("id"),
                                                                               volcoll_or_prottmpl_type='volume_collection',
                                                                               num_retain=2)
        self.assertIsNotNone(protect_sched_resp)
        self.assertEqual(protect_sched_resp.attrs.get("days"),days)
        self.assertEqual(protect_sched_resp.attrs.get("description"),description)
        self.assertEqual(protect_sched_resp.attrs.get("name"),PROTECTION_SCHED_NAME)
        #check if volcoll is present
        volcollresp=nimosclientBase.getNimosClient().volume_collections.list()
        self.assertEqual(volcollresp.__len__(),totalvolcoll+1)        
        #update the schedule
        resp = nimosclientBase.getNimosClient().protection_schedules.update(id=protect_sched_resp.attrs.get("id"),period_unit="minutes")
        self.assertIsNotNone(resp)
        self.assertEqual("minutes",resp.attrs.get("period_unit"))
        #delete the schedule
        resp = nimosclientBase.getNimosClient().protection_schedules.delete(id=protect_sched_resp.attrs.get("id"))
        #check if volcoll has schedule
        volcollresp=nimosclientBase.getNimosClient().volume_collections.get()
        self.assertIsNone(volcollresp.attrs.get("schedule_list"))        
        self.printFooter('test_createEditDeleteProtectionSchedule')
        
    
          

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