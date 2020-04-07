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
FOLDERS_NAME_1 = nimosclientBase.getUniqueString("FolderTC-1")

folders_to_delete = []
#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))




class FoldersTestCase(nimosclientBase.NimosClientbaseTestCase):
    '''FoldersTestCase class test the folders object functionality '''
    
    #client = nimosclientBase.NimosClientbaseTestCase.getNimosClientObj()
    print("**** Running Tests for FoldersTestCase *****")
    def __init__(self, x):
            super().__init__(x)

    def tearDown(self):
        # very last, tear down base class
        super(FoldersTestCase, self).tearDown() 
        self.deleteTestFolders()
        
    
    def deleteTestFolders(self):
        for folderId in folders_to_delete:              
            nimosclientBase.getNimosClient().folders.delete(folderId)
        folders_to_delete.clear()
        
        
    def createTestFolders(self,foldername,**kwargs):
        resp = nimosclientBase.getNimosClient().folders.create(name=foldername,**kwargs)
        folders_to_delete.append(resp.attrs.get("id"))
        self.assertIsNotNone(resp)
        return resp  
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_get_folders(self):
                
        self.printHeader('test_get_folders')
        resp = nimosclientBase.getNimosClient().folders.list(detail=True,pageSize=2)
        self.assertIsNotNone(resp)        
        self.printFooter('test_get_folders')
        
        
        
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_create_folders(self):
                
        self.printHeader('test_create_folders')
        #folder creation requires pool_id. hence first get the ppol id
        poolresp = nimosclientBase.getNimosClient().pools.get()
        resp = self.createTestFolders(foldername=FOLDERS_NAME_1,
                                                     pool_id=poolresp.attrs.get("id"),
                                                     description="created by testcase",
                                                     limit_bytes=2000)
        self.assertIsNotNone(resp) 
        self.assertEqual(resp.attrs.get("name"),FOLDERS_NAME_1)
        self.assertEqual(resp.attrs.get("description"),"created by testcase")
        self.assertEqual(resp.attrs.get("limit_bytes"),2000)
                     
        self.printFooter('test_create_folders')
        
        
    
    @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true")
    def test_update_folders(self):
                
        self.printHeader('test_update_folders')
        #folder creation requires pool_id. hence first get the ppol id
        poolresp = nimosclientBase.getNimosClient().pools.get()
        resp = self.createTestFolders(foldername=FOLDERS_NAME_1,
                                                     pool_id=poolresp.attrs.get("id"),
                                                     description="created by testcase",
                                                     limit_bytes=2000)
        self.assertIsNotNone(resp) 
        self.assertEqual(resp.attrs.get("name"),FOLDERS_NAME_1)
        self.assertEqual(resp.attrs.get("description"),"created by testcase")
        self.assertEqual(resp.attrs.get("limit_bytes"),2000)
        
        #update few fields
        updateresp = nimosclientBase.getNimosClient().folders.update(id=resp.attrs.get("id"),
                                                           description="modified by testcase",
                                                           limit_bytes=4000,
                                                           name="folderupdatetestcase")
        self.assertIsNotNone(updateresp) 
        self.assertEqual(updateresp.attrs.get("name"),"folderupdatetestcase")
        self.assertEqual(updateresp.attrs.get("description"),"modified by testcase")
        self.assertEqual(updateresp.attrs.get("limit_bytes"),4000)                     
        self.printFooter('test_update_folders')
        

          

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
