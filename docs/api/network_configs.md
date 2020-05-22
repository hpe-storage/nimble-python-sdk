
# nimbleclient.v1.api.network_configs


## NetworkConfig
```python
NetworkConfig(self, id, attrs=None, client=None, collection=None)
```
Manage group wide network configuration. The three possible network configurations include active, backup and an optional draft configuration.

__Parameters__

- __id                                __: Identifier for network configuration.
- __name                              __: Name of the network configuration. Use the name 'draft' when creating a draft configuration.
- __mgmt_ip                           __: Management IP address for the Group.
- __secondary_mgmt_ip                 __: Secondary management IP address for the Group.
- __role                              __: Role of network configuration.
- __iscsi_automatic_connection_method __: Whether automatic connection method is enabled. Enabling this means means redirecting connections from the specified iSCSI discovery IP
                                    address to the best data IP address based on connection counts.
- __iscsi_connection_rebalancing      __: Whether rebalancing is enabled. Enabling this means rebalancing iSCSI connections by periodically breaking existing connections that are
                                    out-of-balance, allowing the host to reconnect to a more appropriate data IP address.
- __route_list                        __: List of static routes.
- __subnet_list                       __: List of subnet configs.
- __array_list                        __: List of array network configs.
- __group_leader_array                __: Name of the group leader array.
- __creation_time                     __: Time when this net configuration was created.
- __last_modified                     __: Time when this network configuration was last modified.
- __active_since                      __: Start time of activity.
- __last_active                       __: Time of last activity.
- __ignore_validation_mask            __: Indicates whether to ignore the validation.


## NetworkConfigList
```python
NetworkConfigList(self, client=None)
```

