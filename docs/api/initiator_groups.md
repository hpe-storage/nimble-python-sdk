
# nimbleclient.v1.api.initiator_groups


## InitiatorGroup
```python
InitiatorGroup(self, id, attrs=None, client=None, collection=None)
```
Manage initiator groups for initiator authentication. An initiator group is a set of initiators that can be configured as part of your ACL to access a specific volume through
group membership.

__Parameters__

- __id               __: Identifier for initiator group.
- __name             __: Name of initiator group.
- __full_name        __: Initiator group's full name.
- __search_name      __: Initiator group name used for search.
- __description      __: Text description of initiator group.
- __access_protocol  __: Initiator group access protocol.
- __host_type        __: Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the
                   initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute.
- __fc_tdz_ports     __: List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group.
- __target_subnets   __: List of target subnet labels. If specified, discovery and access to volumes will be restricted to the specified subnets.
- __iscsi_initiators __: List of iSCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label.
- __fc_initiators    __: List of FC initiators. When create/update fc_initiators, wwpn is required.
- __creation_time    __: Time when this initiator group was created.
- __last_modified    __: Time when this initiator group was last modified.
- __vp_override      __: Flag to allow modifying VP created initiator groups. When set to true, user can add this initiator to a VP created initiator group.
- __app_uuid         __: Application identifier of initiator group.
- __volume_count     __: Number of volumes that are accessible by the initiator group.
- __volume_list      __: List of volumes that are accessible by the initiator group.
- __num_connections  __: Total number of connections from initiators in the initiator group.
- __metadata         __: Key-value pairs that augment an initiator group's attributes.


## InitiatorGroupList
```python
InitiatorGroupList(self, client=None)
```

