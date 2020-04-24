# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author alokranjan

"""Test base class for Nimos Client."""

from nimbleclient.v1 import client
import datetime
import time
import configparser
import os
import threading


# the below variable "SKIPTEST" is to be used if a user wants to just run one
# particular function.They should set the value of this to 1  on command
# prompt and then change the value of SKIPTEST to false for the function they
# wish to debug.If they want to skip the entire tests in this testcase, then
# easiest way is to change the value os.getenv('SKIPTEST', '0') TO
# os.getenv('SKIPTEST', '1') "set SKIPTEST=1"
SKIPTEST = bool(int(os.getenv('SKIPTEST', "0")))
log_folder = os.path.abspath(os.path.dirname(__file__)) + "\\" + "logs".strip()

try:
    if os.path.exists(log_folder) is False:
        # create the log folder
        os.mkdir(log_folder)
    testcase_run_log_file = os.path.abspath(
        log_folder) + "\\" + "TestcaseRun.log".strip()
    try:
        log_file = open(testcase_run_log_file, 'w')
        # create a thread lock to make sure only one thread writes to a file
        lock = threading.Lock()
    except Exception:
        pass
except Exception:
    pass

# constant variables
NIMBLE_ARRAY_CREDENTIALS = "NimbleArrayCredentials"
ARRAY_HOSTNAME = "hostname"
ARRAY_USERNAME = "username"
ARRAY_PASSWORD = "password"


config_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "config.ini")
os_client = None


def get_unique_string(baseName):
    time.sleep(0.1)
    unique_string = baseName + datetime.datetime.now().strftime(
        "-%d-%m-%Y") + \
        str(time.time())
    return unique_string


def get_config_section_detail(section_name):
    """Function reads all the values present in the given section
        and returns it as dict."""
    to_return = {}
    config = configparser.ConfigParser()
    config.read(config_path)
    for section in config.sections():
        # print(section)
        if(section_name == section):
            for option in config.options(section):
                to_return[option] = config.get(section_name, option)
    return to_return


def get_nimos_client():
    global os_client
    if os_client is None:
        # Read the config which contains array credentials
        array_detail = get_config_section_detail(NIMBLE_ARRAY_CREDENTIALS)
        if(array_detail.__len__() == 3):
            os_client = client.Client(
                array_detail[ARRAY_HOSTNAME],
                array_detail[ARRAY_USERNAME],
                array_detail[ARRAY_PASSWORD]
            )
        else:
            raise Exception("Array Credentials not present in config file.")
    return os_client


def log_header(name):
    """Function to print header unit tests."""
    # print("\n##Started testing '%s' at " %
    #       name, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    temp = "##Started testing '{name}' at {time}".format(
        name=name, time=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    log_to_file(temp)


def log_footer(name):
    """Function to print header unit tests."""
    temp = "##Completed testing '{name}' \n".format(name=name)
    # print("##Completed testing '%s' \n" % name)
    log_to_file(temp)
    log_file.flush()


def log_to_file(tolog):
    lock.acquire()
    print("%s" % tolog)
    # out, err = capfd.readouterr()
    time = " " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    tolog = "\n" + time + " " + str(tolog)
    log_file.write(tolog)
    lock.release()
