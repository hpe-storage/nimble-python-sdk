# Table of Contents

* [nimbleclient.v1.api.initiator\_groups](#nimbleclient.v1.api.initiator_groups)
  * [InitiatorGroup](#nimbleclient.v1.api.initiator_groups.InitiatorGroup)
    * [suggest\_lun](#nimbleclient.v1.api.initiator_groups.InitiatorGroup.suggest_lun)
    * [validate\_lun](#nimbleclient.v1.api.initiator_groups.InitiatorGroup.validate_lun)
  * [InitiatorGroupList](#nimbleclient.v1.api.initiator_groups.InitiatorGroupList)
    * [suggest\_lun](#nimbleclient.v1.api.initiator_groups.InitiatorGroupList.suggest_lun)
    * [validate\_lun](#nimbleclient.v1.api.initiator_groups.InitiatorGroupList.validate_lun)

<a name="nimbleclient.v1.api.initiator_groups"></a>
# nimbleclient.v1.api.initiator\_groups

<a name="nimbleclient.v1.api.initiator_groups.InitiatorGroup"></a>
## InitiatorGroup

```python
class InitiatorGroup(Resource)
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

<a name="nimbleclient.v1.api.initiator_groups.InitiatorGroup.suggest_lun"></a>
#### suggest\_lun

```python
 | suggest_lun(**kwargs)
```

Suggest an LU number for the volume and initiator group combination.

__Parameters__

- __id     __: ID of the initiator group.
- __vol_id __: ID of the volume.

<a name="nimbleclient.v1.api.initiator_groups.InitiatorGroup.validate_lun"></a>
#### validate\_lun

```python
 | validate_lun(lun, **kwargs)
```

Validate an LU number for the volume and initiator group combination.

__Parameters__

- __id     __: ID of the initiator group.
- __vol_id __: ID of the volume.
- __lun    __: LU number to validate in decimal.

<a name="nimbleclient.v1.api.initiator_groups.InitiatorGroupList"></a>
## InitiatorGroupList

```python
class InitiatorGroupList(Collection)
```

<a name="nimbleclient.v1.api.initiator_groups.InitiatorGroupList.suggest_lun"></a>
#### suggest\_lun

```python
 | suggest_lun(id, **kwargs)
```

Suggest an LU number for the volume and initiator group combination.

__Parameters__

- __id     __: ID of the initiator group.
- __vol_id __: ID of the volume.

<a name="nimbleclient.v1.api.initiator_groups.InitiatorGroupList.validate_lun"></a>
#### validate\_lun

```python
 | validate_lun(id, lun, **kwargs)
```

Validate an LU number for the volume and initiator group combination.

__Parameters__

- __id     __: ID of the initiator group.
- __vol_id __: ID of the volume.
- __lun    __: LU number to validate in decimal.

