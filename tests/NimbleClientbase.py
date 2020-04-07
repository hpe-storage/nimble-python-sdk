# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 

"""Test base class for Nimos Client."""

import datetime
import time
import sys
import unittest
import configparser
import os
from functools import wraps # for decorating wraper function

nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

from nimbleclient.v1 import client 
#when debugging from the debugger, we want the log to be directed to the console rather than a file.
#hence the log file "unittest_result.log" and TestRun.log should not be created.for this to happen.
#please set the env variable "CONSOLELOG=1"
CONSOLELOG = int(os.getenv('CONSOLELOG',"0"))
logfolder= os.path.abspath(os.path.dirname(__file__))  + "\\" + "logs".strip()
unittestresultlog = logfolder  + "\\" + "Unittest_Summary.log".strip()

try:
    if os.path.exists(logfolder) == False:
            #create the folder
            os.mkdir(logfolder)
except Exception as ex:
        pass
try:
    os.remove(unittestresultlog)
except Exception as ex:
        pass

if CONSOLELOG == False:      
    TestcaseRunlogpath = os.path.abspath(logfolder)  + "\\" + "TestcaseRun.log".strip()
    try:
        sys.stdout = open(TestcaseRunlogpath, 'w')
    except Exception as ex:
        pass
    
def getUnittestlogfile():
        try:           
            logstream = open(unittestresultlog, 'a')
            return logstream
        except Exception :
            return sys.stdout


#global variables
NIMBLE_ARRAY_CREDENTIALS = "NimbleArrayCredentials"
ARRAY_HOSTNAME = "hostname"
ARRAY_USERNAME = "username"
ARRAY_PASSWORD = "password"


import logging
from contextlib import redirect_stdout

configPath =  os.path.join(os.path.abspath(os.path.dirname(__file__)),"config.ini")
osclient = None 

def getUniqueString(baseName):
        uniqueString = baseName + datetime.datetime.now().strftime("-%d-%m-%Y") + str(time.time())
        return uniqueString
     
   
def getConfigSectionDetail(sectionName):
        """Function reads all the values present in the given section and returns it as dict."""
        toreturn = {}        
        config =  configparser.ConfigParser()
        config.read(configPath)
        for section in config.sections():
            #print(section)
            if(sectionName == section):
                for option in config.options(section):
                    toreturn[option] = config.get(sectionName,option)        
        
        return toreturn
    

def getNimosClient():
    global osclient
    if  osclient == None:
        #Read the config which contains array credentials
        arrayDetail = getConfigSectionDetail(NIMBLE_ARRAY_CREDENTIALS)
        if(arrayDetail.__len__() == 3):            
            osclient = client.Client(arrayDetail[ARRAY_HOSTNAME],arrayDetail[ARRAY_USERNAME],arrayDetail[ARRAY_PASSWORD])
        else:
            raise Exception("Array Credentials not present in config file.")
    return osclient     
  


class NimosClientbaseTestCase(unittest.TestCase):
   # configPath =  os.path.join(os.path.abspath(os.path.dirname(__file__)),"config.ini")

    def __init__(self, methodName):
        unittest.TestCase.__init__(self,methodName)
        #pass
        
    @classmethod
    def setUpClass(cls):
        pass
        #setup the log file to store the test run log.do this only if we are not debugging        
      #  sys.stdout = open("TestcaseRun.log", 'a')
            #print("base setupclass opened log file")        
    
     

    def print_header_and_footer(self,func):
        """Decorator to print header and footer for unit tests."""
        @wraps(func)
        def wrapped(*args, **kwargs):
            #begin = time.time()
            test = args[0]
            test.printHeader(unittest.TestCase.id(test))
            result = func(*args, **kwargs)
            test.printFooter(unittest.TestCase.id(test))
            #end = time.time()
            return result
        return wrapped

    def printHeader(self, name):
        """Function to print header unit tests."""
        print("\n##Started testing '%s' at " % name, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    def printFooter(self, name):
        """Function to print header unit tests."""
        print("##Completed testing '%s'\n" % name)
