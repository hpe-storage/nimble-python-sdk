# Table of Contents

* [nimbleclient.v1.api.fibre\_channel\_configs](#nimbleclient.v1.api.fibre_channel_configs)
  * [FibreChannelConfig](#nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfig)
    * [regenerate](#nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfig.regenerate)
    * [hw\_upgrade](#nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfig.hw_upgrade)
  * [FibreChannelConfigList](#nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfigList)
    * [regenerate](#nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfigList.regenerate)
    * [hw\_upgrade](#nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfigList.hw_upgrade)

<a name="nimbleclient.v1.api.fibre_channel_configs"></a>
# nimbleclient.v1.api.fibre\_channel\_configs

<a name="nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfig"></a>
## FibreChannelConfig

```python
class FibreChannelConfig(Resource)
```

Manage group wide Fibre Channel configuration.

__Parameters__

- __id                 __: Identifier for Fibre Channel configuration.
- __array_list         __: List of array Fibre Channel configs.
- __group_leader_array __: Name of the group leader array.

<a name="nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfig.regenerate"></a>
#### regenerate

```python
 | regenerate(precheck, wwnn_base_str, **kwargs)
```

Regenerate Fibre Channel configuration.

__Parameters__

- __id            __: ID of the Fibre Channel configuration.
- __wwnn_base_str __: Base World Wide Node Name(WWNN).
- __precheck      __: Check if the interfaces are offline before regenerating the WWNN (World Wide Node Name).

<a name="nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfig.hw_upgrade"></a>
#### hw\_upgrade

```python
 | hw_upgrade(**kwargs)
```

Update Fibre Channel configuration after hardware changes.

__Parameters__

- __id __: ID of the Fibre Channel configuration.

<a name="nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfigList"></a>
## FibreChannelConfigList

```python
class FibreChannelConfigList(Collection)
```

<a name="nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfigList.regenerate"></a>
#### regenerate

```python
 | regenerate(id, precheck, wwnn_base_str, **kwargs)
```

Regenerate Fibre Channel configuration.

__Parameters__

- __id            __: ID of the Fibre Channel configuration.
- __wwnn_base_str __: Base World Wide Node Name(WWNN).
- __precheck      __: Check if the interfaces are offline before regenerating the WWNN (World Wide Node Name).

<a name="nimbleclient.v1.api.fibre_channel_configs.FibreChannelConfigList.hw_upgrade"></a>
#### hw\_upgrade

```python
 | hw_upgrade(id, **kwargs)
```

Update Fibre Channel configuration after hardware changes.

__Parameters__

- __id __: ID of the Fibre Channel configuration.

