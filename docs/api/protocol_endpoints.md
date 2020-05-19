
# nimbleclient.v1.api.protocol_endpoints


## ProtocolEndpoint
```python
ProtocolEndpoint(self, id, attrs=None, client=None, collection=None)
```
Protocol endpoints are administrative logical units (LUs) in an LU conglomerate to be used with VMware Virtual Volumes.

__Parameters__

- __id                     __: Identifier for the protocol endpoint.
- __name                   __: Name of the protocol endpoint.
- __description            __: Text description of the protocol endpoint.
- __pool_name              __: Name of the pool where the protocol endpoint resides. If pool option is not specified, protocol endpoint is assigned to the default pool.
- __pool_id                __: Identifier associated with the pool in the storage pool table.
- __state                  __: Operational state of protocol endpoint.
- __serial_number          __: Identifier associated with the protocol endpoint for the SCSI protocol.
- __target_name            __: The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target protocol endpoint.
- __group_specific_ids     __: External UID is used to compute the serial number and IQN which never change even if the running group changes (e.g. after group merge).
                         Group-specific IDs determine whether external UID is used for computing serial number and IQN.
- __creation_time          __: Time when this protocol endpoint was created.
- __last_modified          __: Time when this protocol endpoint was last modified.
- __num_connections        __: Number of connections via this protocol endpoint.
- __num_iscsi_connections  __: Number of iSCSI connections via this protocol endpoint.
- __num_fc_connections     __: Number of FC connections via this protocol endpoint.
- __access_control_records __: List of access control records that apply to this protocol endpoint.
- __iscsi_sessions         __: List of iSCSI sessions connected to this protocol endpoint.
- __fc_sessions            __: List of FC sessions connected to this protocol endpoint.
- __access_protocol        __: Access protocol of the protocol endpoint. Only initiator groups with the same access protocol can access the protocol endpoint. If not specified in
                         the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre
                         Channel.


## ProtocolEndpointList
```python
ProtocolEndpointList(self, client=None)
```

