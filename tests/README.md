Integration Tests for Nimble Python SDK
================
The test case has been developed using Pytest Framework.

## PREREQUISITE.

1.Please install python 3.6 and above. ex : "pip install python3"

2.Install Pytest package using pip. ex : "pip install pytest"

3.Download and install Nimble python SDK using pip command. ex : "pip install nimble-python-sdk" Or from the link [nimble-python-sdk](https://github.com/hpe-storage/nimble-python-sdk)

4.Edit the "Config.ini" file present under tests folder. Provide the Nimble Array Credentials

For Developers who wish to add more test cases or want to debug testcase.
============================
If you want to debug just one testcase then do the following below steps:

1.Set the environment variable "SKIPTEST" to value 1.

2.Go to the testcase you want to debug and do the below:

Modify the line

@pytest.mark.skipif(SKIPTEST is True, reason="skipped this test as SKIPTEST variable is true")

TO

@pytest.mark.skipif(SKIPTEST == False, "skipped this test as SKIPTEST variable is true")

3.Attach the debugger to this testcase

Q. How to run all the test cases in one shot

Ans: To run all the test cases in one shot,go to the folder where the testscase resides and type  "pytest <test_directory> > " >> log.txt 2&>1 .
     This redirect the output to log file log.txt . Ex: pytest tests >> log.txt 2>&1
OR

Simply then run the command "pytest <test_directory>" or "pytest .". This command will search for all the test case which begins with "test_*.py" under the give directory and run them.

Logging:
=========================
There are three Log files which gets created whenever pytest is run against a single test case or All of them.
1. pytest_session.log : Contains the pytest_sessions related log. This log capturess the details of the test cases run.
2. pytest_summary.xml : Contains a summary of all the test case run in XML format. This xml can be further used to show the result of the tests on a Dashboard.
3. testcaserun.log : Contains debug logs which are present in the test case. 
Note : All the above log files are created under "tests/log" folder.

Q. How do I run individual test cases.

Ans : For individual TC : => pytest <testmodule name> Ex :pytest test_NimosClientUser.py

Q. How do I run some test cases but not all of them.

Ans: If one needs to run a few of them then give "pytest <test_1.py test_2.py>"
### Ex: "pytest test_shelvs.py test_snapshots.py"
