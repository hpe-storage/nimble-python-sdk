# Table of Contents

* [nimbleclient.v1.api.volumes](#nimbleclient.v1.api.volumes)
  * [Volume](#nimbleclient.v1.api.volumes.Volume)
    * [restore](#nimbleclient.v1.api.volumes.Volume.restore)
    * [move](#nimbleclient.v1.api.volumes.Volume.move)
    * [bulk\_move](#nimbleclient.v1.api.volumes.Volume.bulk_move)
    * [abort\_move](#nimbleclient.v1.api.volumes.Volume.abort_move)
    * [bulk\_set\_dedupe](#nimbleclient.v1.api.volumes.Volume.bulk_set_dedupe)
    * [bulk\_set\_online\_and\_offline](#nimbleclient.v1.api.volumes.Volume.bulk_set_online_and_offline)
    * [online](#nimbleclient.v1.api.volumes.Volume.online)
    * [offline](#nimbleclient.v1.api.volumes.Volume.offline)
    * [associate](#nimbleclient.v1.api.volumes.Volume.associate)
    * [dissociate](#nimbleclient.v1.api.volumes.Volume.dissociate)
  * [VolumeList](#nimbleclient.v1.api.volumes.VolumeList)
    * [restore](#nimbleclient.v1.api.volumes.VolumeList.restore)
    * [move](#nimbleclient.v1.api.volumes.VolumeList.move)
    * [bulk\_move](#nimbleclient.v1.api.volumes.VolumeList.bulk_move)
    * [abort\_move](#nimbleclient.v1.api.volumes.VolumeList.abort_move)
    * [bulk\_set\_dedupe](#nimbleclient.v1.api.volumes.VolumeList.bulk_set_dedupe)
    * [bulk\_set\_online\_and\_offline](#nimbleclient.v1.api.volumes.VolumeList.bulk_set_online_and_offline)
    * [online](#nimbleclient.v1.api.volumes.VolumeList.online)
    * [offline](#nimbleclient.v1.api.volumes.VolumeList.offline)
    * [associate](#nimbleclient.v1.api.volumes.VolumeList.associate)
    * [dissociate](#nimbleclient.v1.api.volumes.VolumeList.dissociate)

<a name="nimbleclient.v1.api.volumes"></a>
# nimbleclient.v1.api.volumes

<a name="nimbleclient.v1.api.volumes.Volume"></a>
## Volume

```python
class Volume(Resource)
```

Volumes are the basic storage units from which the total capacity is apportioned. The terms volume and LUN are used interchangeably.The number of volumes per array depends on
storage allocation.

__Parameters__

- __id                            __: Identifier for the volume.
- __name                          __: Name of the volume.
- __full_name                     __: Fully qualified name of volume.
- __search_name                   __: Name of volume used for object search.
- __size                          __: Volume size in mebibytes. Size is required for creating a volume but not for cloning an existing volume.
- __description                   __: Text description of volume.
- __perfpolicy_name               __: Name of performance policy.
- __perfpolicy_id                 __: Identifier of the performance policy. After creating a volume, performance policy for the volume can only be changed to another performance
                                policy with same block size.
- __reserve                       __: Amount of space to reserve for this volume as a percentage of volume size.
- __warn_level                    __: This attribute is deprecated. Alert threshold for the volume's mapped usage, expressed as a percentage of the volume's size. When the volume's
                                mapped usage exceeds warn_level, the array issues an alert. If this option is not specified, array default volume warn level setting is used to
                                decide the warning level for this volume.
- __limit                         __: Limit on the volume's mapped usage, expressed as a percentage of the volume's size. When the volume's mapped usage exceeds limit, the volume
                                will be offlined or made non-writable. If this option is not specified, array default volume limit setting is used to decide the limit for this
                                volume.
- __snap_reserve                  __: Amount of space to reserve for snapshots of this volume as a percentage of volume size.
- __snap_warn_level               __: Threshold for available space as a percentage of volume size below which an alert is raised.
- __snap_limit                    __: This attribute is deprecated. The array does not limit a volume's snapshot space usage. The attribute is ignored on input and returns max int64
                                on output.
- __snap_limit_percent            __: This attribute is deprecated. The array does not limit a volume's snapshot space usage. The attribute is ignored on input and returns -1 on
                                output.
- __num_snaps                     __: Number of live, non-hidden snapshots for this volume.
- __projected_num_snaps           __: Deprecated. Projected number of snapshots (including scheduled and manual) for this volume.
- __online                        __: Online state of volume, available for host initiators to establish connections.
- __owned_by_group                __: Name of group that currently owns the volume.
- __owned_by_group_id             __: ID of group that currently owns the volume.
- __multi_initiator               __: For iSCSI Volume Target, this flag indicates whether the volume and its snapshots can be accessed from multiple initiators at the same time.
                                The default is false. For iSCSI Group Target or FC access protocol, the attribute cannot be modified and always reads as false.
- __iscsi_target_scope            __: This indicates whether volume is exported under iSCSI Group Target or iSCSI Volume Target. This attribute is only meaningful to iSCSI system.
                                On FC system, all volumes are exported under the FC Group Target. In create operation, the volume's target type will be set by this attribute.
                                If not specified, it will be set as the group-setting. In clone operation, the clone's target type will inherit from the parent' setting.
- __pool_name                     __: Name of the pool where the volume resides. Volume data will be distributed across arrays over which specified pool is defined. If pool option
                                is not specified, volume is assigned to the default pool.
- __pool_id                       __: Identifier associated with the pool in the storage pool table.
- __read_only                     __: Volume is read-only.
- __serial_number                 __: Identifier associated with the volume for the SCSI protocol.
- __secondary_serial_number       __: Secondary identifier associated with the volume for the SCSI protocol.
- __target_name                   __: The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target volume.
- __block_size                    __: Size in bytes of blocks in the volume.
- __offline_reason                __: Volume offline reason.
- __clone                         __: Whether this volume is a clone. Use this attribute in combination with name and base_snap_id to create a clone by setting clone = true.
- __parent_vol_name               __: Name of parent volume.
- __parent_vol_id                 __: Parent volume ID.
- __base_snap_name                __: Name of base snapshot.
- __base_snap_id                  __: Base snapshot ID. This attribute is required together with name and clone when cloning a volume with the create operation.
- __replication_role              __: Replication role that this volume performs.
- __volcoll_name                  __: Name of volume collection of which this volume is a member.
- __volcoll_id                    __: ID of volume collection of which this volume is a member. Use this attribute in update operation to associate or dissociate volumes with or
                                from volume collections. When associating, set this attribute to the ID of the volume collection. When dissociating, set this attribute to
                                empty string.
- __agent_type                    __: External management agent type.
- __force                         __: Forcibly offline, reduce size or change read-only status a volume.
- __creation_time                 __: Time when this volume was created.
- __last_modified                 __: Time when this volume was last modified.
- __protection_type               __: Specifies if volume is protected with schedules. If protected, indicate whether replication is setup.
- __last_snap                     __: Last snapshot for this volume.
- __last_replicated_snap          __: Last replicated snapshot for this volume.
- __dest_pool_name                __: Name of the destination pool where the volume is moving to.
- __dest_pool_id                  __: ID of the destination pool where the volume is moving to.
- __move_start_time               __: The Start time when this volume was moved.
- __move_aborting                 __: This indicates whether the move of the volume is aborting or not.
- __move_bytes_migrated           __: The bytes of volume which have been moved.
- __move_bytes_remaining          __: The bytes of volume which have not been moved.
- __move_est_compl_time           __: The estimated time of completion of a move.
- __usage_valid                   __: This indicates whether usage information of volume and snapshots are valid or not.
- __space_usage_level             __: Indicates space usage level based on warning level.
- __total_usage_bytes             __: Sum of volume mapped usage and uncompressed backup data(including pending deletes) in bytes of this volume.
- __vol_usage_compressed_bytes    __: Compressed data in bytes for this volume.
- __vol_usage_uncompressed_bytes  __: Uncompressed data in bytes for this volume.
- __vol_usage_mapped_bytes        __: Mapped data in bytes for this volume.
- __snap_usage_compressed_bytes   __: Sum of compressed backup data in bytes stored in snapshots of this volume.
- __snap_usage_uncompressed_bytes __: Sum of uncompressed unique backup data in bytes stored in snapshots of this volume.
- __snap_usage_populated_bytes    __: Sum of backup data in bytes stored in snapshots of this volume without accounting for the sharing of data between snapshots.
- __cache_pinned                  __: If set to true, all the contents of this volume are kept in flash cache. This provides for consistent performance guarantees for all types of
                                workloads. The amount of flash needed to pin the volume is equal to the limit for the volume.
- __pinned_cache_size             __: The amount of flash pinned on the volume.
- __cache_needed_for_pin          __: The amount of flash needed to pin the volume.
- __upstream_cache_pinned         __: This indicates whether the upstream volume is cache pinned or not.
- __cache_policy                  __: Cache policy applied to the volume.
- __thinly_provisioned            __: Set volume's provisioning level to thin.  Also advertises volume as thinly provisioned to initiators supporting thin provisioning. For such
                                volumes, soft limit notification is set to initiators when the volume space usage crosses its volume_warn_level. Default is yes. The volume's
                                space is provisioned immediately, but for advertising status, this change takes effect only for new connections to the volume. Initiators must
                                disconnect and reconnect for the new setting to be take effect at the initiator level consistently.
- __vol_state                     __: Status of the volume.
- __online_snaps                  __: The list of online snapshots of this volume.
- __num_connections               __: Number of connections of this volume.
- __num_iscsi_connections         __: Number of iscsi connections of this volume.
- __num_fc_connections            __: Number of Fibre Channel connections of this volume.
- __access_control_records        __: List of access control records that apply to this volume.
- __inherit_acl                   __: In a volume clone operation, if both the parent and the clone have no external management agent (their agent_type property is "none"), then
                                inherit_acl controls whether the clone will inherit a copy of the parent's access control list. If either the parent or the clone have an
                                external management agent, then the clone will not inherit the parent's access control list.
- __encryption_cipher             __: The encryption cipher of the volume.
- __app_uuid                      __: Application identifier of volume.
- __folder_id                     __: ID of the folder holding this volume.
- __folder_name                   __: Name of the folder holding this volume. It can be empty.
- __metadata                      __: Key-value pairs that augment an volume's attributes.
- __iscsi_sessions                __: List of iSCSI sessions connected to this volume.
- __fc_sessions                   __: List of Fibre Channel sessions connected to this volume.
- __caching_enabled               __: Indicate caching the volume is enabled.
- __previously_deduped            __: Indicate whether dedupe has ever been enabled on this volume.
- __dedupe_enabled                __: Indicate whether dedupe is enabled.
- __vpd_t10                       __: The volume's T10 Vendor ID-based identifier.
- __vpd_ieee0                     __: The first 64 bits of the volume's EUI-64 identifier, encoded as a hexadecimal string.
- __vpd_ieee1                     __: The last 64 bits of the volume's EUI-64 identifier, encoded as a hexadecimal string.
- __app_category                  __: Application category that the volume belongs to.
- __limit_iops                    __: IOPS limit for this volume. If limit_iops is not specified when a volume is created, or if limit_iops is set to -1, then the volume has no IOPS
                                limit. If limit_iops is not specified while creating a clone, IOPS limit of parent volume will be used as limit. IOPS limit should be in range
                                [256, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other
                                words, IOPS and MBPS limits should honor limit_iops <= ((limit_mbps MB/s * 2^20 B/MB) / block_size B).
- __limit_mbps                    __: Throughput limit for this volume in MB/s. If limit_mbps is not specified when a volume is created, or if limit_mbps is set to -1, then the
                                volume has no MBPS limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified,
                                limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops <= ((limit_mbps MB/s * 2^20 B/MB) /
                                block_size B).
- __needs_content_repl            __: Indicates whether the volume needs content based replication.
- __content_repl_errors_found     __: Indicates whether the last content based replication had errors.
- __last_content_snap_br_cg_uid   __: The branch cg uid of the content based snapshot that was last replicated.
- __last_content_snap_br_gid      __: The branch gid of the content based snapshot that was last replicated.
- __last_content_snap_id          __: The ID of the content based snapshot that was last replicated.
- __cksum_last_verified           __: Last checksum verification time.
- __pre_filter                    __: Pre-filtering criteria.
- __avg_stats_last_5mins          __: Average statistics in last 5 minutes.
- __srep_last_sync                __: Time when synchronously replicated volume was last synchronized.
- __srep_resync_percent           __: Percentage of resync progress for synchronously replicated volume.

<a name="nimbleclient.v1.api.volumes.Volume.restore"></a>
#### restore

```python
 | restore(base_snap_id, **kwargs)
```

Restore volume data from a previous snapshot.

__Parameters__

- __id           __: ID of the restored volume.
- __base_snap_id __: ID of the snapshot to which this the volume is restored.

<a name="nimbleclient.v1.api.volumes.Volume.move"></a>
#### move

```python
 | move(dest_pool_id, **kwargs)
```

Move a volume and its related volumes to another pool. To change a single volume's folder assignment (while remaining in the same pool), use a volume update operation to
change the folder_id attribute.

__Parameters__

- __id           __: ID of the volume to move.
- __dest_pool_id __: ID of the destination pool or folder. Specify a pool ID when the volumes should not be in a folder; otherwise, specify a folder ID and the pool will be
               derived from the folder.
- __force_vvol   __: Forcibly move a Virtual Volume. Moving Virtual Volume is disruptive to the vCenter, hence it should only be done by the VASA Provider (VP). This flag should
               only be set by the VP when it calls this API.

<a name="nimbleclient.v1.api.volumes.Volume.bulk_move"></a>
#### bulk\_move

```python
 | bulk_move(dest_pool_id, vol_ids, **kwargs)
```

Move volumes and their related volumes to another pool. To change a single volume's folder assignment (while remaining in the same pool), use a volume update operation to
change the folder_id attribute.

__Parameters__

- __vol_ids      __: IDs of the volumes to move.
- __dest_pool_id __: ID of the destination pool or folder. Specify a pool ID when the volumes should not be in a folder; otherwise, specify a folder ID and the pool will be
               derived from the folder.
- __force_vvol   __: Forcibly move a Virtual Volume. Moving Virtual Volume is disruptive to the vCenter, hence it should only be done by the VASA Provider (VP). This flag should
               only be set by the VP when it calls this API.

<a name="nimbleclient.v1.api.volumes.Volume.abort_move"></a>
#### abort\_move

```python
 | abort_move(**kwargs)
```

Abort the in-progress move of the specified volume to another pool.

__Parameters__

- __id __: ID of the volume to stop moving to a different pool.

<a name="nimbleclient.v1.api.volumes.Volume.bulk_set_dedupe"></a>
#### bulk\_set\_dedupe

```python
 | bulk_set_dedupe(dedupe_enabled, vol_ids, **kwargs)
```

Enable or disable dedupe on a list of volumes. If the volumes are not dedupe capable, the operation will fail for the specified volume.

__Parameters__

- __vol_ids        __: IDs of the volumes to enable/disable dedupe.
- __dedupe_enabled __: Dedupe property to be applied to the list of volumes.

<a name="nimbleclient.v1.api.volumes.Volume.bulk_set_online_and_offline"></a>
#### bulk\_set\_online\_and\_offline

```python
 | bulk_set_online_and_offline(online, vol_ids, **kwargs)
```

Bring a list of volumes online or offline.

__Parameters__

- __vol_ids __: IDs of the volumes to set online or offline.
- __online  __: Desired state of the volumes. "true" for online, "false" for offline.

<a name="nimbleclient.v1.api.volumes.Volume.online"></a>
#### online

```python
 | online()
```

Bring volume online.

<a name="nimbleclient.v1.api.volumes.Volume.offline"></a>
#### offline

```python
 | offline()
```

Take volume offline.

<a name="nimbleclient.v1.api.volumes.Volume.associate"></a>
#### associate

```python
 | associate(volcoll)
```

Associate the volume to a volume_collection.

<a name="nimbleclient.v1.api.volumes.Volume.dissociate"></a>
#### dissociate

```python
 | dissociate()
```

Dissociate the volume from a volume collection.

<a name="nimbleclient.v1.api.volumes.VolumeList"></a>
## VolumeList

```python
class VolumeList(Collection)
```

<a name="nimbleclient.v1.api.volumes.VolumeList.restore"></a>
#### restore

```python
 | restore(id, base_snap_id, **kwargs)
```

Restore volume data from a previous snapshot.

__Parameters__

- __id           __: ID of the restored volume.
- __base_snap_id __: ID of the snapshot to which this the volume is restored.

<a name="nimbleclient.v1.api.volumes.VolumeList.move"></a>
#### move

```python
 | move(id, dest_pool_id, **kwargs)
```

Move a volume and its related volumes to another pool. To change a single volume's folder assignment (while remaining in the same pool), use a volume update operation to
change the folder_id attribute.

__Parameters__

- __id           __: ID of the volume to move.
- __dest_pool_id __: ID of the destination pool or folder. Specify a pool ID when the volumes should not be in a folder; otherwise, specify a folder ID and the pool will be
               derived from the folder.
- __force_vvol   __: Forcibly move a Virtual Volume. Moving Virtual Volume is disruptive to the vCenter, hence it should only be done by the VASA Provider (VP). This flag should
               only be set by the VP when it calls this API.

<a name="nimbleclient.v1.api.volumes.VolumeList.bulk_move"></a>
#### bulk\_move

```python
 | bulk_move(dest_pool_id, vol_ids, **kwargs)
```

Move volumes and their related volumes to another pool. To change a single volume's folder assignment (while remaining in the same pool), use a volume update operation to
change the folder_id attribute.

__Parameters__

- __vol_ids      __: IDs of the volumes to move.
- __dest_pool_id __: ID of the destination pool or folder. Specify a pool ID when the volumes should not be in a folder; otherwise, specify a folder ID and the pool will be
               derived from the folder.
- __force_vvol   __: Forcibly move a Virtual Volume. Moving Virtual Volume is disruptive to the vCenter, hence it should only be done by the VASA Provider (VP). This flag should
               only be set by the VP when it calls this API.

<a name="nimbleclient.v1.api.volumes.VolumeList.abort_move"></a>
#### abort\_move

```python
 | abort_move(id, **kwargs)
```

Abort the in-progress move of the specified volume to another pool.

__Parameters__

- __id __: ID of the volume to stop moving to a different pool.

<a name="nimbleclient.v1.api.volumes.VolumeList.bulk_set_dedupe"></a>
#### bulk\_set\_dedupe

```python
 | bulk_set_dedupe(dedupe_enabled, vol_ids, **kwargs)
```

Enable or disable dedupe on a list of volumes. If the volumes are not dedupe capable, the operation will fail for the specified volume.

__Parameters__

- __vol_ids        __: IDs of the volumes to enable/disable dedupe.
- __dedupe_enabled __: Dedupe property to be applied to the list of volumes.

<a name="nimbleclient.v1.api.volumes.VolumeList.bulk_set_online_and_offline"></a>
#### bulk\_set\_online\_and\_offline

```python
 | bulk_set_online_and_offline(online, vol_ids, **kwargs)
```

Bring a list of volumes online or offline.

__Parameters__

- __vol_ids __: IDs of the volumes to set online or offline.
- __online  __: Desired state of the volumes. "true" for online, "false" for offline.

<a name="nimbleclient.v1.api.volumes.VolumeList.online"></a>
#### online

```python
 | online(id)
```

Bring volume online.

__Parameters__

- __id __: ID of the volume.

<a name="nimbleclient.v1.api.volumes.VolumeList.offline"></a>
#### offline

```python
 | offline(id)
```

Take volume offline.

__Parameters__

- __id __: ID of the volume.

<a name="nimbleclient.v1.api.volumes.VolumeList.associate"></a>
#### associate

```python
 | associate(id, volcoll)
```

Associate the volume to a volume_collection

__Parameters__

- __id __: ID of the volume.

<a name="nimbleclient.v1.api.volumes.VolumeList.dissociate"></a>
#### dissociate

```python
 | dissociate(id)
```

Dissociate the volume from a volume collection

__Parameters__

- __id __: ID of the volume.

