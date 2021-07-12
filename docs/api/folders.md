# Table of Contents

* [nimbleclient.v1.api.folders](#nimbleclient.v1.api.folders)
  * [Folder](#nimbleclient.v1.api.folders.Folder)
    * [set\_dedupe](#nimbleclient.v1.api.folders.Folder.set_dedupe)
  * [FolderList](#nimbleclient.v1.api.folders.FolderList)
    * [set\_dedupe](#nimbleclient.v1.api.folders.FolderList.set_dedupe)

<a name="nimbleclient.v1.api.folders"></a>
# nimbleclient.v1.api.folders

<a name="nimbleclient.v1.api.folders.Folder"></a>
## Folder

```python
class Folder(Resource)
```

Folders are a way to group volumes, as well as a way to apply space constraints to them.

__Parameters__

- __id                            __: Identifier for the folder.
- __name                          __: Name of folder.
- __fqn                           __: Fully qualified name of folder in the pool.
- __full_name                     __: Fully qualified name of folder in the group.
- __search_name                   __: Name of folder used for object search.
- __description                   __: Text description of folder.
- __pool_name                     __: Name of the pool where the folder resides.
- __pool_id                       __: ID of the pool where the folder resides.
- __limit_bytes_specified         __: Indicates whether the folder has a limit.
- __limit_bytes                   __: Folder limit size in bytes. By default, a folder (except SMIS and VVol types) does not have a limit. If limit_bytes is not specified when a
                                folder is created, or if limit_bytes is set to the largest possible 64-bit signed integer (9223372036854775807), then the folder has no limit.
                                Otherwise, a limit smaller than the capacity of the pool can be set. On output, if the folder has a limit, the limit_bytes_specified attribute
                                will be true and limit_bytes will be the limit. If the folder does not have a limit, the limit_bytes_specified attribute will be false and
                                limit_bytes will be interpreted based on the value of the usage_valid attribute. If the usage_valid attribute is true, limits_byte will be the
                                capacity of the pool. Otherwise, limits_bytes is not meaningful and can be null. SMIS and VVol folders require a size limit. This attribute is
                                superseded by limit_size_bytes.
- __limit_size_bytes              __: Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder
                                has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of 'smis' or 'vvol' must have a
                                size limit.
- __provisioned_limit_size_bytes  __: Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if
                                provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit.
- __overdraft_limit_pct           __: Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is
                                the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued.
- __capacity_bytes                __: Capacity of the folder in bytes. If the folder's size has a usage limit, capacity_bytes will be the folder's usage limit. If the folder's size
                                does not have a usage limit, capacity_bytes will be the pool's capacity. This field is meaningful only when the usage_valid attribute is true.
- __free_space_bytes              __: Free space in the folder in bytes. If the folder has a usage limit, free_space_bytes will be the folder's free space (the folder's usage limit
                                minus the folder's space usage). If the folder does not have a usage limit, free_space_bytes will be the pool's free space. This field is
                                meaningful only when the usage_valid attribute is true.
- __provisioned_bytes             __: Sum of provisioned size of volumes in the folder.
- __usage_bytes                   __: Sum of mapped usage and snapshot uncompressed usage of volumes in the folder.
- __volume_mapped_bytes           __: Sum of mapped usage of volumes in the folder.
- __usage_valid                   __: Indicate whether the space usage attributes of folder are valid.
- __agent_type                    __: External management agent type.
- __inherited_vol_perfpol_id      __: Identifier of the default performance policy for a newly created volume.
- __inherited_vol_perfpol_name    __: Name of the default performance policy for a newly created volume.
- __unused_reserve_bytes          __: Unused reserve of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.
- __unused_snap_reserve_bytes     __: Unused reserve of snapshots of volumes in the folder in bytes. This field is meaningful only when the usage_valid attribute is true.
- __compressed_vol_usage_bytes    __: Compressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.
- __compressed_snap_usage_bytes   __: Compressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.
- __uncompressed_vol_usage_bytes  __: Uncompressed usage of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.
- __uncompressed_snap_usage_bytes __: Uncompressed usage of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.
- __vol_compression_ratio         __: Compression ratio of volumes in the folder. This field is meaningful only when the usage_valid attribute is true.
- __snap_compression_ratio        __: Compression ratio of snapshots in the folder. This field is meaningful only when the usage_valid attribute is true.
- __compression_ratio             __: Compression savings for the folder expressed as ratio. This field is meaningful only when the usage_valid attribute is true.
- __creation_time                 __: Time when this folder was created.
- __last_modified                 __: Time when this folder was last modified.
- __num_snaps                     __: Number of snapshots inside the folder. This attribute is deprecated and has no meaningful value.
- __num_snapcolls                 __: Number of snapshot collections inside the folder. This attribute is deprecated and has no meaningful value.
- __app_uuid                      __: Application identifier of the folder.
- __volume_list                   __: List of volumes contained by the folder.
- __appserver_id                  __: Identifier of the application server associated with the folder.
- __appserver_name                __: Name of the application server associated with the folder.
- __folset_id                     __: Identifier of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing
                                folder set must be associated with the same application server.
- __folset_name                   __: Name of the folder set associated with the folder. Only VVol folder can be associated with the folder set. The folder and the containing folder
                                set must be associated with the same application server.
- __limit_iops                    __: IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS
                                limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited.
- __limit_mbps                    __: Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the
                                folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited.
- __access_protocol               __: Access protocol of the folder. This attribute is used by the VASA Provider to determine the access protocol of the bind request. If not
                                specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default
                                will be Fibre Channel. This field is meaningful only to VVol folder.
- __tenant_id                     __: Tenant ID of the folder. This is used to determine what tenant context the folder belongs to.

<a name="nimbleclient.v1.api.folders.Folder.set_dedupe"></a>
#### set\_dedupe

```python
 | set_dedupe(dedupe_enabled, **kwargs)
```

Set dedupe enabled/disabled for all applicable volumes inside a folder.

__Parameters__

- __dedupe_enabled __: Enable/disable dedupe.
- __id             __: Folder containing the volumes to enable/disable dedupe on.

<a name="nimbleclient.v1.api.folders.FolderList"></a>
## FolderList

```python
class FolderList(Collection)
```

<a name="nimbleclient.v1.api.folders.FolderList.set_dedupe"></a>
#### set\_dedupe

```python
 | set_dedupe(id, dedupe_enabled, **kwargs)
```

Set dedupe enabled/disabled for all applicable volumes inside a folder.

__Parameters__

- __dedupe_enabled __: Enable/disable dedupe.
- __id             __: Folder containing the volumes to enable/disable dedupe on.

