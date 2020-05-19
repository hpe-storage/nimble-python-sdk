
# nimbleclient.v1.api.initiators


## Initiator
```python
Initiator(self, id, attrs=None, client=None, collection=None)
```
Manage initiators in initiator groups. An initiator group has a set of initiators that can be configured as part of your ACL to access a specific volume through group
membership.

__Parameters__

- __id                      __: Identifier for initiator.
- __access_protocol         __: Access protocol used by the initiator. Valid values are 'iscsi' and 'fc'.
- __initiator_group_id      __: Identifier of the initiator group that this initiator is assigned to.
- __initiator_group_name    __: Name of the initiator group that this initiator is assigned to.
- __label                   __: Unique Identifier of the iSCSI initiator. Label is required when creating iSCSI initiator.
- __iqn                     __: IQN name of the iSCSI initiator. Each initiator IQN name must have an associated IP address specified using the 'ip_address' attribute. You can
                          choose not to enter the IP address for an initiator if you prefer not to authenticate using both name and IP address, in this case the IP address
                          will be returned as '*'.
- __ip_address              __: IP address of the iSCSI initiator. Each initiator IP address must have an associated name specified using 'name' attribute. You can choose not to
                          enter the name for an initiator if you prefer not to authenticate using both name and IP address, in this case the IQN name will be returned as '*'.
- __alias                   __: Alias of the Fibre Channel initiator. Maximum alias length is 32 characters. Each initiator alias must have an associated WWPN specified using the
                          'wwpn' attribute. You can choose not to enter the WWPN for an initiator when using previously saved initiator alias.
- __chapuser_id             __: Identifier for the CHAP user.
- __wwpn                    __: WWPN (World Wide Port Name) of the Fibre Channel initiator. WWPN is required when creating a Fibre Channel initiator. Each initiator WWPN can have an
                          associated alias specified using the 'alias' attribute. You can choose not to enter the alias for an initiator if you prefer not to assign an
                          initiator alias.
- __vp_override             __: Flag to allow modifying VP created initiator groups. When set to true, user can add this initiator to a VP created initiator group.
- __creation_time           __: Time when this initiator group was created.
- __last_modified           __: Time when this initiator group was last modified.
- __override_existing_alias __: Forcibly add Fibre Channel initiator to initiator group by updating or removing conflicting Fibre Channel initiator aliases.


## InitiatorList
```python
InitiatorList(self, client=None)
```

