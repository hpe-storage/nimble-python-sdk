#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection
from ...exceptions import NimOSAPIOperationUnsupported


class AccessControlRecord(Resource):
    """Manage access control records for volumes.

    # Parameters
    id                   : Identifier for the access control record.
    apply_to             : Type of object this access control record applies to.
    chap_user_id         : Identifier for the CHAP user.
    chap_user_name       : Name of the CHAP user.
    initiator_group_id   : Identifier for the initiator group.
    initiator_group_name : Name of the initiator group.
    lun                  : If this access control record applies to a regular volume, this attribute is the volume's LUN (Logical Unit Number). If the access protocol is iSCSI,
                           the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual
                           Volume, this attribute is the volume's secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a
                           OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only
                           a snapshot, this attribute is not meaningful and is set to null.
    vol_id               : Identifier for the volume this access control record applies to.
    vol_name             : Name of the volume this access control record applies to.
    vol_agent_type       : External management agent type.
    pe_id                : Identifier for the protocol endpoint this access control record applies to.
    pe_name              : Name of the protocol endpoint this access control record applies to.
    pe_lun               : LUN (Logical Unit Number) to associate with this protocol endpoint. Valid LUNs are in the 0-2047 range.
    snap_id              : Identifier for the snapshot this access control record applies to.
    snap_name            : Name of the snapshot this access control record applies to.
    pe_ids               : List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This
                           field is required only when creating an access control record for a Virtual Volume.
    snapluns             : Information about the snapshot LUNs associated with this access control record. This field is meaningful when the online snapshot can be accessed as a
                           LUN in the group.
    creation_time        : Time when this access control record was created.
    last_modified        : Time when this access control record was last modified.
    access_protocol      : Access protocol of the volume.
    """

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")


class AccessControlRecordList(Collection):
    resource = AccessControlRecord
    resource_type = "access_control_records"

    def create(self, **kwargs):
        resp = self._client.create_resource(self.resource_type, **kwargs)
        return self.resource(resp['id'], resp, client=self._client, collection=self)

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
