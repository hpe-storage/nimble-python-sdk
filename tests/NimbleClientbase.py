# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan 

"""Test base class for Nimos Client."""

import datetime
import time
import sys
import unittest
import configparser
import os
import logging
from functools import wraps # for decorating wraper function

nimosClientPackagePath =    os.path.join(os.path.abspath(os.path.dirname(__file__)),"..\\")
sys.path.append(nimosClientPackagePath) #need this path to search modules when debugging from editor

from nimbleclient.v1 import client 

#the below variable "SKIPTEST" is to be used if a user wants to just run one particular function .
#they should set the value of this to 1  on command prompt and then change the value of SKIPTEST to flase for the function they wish to debug.
#if they want to skip the entire tests in this testcase, then easiest way is to change the value os.getenv('SKIPTEST', '0') TO os.getenv('SKIPTEST', '1')
#"set SKIPTEST=1"
SKIPTEST = int(os.getenv('SKIPTEST', '0'))

#when debugging from the debugger, we want the log to be directed to the console rather than a file.
#hence the log file "unittest_summary.log" and TestRun.log should not be created.for this to happen.
#please set the env variable "CONSOLELOG=1"
CONSOLELOG = int(os.getenv('CONSOLELOG',"0"))
logfolder= os.path.abspath(os.path.dirname(__file__))  + "\\" + "logs".strip()
unittestresultlog = logfolder  + "\\" + "Unittest_Summary.log".strip()

try:
    if os.path.exists(logfolder) == False:
            #create the log folder
            os.mkdir(logfolder)
except Exception as ex:
        pass
try:
    os.remove(unittestresultlog)
except Exception as ex:
        pass

if CONSOLELOG == False:      
    TestcaseRunlogfile = os.path.abspath(logfolder)  + "\\" + "TestcaseRun.log".strip()
    try:
        sys.stdout = open(TestcaseRunlogfile, 'w')
        sys.stderr = open(unittestresultlog, 'a') #let the summary of test go to different file
    except Exception as ex:
        pass
    
#global variables
NIMBLE_ARRAY_CREDENTIALS = "NimbleArrayCredentials"
ARRAY_HOSTNAME = "hostname"
ARRAY_USERNAME = "username"
ARRAY_PASSWORD = "password"


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

    def __init__(self, methodName):
        unittest.TestCase.__init__(self,methodName)
       
    @classmethod
    def tearDownClass(cls):
        #flush the logs
        sys.stdout.flush()
        sys.stderr.flush()
          

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
        #print("\n##Started testing '%s' " % name)

    def printFooter(self, name):
        """Function to print header unit tests."""
        print("##Completed testing '%s' \n" % name)
       
        
        
        
# class StreamToLogger(object):
#    """
#    Fake file-like stream object that redirects writes to a logger instance.
#    """
#    def __init__(self, logger, log_level=logging.INFO):
#       self.logger = logger
#       self.log_level = log_level
#       self.linebuf = ''
#       #self.logger.flush = logger.flush

#    def write(self, buf):       
#         for line in buf.rstrip().splitlines():
#              self.logger.log(self.log_level, line.rstrip())
     
         
#    def flush(self):
#      pass        
         
    

# logging.basicConfig(
#     level=logging.INFO,
#     #format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
#     format='%(asctime)s:  %(message)s',
#     filename=unittestresultlog,
#     filemode='a'
# )

# stdout_logger = logging.getLogger('STDOUT')
# s2 = StreamToLogger(stdout_logger, logging.INFO)
# sys.stdout = s2

# stderr_logger = logging.getLogger('STDERR')
# sl = StreamToLogger(stderr_logger, logging.ERROR)
# sys.stderr = sl

