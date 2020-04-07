# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
#
#
# @author alokranjan 

import sys
import os
import time
# need this path to search modules when debugging from editor
nimosClientPackagePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..\\")
sys.path.append(nimosClientPackagePath)

import unittest
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

#VOL_NAME_PREFIX_COUNTER=1
VOL_NAME1 = nimosclientBase.getUniqueString("VolumeTC-Vol1")
time.sleep(.05)
VOL_NAME2 = nimosclientBase.getUniqueString("VolumeTC-Vol2")
time.sleep(.05)
VOL_NAME3 = nimosclientBase.getUniqueString("VolumeTC-Vol3")
vol_to_delete = []
deleteVolumeCounter = 5 # we will try to deletevolume  at max 5 times 

class VolumeTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''VolumeTestCase class test the volume object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for VolumeTestCase *****")
    
    def __init__(self, x):
            super().__init__(x)
            
            
    @classmethod
    def setUpClass(cls):
        #due to bulk_move operation most of the times when abort is issued. the array ignores the 
        #request to delete the volume as the operation is already in progress and hence teh volumes are left over.
        #hence, every time this test is run ,we will try to remove the old entries        
        global deleteVolumeCounter
        volresp = nimosclientBase.getNimosClient().volumes.list()
        #try:
        for volobj in volresp:
            while  deleteVolumeCounter != 0:
                try:
                    if (str.startswith(volobj.attrs.get("name"),"VolumeTC-Vol")) or (str.startswith(volobj.attrs.get("name"),"clone-VolumeTC")) == True:
                        volname=volobj.attrs.get("name")
                        nimosclientBase.getNimosClient().volumes.offline(volobj.attrs.get("id"))
                        nimosclientBase.getNimosClient().volumes.delete(volobj.attrs.get("id"))
                        print(f"Deleted volume '{volname}'") 
                        time.sleep(2)
                    break # break from inner while loop
                except exceptions.NimOSAPIError as ex:
                    if ("SM_volmv_vol_einprog" in str(ex)) or ("SM_vol_connection_count_unavailable" in str(ex)):
                        print(f"'SM_volmv_vol_einprog' in progress. Trying to delete volume '{volname}' again after 3 minutes")
                        time.sleep(180)
                        deleteVolumeCounter = deleteVolumeCounter - 1                       
                    else:
                        break#from while loop
                except Exception as ex:
                    print(ex)         
                           


    def tearDown(self):
        global  VOL_NAME1,VOL_NAME2,VOL_NAME3         
        self.deleteVolume()
        # very last, tear down base class
        super(VolumeTestCase, self).tearDown()
        VOL_NAME1 = nimosclientBase.getUniqueString("VolumeTC-Vol1")
        time.sleep(0.5)
        VOL_NAME2 = nimosclientBase.getUniqueString("VolumeTC-Vol2")
        time.sleep(0.5)
        VOL_NAME3 = nimosclientBase.getUniqueString("VolumeTC-Vol3")
     
 
    def deleteVolume(self):
        for volId in vol_to_delete:
            try:
                # check               
                nimosclientBase.getNimosClient().volumes.offline(volId)
                nimosclientBase.getNimosClient().volumes.delete(volId)
            except Exception as ex:
                print(ex)
        vol_to_delete.clear()
        
            
    def CreateTestVolume(self,volName,size=50,read_only="false"):
        print(f"Creating volume with name {volName}")   
        resp = nimosclientBase.getNimosClient().volumes.create(volName, size=size,read_only=read_only)
        vol_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp
        
        
   
    # @nimosclientBase.NimosClientbaseTestCase.print_header_and_footer
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_CreateVolume(self):
            self.printHeader('CreateVolume')
            #print(VOL_NAME1)
            self.CreateTestVolume(VOL_NAME1)
            # check
            vol1 = nimosclientBase.getNimosClient().volumes.get(id=None, name=VOL_NAME1)
            self.assertIsNotNone(vol1)
            self.assertEqual(VOL_NAME1, vol1.attrs.get("name"))            
            self.printFooter('CreateVolume')
            

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_CreateVolume_AlreadyExists(self):
        self.printHeader('CreateVolume_AlreadyExists')       
        self.CreateTestVolume(VOL_NAME1)
        try:
            #now try creating the same volume again
           self.CreateTestVolume(VOL_NAME1)

        except exceptions.NimOSAPIError as ex:
                if 'SM_eexist' in str(ex):  # covered sm_eexist and sm_http_conflict
                    print(f"Failed As Expected")
                   # print(ex)
        except Exception as exgeneral:
                print(exgeneral)

        self.printFooter('CreateVolume_AlreadyExists')
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_create_volume_badParams(self):
        self.printHeader('create_volume_badParams')
        volName = VOL_NAME1 + "/,"  # , or / is not supported by nimble for creating vol name
        try:
           self.CreateTestVolume(volName)

        except exceptions.NimOSAPIError as ex:
            # protocol ex is sm_http_bad_request
            if 'SM_invalid_arg_value' in str(ex):
                print(f"Failed As Expected. Invalid volname to create: {volName}")
                #print(ex)

        self.printFooter('create_volume_badParams')
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_create_volume_Unexpected_arg(self):
        self.printHeader('create_volume_Unexpected_arg')
        try:
            # "invalidarg" is not a part of volume argument.
            nimosclientBase.getNimosClient().volumes.create(VOL_NAME1, size=50, invalidarg="testinvalidarg")
        except exceptions.NimOSAPIError as ex:
            # protocol ex is sm_http_bad_request
            if 'SM_unexpected_arg' in str(ex):
                print(f"Failed As Expected. Unexpected arg for volname : {VOL_NAME1}")
               # print(ex)

        self.printFooter('create_volume_Unexpected_arg')
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_get_VolumePageSize(self):
        self.printHeader('test_1_get_VolumePageSize')
        respvol = []
        #first atleast create few volume
        for i in range(0,5):
            volName = nimosclientBase.getUniqueString("VolumeTC-Vol1-" + str(i))
            resp = self.CreateTestVolume(volName)
            respvol.append(resp)        
        resp =  nimosclientBase.getNimosClient().volumes.list(detail=True,pageSize=2)       
        self.assertIsNotNone(resp) 
        self.assertEqual(resp.__len__(),2)           
        #self.assertEqual(resp[0].attrs.get("name"),respvol[0].attrs.get("name"))                
        self.printFooter('test_1_get_VolumePageSize')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_InvalidVolumePageSize(self):
        self.printHeader('test_1_InvalidVolumePageSize')
     
        #first atleast create few volume
        for i in range(0,6):
            volName = nimosclientBase.getUniqueString("VolumeTC-Vol1-" + str(i))
            self.CreateTestVolume(volName)           
        try :       
            resp =  nimosclientBase.getNimosClient().volumes.list(detail=True,pageSize=5000)
          
        except Exception as ex:
            if"SM_too_large_page_size" in str(ex):
                pass
            else:
                print(ex)                        
        self.printFooter('test_1_InvalidVolumePageSize')
        
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_create_volume_ReadOnly(self):
        self.printHeader('test_1_create_volume_ReadOnly')       
        # create a read only volume..the volume gets created as write only.
        # which  makes  sense. why would someone create a volume as read only.. but doc says we can..file a bug.
        self.CreateTestVolume(VOL_NAME1,50,"true")
        #check
        vol1 = nimosclientBase.getNimosClient().volumes.get(id=None, name=VOL_NAME1)
        self.assertIsNotNone(vol1)
        self.assertFalse(vol1.attrs.get("read_only"))        
        self.printFooter('test_1_create_volume_ReadOnly')
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_VolumeWithFewFields(self):
        self.printHeader('getVolumes')
        self.CreateTestVolume(VOL_NAME1)
        resp = nimosclientBase.getNimosClient().volumes.get()
        self.assertIsNotNone(resp)
        print(resp)
        self.printFooter('getvolumes')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_SelectedFieldsForAllVolumes(self):
        self.printHeader('test_2_get_SelectedFieldsForAllVolumes')
        #first atleast create few volume
        vol1 = self.CreateTestVolume(VOL_NAME1)
        self.CreateTestVolume(VOL_NAME2)        
        resp = nimosclientBase.getNimosClient().volumes.list(detail=True,fields="name,id,size")
        for obj in resp:
            #first match the volume name. there could be that there were volumes on the array than the ones we created
            #also, we will just check the attrs of one volume. if that works fine it will work for other
            if(vol1.attrs.get("name") == obj.attrs.get("name") ):
                self.assertEqual(obj.attrs.get("id"),vol1.attrs.get("id"))
                self.assertEqual(obj.attrs.get("size"),vol1.attrs.get("size"))
                #now check no other extra attributes were returned from server for this volume
                self.assertTrue(" ",obj.attrs.get("read_only"," ")) # try fetching some attribute
                
        self.printFooter('test_2_get_SelectedFieldsForAllVolumes')
        
        
    #below function will be implemented when sdk is ready for accepting filters
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_SelectFieldsForFilteredVolumes(self):
        self.printHeader('test_2_get_SelectFieldsForFilteredVolumes')
        #first atleast create few volume
        resp = self.CreateTestVolume(VOL_NAME1)        
        #get by name
        vol1 = nimosclientBase.getNimosClient().volumes.get(id=None,name=VOL_NAME1,fields="name,id,size") 
        self.assertIsNotNone(vol1)
        self.assertEqual(resp.attrs.get("id"), vol1.attrs.get("id"))
        self.assertEqual(resp.attrs.get("size"), vol1.attrs.get("size"))
        self.assertEqual(resp.attrs.get("name"), vol1.attrs.get("name"))
         #now check no other extra attributes were returned from server for this volume
        self.assertTrue(" ",resp.attrs.get("full_name"," ")) # try fetching some attribute
        self.printFooter('test_2_getSelectFieldsForFilteredVolumes')        
        

    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_Nonexistent_Volumes(self):
        self.printHeader('test_2_get_Nonexistent_Volumes')
        resp = nimosclientBase.getNimosClient().volumes.get(name="nonexistentvolume")
        self.assertIsNone(resp)
        self.printFooter('test_2_get_Nonexistent_Volumes')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_Sortby_asce_VolumeName(self):
        self.printHeader('test_2_get_Sortby_asce_VolumeName')
        volname1 = nimosclientBase.getUniqueString("VolumeTC-Vol-Vol1-z")
        volname2 = nimosclientBase.getUniqueString("VolumeTC-Vol-Vol1-a")
        self.CreateTestVolume(volname1)
        self.CreateTestVolume(volname2)
        resp = nimosclientBase.getNimosClient().volumes.list(detail=True,sortBy="name")#ascending
        #asert that the resp contains only 2 objects. if more than 2 objects that means the array has volumes 
        #which are not created by test. in that case just fail
        if resp.__len__() != 2 :
            print("Array has volumes which were not created by unit testcase. pls make sure array has no volume present before running the test")
        else:
        #after sorting, volname2 should be the first object and 2nd object should be volname1.
            self.assertEqual(volname2, resp[0].attrs.get("name"))
            self.assertEqual(volname1, resp[1].attrs.get("name"))        
        self.printFooter('test_2_get_Sortby_asce_VolumeName')
        
        
       
    #the belwo test actually also covers the message "SM_start_row_beyond_total_rows"  and "SM_start_row_beyond_end_rows"
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_Volume_StartRowBeyondEndRowVolume(self):
        self.printHeader('test_1_get_Volume_StartRowBeyondEndRowVolume')
        self.CreateTestVolume(VOL_NAME1)
        self.CreateTestVolume(VOL_NAME2)
        #try to read from startrow 7. total only 2 rows will be there and hence the resp should be none 
        try:           
            resp =  nimosclientBase.getNimosClient().volumes.get(startRow=50)
            self.assertIsNone(resp)
        except exceptions.NimOSAPIError as ex:
            if "SM_start_row_beyond_total_rows" in str(ex):
                pass    
            else:
                print(ex)
        self.printFooter('test_1_get_Volume_StartRowBeyondEndRowVolume')
        
        
        
    #the belwo test actually also covers the message "SM_start_row_beyond_total_rows"  == "SM_start_row_beyond_end_rows"
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_2_get_Volume_StartRowEqualsEndRowVolume(self):
        self.printHeader('test_2_get_Volume_StartRowEqualsEndRowVolume')
        self.CreateTestVolume(VOL_NAME1)
        self.CreateTestVolume(VOL_NAME2)
        #try to read from startrow 7. totalrows are only 2 rows will be there and hence the resp should be none 
        try:           
            resp =  nimosclientBase.getNimosClient().volumes.get(startRow=1,endRow=1)
            self.assertIsNone(resp)
        except exceptions.NimOSAPIError as ex:
            print(ex)    
        self.printFooter('test_2_get_Volume_StartRowEqualsEndRowVolume')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_3_update_VolumeSizeAttribute(self):
        self.printHeader('test_3_update_VolumeSizeAttribute')
        #first atleast create few volume
        resp = self.CreateTestVolume(VOL_NAME1)        
        #update the size to 100
        resp = nimosclientBase.getNimosClient().volumes.update(id=resp.attrs.get("id"),size=100)
        self.assertIsNotNone(resp)
        #check the size is updated correctly
        vol = nimosclientBase.getNimosClient().volumes.get(id=resp.attrs.get("id"),fields="name,id,size")
        self.assertEqual(resp.attrs.get("size"), vol.attrs.get("size"))
        self.printFooter('test_3_update_VolumeSizeAttribute')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_3_update_VolumeMetadataWithInvalidKeyPair(self):
        self.printHeader('test_3_update_VolumeMetadataWithInvalidKeyPair')
        #first atleast create few volume
        respvol1 = self.CreateTestVolume(VOL_NAME1)
        self.CreateTestVolume(VOL_NAME2)
        metadata = {
            "key1" : "abcde",
            "key2" : "xyz"
        }
        try:                
            #update the size to 100
            nimosclientBase.getNimosClient().volumes.update(id=respvol1.attrs.get("id"),metadata=metadata)
        except exceptions.NimOSAPIError as ex:
            if 'SM_invalid_keyvalue' in str(ex):  # covered sm_eexist and sm_http_conflict
                    print(f"Failed As Expected")
        self.printFooter('test_3_updatest_VolumeMetadataWithInvalidKeyPair')
        
        
     #as of now the below will always fail as no way to provide correct metadata   
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_3_update_VolumeMetadata(self):
        self.printHeader('test_3_update_VolumeMetadata')
        #first atleast create few volume
        respvol1 = self.CreateTestVolume(VOL_NAME1)
        self.CreateTestVolume(VOL_NAME2)
        metadata = {
            'key1' : 'abcde'
            #"key2" : "xyz'
        }
        try:                
            #update the size to 100
            nimosclientBase.getNimosClient().volumes.update(id=respvol1.attrs.get("id"),metadata=metadata)
        except exceptions.NimOSAPIError as ex:
            if 'SM_invalid_keyvalue' in str(ex):  # covered sm_eexist and sm_http_conflict
                    print(f"Failed As Expected")
        self.printFooter('test_3_update_VolumeMetadata')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_3_update_resizeVolumeForce(self):
        # Shrinking an online volume is an operation which will fail unless force=true is specified.
        # This tests the forceUpdateObject functionality.        
        self.printHeader('test_3_update_resizeVolumeForce')
        #first atleast create few volume
        resp = self.CreateTestVolume(VOL_NAME1)
        self.assertIsNotNone(resp)
        self.assertEqual(resp.attrs.get("size"), 50)
        #assert that the volume is online
        self.assertEqual(1,resp.attrs.get("online"),"Volume is not Online")        
        try:                
            #update the size to 100
            resp = nimosclientBase.getNimosClient().volumes.update(id=resp.attrs.get("id"),size=5)
        except exceptions.NimOSAPIError as ex:
            if 'SM_vol_size_decreased' in str(ex):  # covered sm_http_conflict                   
                    self.assertIn("The operation will decrease the size of the volume. Use force option to proceed.",str(ex))                    
        #try with force option
        resp = nimosclientBase.getNimosClient().volumes.update(id=resp.attrs.get("id"),size=5,force=True)
        self.assertEqual(resp.attrs.get("size"), 5)
        self.printFooter('test_3_update_resizeVolumeForce')
        
        
 
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_create_cloneVolume(self):
        self.printHeader('test_1_create_cloneVolume')
        #first atleast create few volume
        CLONE_VOL_NAME = "test.VolumeClone.clone"
        respvol = self.CreateTestVolume(VOL_NAME1)
        snapresp = nimosclientBase.getNimosClient().snapshots.create(name="test.VolumeClone.snapshot",vol_id=respvol.attrs.get("id"))
        clonevolresp = nimosclientBase.getNimosClient().volumes.create(name=CLONE_VOL_NAME,base_snap_id=snapresp.attrs.get("id"),clone=True)
        #confirm
        self.assertEqual(CLONE_VOL_NAME,clonevolresp.attrs.get("name"))
        self.assertEqual(clonevolresp.attrs.get("size"),respvol.attrs.get("size"))
        
        #cleanup
        nimosclientBase.getNimosClient().volumes.offline(clonevolresp.attrs.get("id"))
        nimosclientBase.getNimosClient().volumes.delete(clonevolresp.attrs.get("id"))
       # self.deleteVolume(CLONE_VOL_NAME)        
        self.printFooter('test_1_create_cloneVolume')
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_1_delete_cloneVolume(self):
        self.printHeader('test_1_delete_cloneVolume')
        #first create  volume
        CLONE_VOL_NAME = nimosclientBase.getUniqueString("clone-VolumeTC")
        respvol = self.CreateTestVolume(VOL_NAME1)
        #clone a volume
        snapresp = nimosclientBase.getNimosClient().snapshots.create(name="test.VolumeClone.snapshot",vol_id=respvol.attrs.get("id"))
        clonevolresp = nimosclientBase.getNimosClient().volumes.create(name=CLONE_VOL_NAME,base_snap_id=snapresp.attrs.get("id"),clone=True)
        #confirm
        self.assertEqual(CLONE_VOL_NAME,clonevolresp.attrs.get("name"))
        self.assertEqual(clonevolresp.attrs.get("size"),respvol.attrs.get("size"))
        
        #try deleting parent volume . it should fail with exception "SM_vol_has_clone"
        try:
            self.deleteVolume()
        except exceptions.NimOSAPIError as ex:
            if "SM_vol_has_clone" in str(ex):
                print("Failed as expected")
                 #cleanup
                nimosclientBase.getNimosClient().volumes.offline(clonevolresp.attrs.get("id"))
                nimosclientBase.getNimosClient().volumes.delete(clonevolresp.attrs.get("id"))
            else:
                print(ex)
        self.printFooter('test_1_delete_cloneVolume')
    
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_bulk_move_Volume(self):
        self.printHeader('test_bulk_move_Volume')
        try:                      
            origVolPoolname=""
            #first atleast create few volume      
           # self.CreateTestVolume(VOL_NAME1)
            resp = self.CreateTestVolume(VOL_NAME3,size=5)
            origVolPoolname=resp.attrs.get("pool_name")
            #get the dest pool id.
            poolresp=nimosclientBase.getNimosClient().pools.list()
            self.assertIsNotNone(poolresp)
            #make sure we have 2 pools atleaset
            self.assertGreaterEqual(poolresp.__len__(),2)
            #get the pool id where to move the volume
            for poolobj in poolresp:
                if poolobj.attrs.get("name") == origVolPoolname:
                    continue
                else:
                    break
            pool_id=poolobj.attrs.get("id")
            #move the volumes
            moveresp=nimosclientBase.getNimosClient().volumes.bulk_move(dest_pool_id=pool_id,
                                                                        vol_ids=vol_to_delete)
            self.assertIsNotNone(moveresp)
            #abort the move now
            for volID in vol_to_delete:
                abortresp=nimosclientBase.getNimosClient().volumes.abort_move(volID)
                self.assertIsNotNone(abortresp)
        except exceptions.NimOSAPIError as ex:
            if "SM_vol_connection_count_unavailable" in str(ex) or "SM_vol_usage_unavailable" in str(ex):
                print("Failed to abort volume move due to service inavailiability")
            elif "SM_invalid_arg_value" in str(ex):
                print("Failed as expected. Invalid Pool id provided")
            else:
                print(ex)                
        self.printFooter("test_bulk_move_Volume")
        
        
     
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_move_Volume(self):
        self.printHeader('test_move_Volume')
        try:            
          
            #first atleast create volume
            self.CreateTestVolume(VOL_NAME3,size=5)
            #deliberately pass wrong pool id. move operation takes lot of time
            #hence we will just call the sdk api to make sure it takes all the arguments
            # 
            moveresp=nimosclientBase.getNimosClient().volumes.move(dest_pool_id="kasdkashdqwkdhkas286623787213612000ef",
                                                                        id=vol_to_delete[0])
            self.assertIsNotNone(moveresp)
            #abort the move now
            for volID in vol_to_delete:
                abortresp=nimosclientBase.getNimosClient().volumes.abort_move(volID)
                self.assertIsNotNone(abortresp)
        except exceptions.NimOSAPIError as ex:
            if ("SM_vol_connection_count_unavailable" in str(ex)) or ("SM_vol_usage_unavailable" in str(ex)):
                print("Failed to abort volume move due to service inavailiability")
            elif "SM_invalid_arg_value" in str(ex):
                print("Failed as expected. Invalid Pool id provided")
            else:
                print(ex)                 
        self.printFooter("test_move_Volume")
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_Bulk_set_dedupe(self):
        self.printHeader('test_Bulk_set_dedupe')
        try: 
            #first atleast create volume
            self.CreateTestVolume(VOL_NAME3,size=5)
            dedupresp=nimosclientBase.getNimosClient().volumes.bulk_set_dedupe(dedupe_enabled=True,vol_ids=vol_to_delete)
            self.assertIsNotNone(dedupresp)
        except exceptions.NimOSAPIError as ex:
            if "SM_pool_dedupe_incapable" in str(ex) :
                print("Failed as expected. Pool is not capable of hosting dedup volumes")
            else:
                print(ex)                 
        self.printFooter("test_Bulk_set_dedupe")
        
    
     
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

#if you want to run just one function then comment the else part of this code
# and from cmd line run "python -m unittest test_NimosClientVolume.VolumeTestCase.test_1_CreateVolume"
# if __name__ == "__main__":
#     try:
#         unittest.main()
#     except Exception as ex:
#         pass
# else:
#     suite = unittest.TestLoader().loadTestsFromTestCase(VolumeTestCase)
#     unittest.TextTestRunner(verbosity=2).run(suite)
