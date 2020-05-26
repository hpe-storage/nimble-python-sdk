#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#

import nimbleclient.v1

from .query import (
    and_,
    or_
)

# Version for NimbleOS SDK client package
__version__ = "1.0.0"

__all__ = [
    "v1",
    "and_",
    "or_",
    "NimOSClient",
]


def NimOSClient(hostname, username, password, job_timeout=60, port=5392, version=1):
    """Instantiates Nimble client instance to interact with the NimOS REST API Server."""

    return getattr(nimbleclient, f'v{version}').NimOSClient(hostname, username, password, job_timeout, port)
