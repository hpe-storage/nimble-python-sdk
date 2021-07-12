# Table of Contents

* [nimbleclient.v1.api.network\_configs](#nimbleclient.v1.api.network_configs)
  * [NetworkConfig](#nimbleclient.v1.api.network_configs.NetworkConfig)
    * [activate\_netconfig](#nimbleclient.v1.api.network_configs.NetworkConfig.activate_netconfig)
    * [validate\_netconfig](#nimbleclient.v1.api.network_configs.NetworkConfig.validate_netconfig)
  * [NetworkConfigList](#nimbleclient.v1.api.network_configs.NetworkConfigList)
    * [activate\_netconfig](#nimbleclient.v1.api.network_configs.NetworkConfigList.activate_netconfig)
    * [validate\_netconfig](#nimbleclient.v1.api.network_configs.NetworkConfigList.validate_netconfig)

<a name="nimbleclient.v1.api.network_configs"></a>
# nimbleclient.v1.api.network\_configs

<a name="nimbleclient.v1.api.network_configs.NetworkConfig"></a>
## NetworkConfig

```python
class NetworkConfig(Resource)
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

<a name="nimbleclient.v1.api.network_configs.NetworkConfig.activate_netconfig"></a>
#### activate\_netconfig

```python
 | activate_netconfig(ignore_validation_mask, **kwargs)
```

Activate a network configuration.

__Parameters__

- __id                     __: ID of the netconfig to activate.
- __ignore_validation_mask __: Whether to ignore validation or not.

<a name="nimbleclient.v1.api.network_configs.NetworkConfig.validate_netconfig"></a>
#### validate\_netconfig

```python
 | validate_netconfig(ignore_validation_mask, **kwargs)
```

Validate a network configuration.

__Parameters__

- __id                     __: ID of the netconfig to validate.
- __ignore_validation_mask __: Whether to ignore validation or not.

<a name="nimbleclient.v1.api.network_configs.NetworkConfigList"></a>
## NetworkConfigList

```python
class NetworkConfigList(Collection)
```

<a name="nimbleclient.v1.api.network_configs.NetworkConfigList.activate_netconfig"></a>
#### activate\_netconfig

```python
 | activate_netconfig(id, ignore_validation_mask, **kwargs)
```

Activate a network configuration.

__Parameters__

- __id                     __: ID of the netconfig to activate.
- __ignore_validation_mask __: Whether to ignore validation or not.

<a name="nimbleclient.v1.api.network_configs.NetworkConfigList.validate_netconfig"></a>
#### validate\_netconfig

```python
 | validate_netconfig(id, ignore_validation_mask, **kwargs)
```

Validate a network configuration.

__Parameters__

- __id                     __: ID of the netconfig to validate.
- __ignore_validation_mask __: Whether to ignore validation or not.

