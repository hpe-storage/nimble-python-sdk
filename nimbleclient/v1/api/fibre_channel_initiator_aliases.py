#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection
from ...exceptions import NimOSAPIOperationUnsupported


class FibreChannelInitiatorAlias(Resource):
    '''
    This API provides the alias information for Fibre Channel initiators.

    Parameters:
    - id     : Unique identifier for the Fibre Channel initiator alias.
    - alias  : Alias of the Fibre Channel initiator.
    - wwpn   : WWPN (World Wide Port Name) of the Fibre Channel initiator.
    - source : Source of the Fibre Channel initiator alias.
    '''

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")


class FibreChannelInitiatorAliasList(Collection):
    resource = FibreChannelInitiatorAlias
    resource_type = "fibre_channel_initiator_aliases"

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
