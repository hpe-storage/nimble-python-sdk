#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#


class NimOSClientError(Exception):
    """NimOS Client failed"""


class NimOSAuthenticationError(NimOSClientError):
    """Authentication to NimOS failed"""


class NimOSConnectionError(NimOSClientError):
    """Unable to connect to NimOS"""


class NimOSAPIError(NimOSClientError):
    """NimOS API call failed"""


class NimOSCLIError(NimOSClientError):
    """NimOS CLI command failed"""


class NimOSAPIOperationUnsupported(NimOSClientError):
    """NimOS API Operation not supported"""


class NimOSClientJobTimeoutError(NimOSClientError):
    """NimOS Client job timeout failure"""
