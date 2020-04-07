#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#

class NimOSAuthenticationError(Exception):
    """Authentication to NimOS failed"""

class NimOSConnectionError(Exception):
    """Unable to connect to NimOS"""

class NimOSAPIError(Exception):
    """NimOS API call failed"""

class NimOSCLIError(Exception):
    """NimOS CLI command failed"""

class NimOSAPIOperationUnsupported(Exception):
    """NimOS API Operation not supported"""
