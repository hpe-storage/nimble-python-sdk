Integration Tests for Nimble Python SDK
=======================================
PREREQUISITE:
1.Please install python 3.6 and above.
2.Download and install Nimble python SDK using pip command. ex : pip install nimble-python-sdk. or from Github from the link https://github.com/hpe-storage/nimble-python-sdk
3.Edit the "Config.ini" file present under tests folder. Provide the Nible Array Credentials

For Developers who wish to add more testcase or want to debug testcase.
============================
If you want just to debug one testcase then do the following below steps:
1.set teh env variable "SKIPTEST=1"
2.go to the testcase you want to debug and do the below:
Modify the line @unittest.skipIf(SKIPTEST == True, "skipping this test as SKIPTEST variable is true") TO @unittest.skipIf(SKIPTEST == False, "skipping this test as SKIPTEST variable is true")
3.then attach the debugger to that testcase

Q. How to run all the test case in one shot
Ans: To run all the testcase in one shot and redirect the result to log file "python -m unittest discover <test_directory> > "
OR 
please set env variable "CONSOLELOG=0" and then run the below command "python -m unittest discover <test_directory>" .

This will create a log file named "UnittestResult.log" and "TestcaseRun.log" under the testcase/logs folder. UnittestResult.log has the summary of the testcase run whereas the Testcaserun.log will have the log for each test.

Example : go to testcase folder on cmd prompt and run "python -m unittest discover -v ."

Q. How do I run Individual Test case.
Ans : For individual TC : => python -m unittest -v <testmodule name> Ex : python -m unittest -v test_NimosClientUser.py 

Q. How do I run Some test case but not all of them.
Ans: If one needs to run few of them then give "python -m unittest -v <test_1.py test_2.py>"  Ex: "python -m unittest -v test_shelvs.py test_snapshots.py"