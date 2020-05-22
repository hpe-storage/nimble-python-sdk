
# nimbleclient.v1.api.subnets


## Subnet
```python
Subnet(self, id, attrs=None, client=None, collection=None)
```
Search subnets information. Many networking tasks require that objects such as replication partners are either on the same network or have a route to a secondary network.
Subnets let you create logical addressing for selective routing.

__Parameters__

- __id                   __: Identifier for the initiator group.
- __name                 __: Name of subnet configuration.
- __network              __: Subnet network address.
- __netmask              __: Subnet netmask address.
- __type                 __: Subnet type. Options include 'mgmt', 'data', and 'mgmt,data'.
- __allow_iscsi          __: Subnet type.
- __allow_group          __: Subnet type.
- __discovery_ip         __: Subnet network address.
- __mtu                  __: MTU for specified subnet. Valid MTU's are in the 512-16000 range.
- __netzone_type         __: Specify Network Affinity Zone type for iSCSI enabled subnets. Valid types are Single, Bisect, and EvenOdd for iSCSI subnets.
- __vlan_id              __: VLAN ID for specified subnet. Valid ID's are in the 1-4094 range.
- __creation_time        __: Time when this subnet configuration was created.
- __last_modified        __: Time when this subnet configuration was last modified.
- __failover             __: Failover setting of the subnet.
- __failover_enable_time __: Failover for this subnet will be enabled again at the time specified by failover_enable_time.


## SubnetList
```python
SubnetList(self, client=None)
```

