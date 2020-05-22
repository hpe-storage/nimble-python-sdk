
# nimbleclient.v1.api.pools


## Pool
```python
Pool(self, id, attrs=None, client=None, collection=None)
```
Manage pools. Pools are an aggregation of arrays.

__Parameters__

- __id                            __: Identifier for the pool.
- __name                          __: Name of pool.
- __full_name                     __: Fully qualified name of pool.
- __search_name                   __: Name of pool used for object search.
- __description                   __: Text description of pool.
- __creation_time                 __: Time when this pool was created.
- __last_modified                 __: Time when this pool was last modified.
- __capacity                      __: Total storage space of the pool in bytes.
- __usage                         __: Used space of the pool in bytes.
- __savings                       __: Overall space usage savings in the pool.
- __savings_data_reduction        __: Space usage savings in the pool that does not include thin-provisioning savings.
- __savings_compression           __: Space usage savings in the pool due to compression.
- __savings_dedupe                __: Space usage savings in the pool due to deduplication.
- __savings_clone                 __: Space usage savings in the pool due to cloning of volumes.
- __savings_vol_thin_provisioning __: Space usage savings in the pool due to thin provisioning of volumes.
- __reserve                       __: Reserved space of the pool in bytes. Sum of volume reserve in the pool.
- __unused_reserve                __: Unused reserve space of the pool in bytes.
- __free_space                    __: Free space of the pool in bytes.
- __cache_capacity                __: Total usable cache capacity of the pool in bytes.
- __pinnable_cache_capacity       __: Total pinnable cache capacity of the pool in bytes.
- __pinned_cache_capacity         __: Total pinned cache capacity of the pool in bytes.
- __dedupe_capacity_bytes         __: The dedupe capacity of a hybrid pool. Does not apply to all-flash pools.
- __dedupe_usage_bytes            __: The dedupe usage of a hybrid pool. Does not apply to all-flash pools.
- __savings_ratio                 __: Overall space usage savings in the pool expressed as ratio.
- __data_reduction_ratio          __: Space usage savings in the pool expressed as ratio that does not include thin-provisioning savings.
- __compression_ratio             __: Compression savings for the pool expressed as ratio.
- __dedupe_ratio                  __: Dedupe savings for the pool expressed as ratio.
- __clone_ratio                   __: Clone savings for the pool expressed as ratio.
- __vol_thin_provisioning_ratio   __: Thin provisioning savings for volumes in the pool expressed as ratio.
- __snapcoll_count                __: Snapshot collection count.
- __snap_count                    __: Snapshot count.
- __array_count                   __: Number of arrays in the pool.
- __vol_count                     __: Number of volumes assigned to the pool.
- __array_list                    __: List of arrays in the pool with detailed information. When create/update array list, only arrays' ID is required.
- __unassigned_array_list         __: List of arrays being unassigned from the pool.
- __vol_list                      __: The list of volumes in the pool.
- __pinned_vol_list               __: The list of pinned volumes in the pool.
- __folder_list                   __: The list of fully qualified names of folders in the pool.
- __force                         __: Forcibly delete the specified pool even if it contains deleted volumes whose space is being reclaimed. Forcibly remove an array from array_list
                                via an update operation even if the array is not reachable. There should no volumes currently in the pool for the forced update operation to
                                succeed.
- __usage_valid                   __: Indicates whether the usage of pool is valid.
- __uncompressed_vol_usage_bytes  __: Uncompressed usage of volumes in the pool.
- __uncompressed_snap_usage_bytes __: Uncompressed usage of snapshots in the pool.
- __all_flash                     __: Indicate whether the pool is an all_flash pool.
- __dedupe_capable                __: Indicates whether the pool is capable of hosting deduped volumes.
- __dedupe_all_volumes_capable    __: Indicates whether the pool can enable dedupe by default.
- __dedupe_all_volumes            __: Indicates if dedupe is enabled by default for new volumes on this pool.
- __is_default                    __: Indicates if this is the default pool.


## PoolList
```python
PoolList(self, client=None)
```

