
# nimbleclient.v1.api.access_control_records


## AccessControlRecord
```python
AccessControlRecord(self, id, attrs=None, client=None, collection=None)
```
Manage access control records for volumes.

__Parameters__

- __id                   __: Identifier for the access control record.
- __apply_to             __: Type of object this access control record applies to.
- __chap_user_id         __: Identifier for the CHAP user.
- __chap_user_name       __: Name of the CHAP user.
- __initiator_group_id   __: Identifier for the initiator group.
- __initiator_group_name __: Name of the initiator group.
- __lun                  __: If this access control record applies to a regular volume, this attribute is the volume's LUN (Logical Unit Number). If the access protocol is iSCSI,
                       the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual
                       Volume, this attribute is the volume's secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a
                       OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only
                       a snapshot, this attribute is not meaningful and is set to null.
- __vol_id               __: Identifier for the volume this access control record applies to.
- __vol_name             __: Name of the volume this access control record applies to.
- __vol_agent_type       __: External management agent type.
- __pe_id                __: Identifier for the protocol endpoint this access control record applies to.
- __pe_name              __: Name of the protocol endpoint this access control record applies to.
- __pe_lun               __: LUN (Logical Unit Number) to associate with this protocol endpoint. Valid LUNs are in the 0-2047 range.
- __snap_id              __: Identifier for the snapshot this access control record applies to.
- __snap_name            __: Name of the snapshot this access control record applies to.
- __pe_ids               __: List of candidate protocol endpoints that may be used to access the Virtual Volume. One of them will be selected for the access control record. This
                       field is required only when creating an access control record for a Virtual Volume.
- __snapluns             __: Information about the snapshot LUNs associated with this access control record. This field is meaningful when the online snapshot can be accessed as a
                       LUN in the group.
- __creation_time        __: Time when this access control record was created.
- __last_modified        __: Time when this access control record was last modified.
- __access_protocol      __: Access protocol of the volume.


## AccessControlRecordList
```python
AccessControlRecordList(self, client=None)
```

