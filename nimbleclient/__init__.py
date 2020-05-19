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

__all__ = [
    "v1",
    "and_",
    "or_",
    "NimOSClient",
]


def NimOSClient(hostname, username, password, port=5392, version=1):
    """Instantiates Nimble client instance to interact with the NimOS REST API Server."""

    return getattr(nimbleclient, 'v1').NimOSClient(hostname, username, password, port)
