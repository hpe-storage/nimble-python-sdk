# (c) Copyright 2020 Hewlett Packard Enterprise Development LP

# @author mandar shivrekar

import pytest
import os

'''Version check test for NimOS package'''
from tests.nimbleclientbase import SKIPTEST, log_to_file as log
@pytest.mark.skipif(SKIPTEST is True,
                    reason="skipped this test as SKIPTEST variable is true")
def test_nimos_sdk_package_versioning():
    log("**** Starting Tests for NimOS SDK package versioning TestCase *****\n")

    version = None
    base_path = os.path.dirname(__file__)
    with open(os.path.join(base_path, '..', 'nimbleclient', '__init__.py')) as fh:
        info = fh.read()
        version = [line for line in info.split('\n') if line.startswith('__version__')][0].split(' = ')[1][1:-1]
        log("Obtained {!r} version for NimOS SDK package".format(version))
    assert(version is not None)

    log("**** Completed Tests for NimOS SDK package versioning TestCase *****\n")

