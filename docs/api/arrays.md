
# nimbleclient.v1.api.arrays


## Array
```python
Array(self, id, attrs=None, client=None, collection=None)
```
Retrieve information of specified arrays. The array is the management and configuration for the underlying physical hardware array box.

__Parameters__

- __id                            __: Identifier for array.
- __name                          __: The user provided name of the array. It is also the array's hostname.
- __force                         __: Forcibly delete the specified array.
- __full_name                     __: The array's fully qualified name.
- __search_name                   __: The array name used for object search.
- __status                        __: Reachability status of the array in the group.
- __role                          __: Role of the array in the group.
- __group_state                   __: State of the array in the group.
- __pool_name                     __: Name of pool to which this is a member.
- __pool_id                       __: ID of pool to which this is a member.
- __model                         __: Array model.
- __serial                        __: Serial number of the array.
- __version                       __: Software version of the array.
- __is_sfa                        __: True if this array supports SFA; false otherwise.
- __creation_time                 __: Time when this array object was created.
- __last_modified                 __: Time when this array object was last modified.
- __usage_valid                   __: Indicates whether the usage of array is valid.
- __usable_capacity_bytes         __: The usable capacity of the array in bytes.
- __usable_cache_capacity_bytes   __: The usable cache capacity of the array in bytes.
- __raw_capacity_bytes            __: The raw capacity of the array in bytes.
- __vol_usage_bytes               __: The compressed usage of volumes in array.
- __vol_usage_uncompressed_bytes  __: The uncompressed usage of volumes in array. This is the pre-reduced usage.
- __vol_compression               __: The compression rate of volumes in array expressed as ratio.
- __vol_saved_bytes               __: The saved space of volumes in array.
- __snap_usage_bytes              __: The compressed usage of snapshots in array.
- __snap_usage_uncompressed_bytes __: The uncompressed usage of snapshots in array. This is the pre-reduced usage.
- __snap_compression              __: The compression rate of snapshots in array expressed as ratio.
- __snap_space_reduction          __: The space reduction rate of snapshots in array expressed as ratio.
- __snap_saved_bytes              __: The saved space of snapshots in array.
- __pending_delete_bytes          __: The pending delete bytes in array.
- __available_bytes               __: The available space of array.
- __usage                         __: Used space of the array in bytes.
- __all_flash                     __: Whether it is an all-flash array.
- __dedupe_capacity_bytes         __: The dedupe capacity of a hybrid array. Does not apply to all-flash arrays.
- __dedupe_usage_bytes            __: The dedupe usage of a hybrid array. Does not apply to all-flash arrays.
- __is_fully_dedupe_capable       __: Is array fully capable to dedupe its usable capacity.
- __extended_model                __: Extended model of the array.
- __is_supported_hw_config        __: Whether it is a supported hardware config.
- __gig_nic_port_count            __: Count of 1G NIC Ports installed on the array.
- __ten_gig_sfp_nic_port_count    __: Count of 10G SFP NIC Ports installed on the array.
- __ten_gig_t_nic_port_count      __: Count of 10G BaseT NIC Ports installed on the array.
- __fc_port_count                 __: Count of Fibre Channel Ports installed on the array.
- __public_key                    __: Public key of the array.
- __upgrade                       __: The array upgrade data.
- __create_pool                   __: Whether to create associated pool during array create.
- __pool_description              __: Text description of the pool to be created during array creation.
- __allow_lower_limits            __: A True setting will allow you to add an array with lower limits to a pool with higher limits.
- __ctrlr_a_support_ip            __: Controller A Support IP Address.
- __ctrlr_b_support_ip            __: Controller B Support IP Address.
- __nic_list                      __: List NICs information. Used when creating an array.
- __model_sub_type                __: Array model sub type.
- __zconf_ipaddrs                 __: List of link-local zero-configuration addresses of the array.
- __secondary_mgmt_ip             __: Secondary management IP address for the Group.


## ArrayList
```python
ArrayList(self, client=None)
```

