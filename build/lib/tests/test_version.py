# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author mandar shivrekar

import pytest
import os
import nimbleclient
from tests.nimbleclientbase import SKIPTEST, log_to_file as log

'''Version check test for NimOS package'''

@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")

def test_nimos_sdk_package_versioning():
    log("**** Starting Tests for NimOS SDK package versioning TestCase *****\n")

    version = None
    with open(nimbleclient.__file__) as fh:
        info = fh.read()
        version = [line for line in info.split('\n') if line.startswith('__version__')][0].split(' = ')[1][1:-1]
        log("Obtained {!r} version for NimOS SDK package".format(version))
    assert(version is not None)

    log("**** Completed Tests for NimOS SDK package versioning TestCase *****\n")

