# Table of Contents

* [nimbleclient.v1.api.snapshots](#nimbleclient.v1.api.snapshots)
  * [Snapshot](#nimbleclient.v1.api.snapshots.Snapshot)
    * [bulk\_create](#nimbleclient.v1.api.snapshots.Snapshot.bulk_create)
  * [SnapshotList](#nimbleclient.v1.api.snapshots.SnapshotList)
    * [bulk\_create](#nimbleclient.v1.api.snapshots.SnapshotList.bulk_create)

<a name="nimbleclient.v1.api.snapshots"></a>
# nimbleclient.v1.api.snapshots

<a name="nimbleclient.v1.api.snapshots.Snapshot"></a>
## Snapshot

```python
class Snapshot(Resource)
```

Snapshots are point-in-time copies of a volume. Snapshots are managed the same way you manage volumes. In reality, snapshots are volumes: they can be accessed by initiators,
are subject to the same controls, can be modified, and have the same restrictions as volumes. Snapshots can be cloned and replicated. The initial snapshot uses no space: it
shares the original data with the source volume. Each successive snapshot captures the changes that have occurred on the volume. The changed blocks are compressed.

__Parameters__

- __id                          __: Identifier for the snapshot.
- __name                        __: Name of snapshot.
- __description                 __: Text description of snapshot.
- __size                        __: Size of volume at time of snapshot (in bytes).
- __vol_name                    __: Name of the parent volume in which the snapshot belongs to.
- __pool_name                   __: Name of the pool in which the parent volume belongs to.
- __vol_id                      __: Parent volume ID.
- __snap_collection_name        __: Name of snapshot collection.
- __snap_collection_id          __: Identifier of snapshot collection.
- __online                      __: Online state for a snapshot means it could be mounted for data restore.
- __writable                    __: Allow snapshot to be writable. Mandatory and must be set to 'true' for VSS application synchronized snapshots.
- __offline_reason              __: Snapshot offline reason - possible entries: one of 'user', 'recovery', 'replica', 'over_volume_limit', 'over_snapshot_limit',
                              'over_volume_reserve', 'nvram_loss_recovery', 'pool_free_space_exhausted' .
- __expiry_time                 __: Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never
                              expires.
- __expiry_after                __: Number of seconds after which this snapshot is considered expired by snapshot TTL. A value of 0 indicates that snapshot never expires, 1
                              indicates that snapshot uses group-level configured TTL value and any other value indicates number of seconds.
- __origin_name                 __: Origination group name.
- __is_replica                  __: Snapshot is a replica from upstream replication partner.
- __is_unmanaged                __: Indicates whether the snapshot is unmanaged. The snapshot will not be deleted automatically unless the unmanaged cleanup feature is enabled.
- __is_manually_managed         __: Is snapshot manually managed, i.e., snapshot is manually or third party created or created by system at the time of volume restore or resize.
- __replication_status          __: Replication status.
- __access_control_records      __: List of access control records that apply to this snapshot.
- __serial_number               __: Identifier for the SCSI protocol.
- __target_name                 __: The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target snapshot.
- __creation_time               __: Time when this snapshot was created.
- __last_modified               __: Time when this snapshort was last modified.
- __schedule_name               __: Name of protection schedule.
- __schedule_id                 __: Identifier of protection schedule.
- __app_uuid                    __: Application identifier of snapshots.
- __metadata                    __: Key-value pairs that augment a snapshot's attributes.
- __new_data_valid              __: Indicate the usage infomation is valid.
- __new_data_compressed_bytes   __: The bytes of compressed new data.
- __new_data_uncompressed_bytes __: The bytes of uncompressed new data.
- __agent_type                  __: External management agent type.
- __vpd_t10                     __: The snapshot's T10 Vendor ID-based identifier.
- __vpd_ieee0                   __: The first 64 bits of the snapshots's EUI-64 identifier, encoded as a hexadecimal string.
- __vpd_ieee1                   __: The last 64 bits of the snapshots's EUI-64 identifier, encoded as a hexadecimal string.
- __force                       __: Forcibly delete the specified snapshot even if it is the last replicated collection. Doing so could lead to full re-seeding at the next
                              replication.

<a name="nimbleclient.v1.api.snapshots.Snapshot.bulk_create"></a>
#### bulk\_create

```python
 | bulk_create(replicate, snap_vol_list, vss_snap, **kwargs)
```

Create snapshots on the given set of volumes.

__Parameters__

- __snap_vol_list __: List of volumes to snapshot and corresponding snapshot creation attributes. VSS application-synchronized snapshot must specify the 'writable' parameter and
                set it to true.
- __replicate     __: Allow snapshot to be replicated.
- __vss_snap      __: VSS app-synchronized snapshot; we don't support creation of non app-synchronized sanpshots through this interface; must be set to true.

<a name="nimbleclient.v1.api.snapshots.SnapshotList"></a>
## SnapshotList

```python
class SnapshotList(Collection)
```

<a name="nimbleclient.v1.api.snapshots.SnapshotList.bulk_create"></a>
#### bulk\_create

```python
 | bulk_create(replicate, snap_vol_list, vss_snap, **kwargs)
```

Create snapshots on the given set of volumes.

__Parameters__

- __snap_vol_list __: List of volumes to snapshot and corresponding snapshot creation attributes. VSS application-synchronized snapshot must specify the 'writable' parameter and
                set it to true.
- __replicate     __: Allow snapshot to be replicated.
- __vss_snap      __: VSS app-synchronized snapshot; we don't support creation of non app-synchronized sanpshots through this interface; must be set to true.

