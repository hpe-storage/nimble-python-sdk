# Table of Contents

* [nimbleclient.v1.api.snapshot\_collections](#nimbleclient.v1.api.snapshot_collections)
  * [SnapshotCollection](#nimbleclient.v1.api.snapshot_collections.SnapshotCollection)

<a name="nimbleclient.v1.api.snapshot_collections"></a>
# nimbleclient.v1.api.snapshot\_collections

<a name="nimbleclient.v1.api.snapshot_collections.SnapshotCollection"></a>
## SnapshotCollection

```python
class SnapshotCollection(Resource)
```

Snapshot collections are collections of scheduled snapshots that are taken from volumes sharing a volume collection. Snapshot collections are replicated in the order that the
collections were taken.

__Parameters__

- __id                         __: Identifier for snapshot collection.
- __name                       __: Name of snapshot collection.
- __description                __: Text description of snapshot collection.
- __volcoll_name               __: Volume collection name.
- __volcoll_id                 __: Parent volume collection ID.
- __origin_name                __: Origination group name/ID.
- __is_replica                 __: Indicates if snapshot collection was created as a replica.
- __srep_owner_name            __: Name of the partner where the snapshots in this snapshot collection reside.
- __srep_owner_id              __: ID of the partner where snapshots for this snapshot collection reside which were created by synchronous replication. Field will be null if no peer
                             snapshot_collection was created by synchronous replication.
- __peer_snapcoll_id           __: ID of the peer snapshot collection created by synchronous replication. Field will be null if no peer snapshot_collection was created by
                             synchronous replication.
- __num_snaps                  __: Current number of live, non-hidden snaps in this collection.
- __is_complete                __: Is complete.
- __is_manual                  __: Is manual.
- __is_external_trigger        __: Is externally triggered.
- __is_unmanaged               __: Indicates whether a snapshot collection is unmanaged. This is based on the state of individual snapshots.
- __is_manually_managed        __: Indicates whether a snapshot collection is managed.
- __repl_status                __: Replication status.
- __repl_start_time            __: Replication start time.
- __repl_complete_time         __: Replication complete time.
- __repl_bytes_transferred     __: Number of bytes transferred after replication completes.
- __creation_time              __: Time when this snapshot collection was created.
- __last_modified              __: Time when this snapshot collection was last modified.
- __online_status              __: Online status of snapcoll. This is based on the online status of the individual snapshots.
- __vol_snap_attr_list         __: List of snapshot attributes for snapshots being created as part of snapshot collection creation.
- __snapshots_list             __: List of snapshots in the snapshot collection.
- __replicate                  __: True if this snapshot collection has been marked for replication. This attribute cannot be updated for synchronous replication.
- __replicate_to               __: Specifies the partner name that the snapshots in this snapshot collection are replicated to.
- __start_online               __: Start with snapshot set online.
- __allow_writes               __: Allow applications to write to created snapshot(s). Mandatory and must be set to 'true' for VSS application synchronized snapshots.
- __disable_appsync            __: Do not perform application synchronization for this snapshot, create a crash-consistent snapshot instead.
- __snap_verify                __: Run verification tool on this snapshot. This option can only be used with a volume collection that has application synchronization.
- __skip_db_consistency_check  __: Skip consistency check for database files on this snapshot. This option only applies to volume collections with application synchronization set to
                             VSS, application ID set to MS Exchange 2010 or later with Database Availability Group (DAG), snap_verify option set to true, and disable_appsync
                             option set to false.
- __sched_id                   __: ID of protection schedule of snapshot collection.
- __sched_name                 __: Name of protection schedule of snapshot collection.
- __invoke_on_upstream_partner __: Invoke snapshot request on upstream partner. This operation is not supported for synchronous replication volume vollections.
- __agent_type                 __: External management agent type for snapshots being created as part of snapshot collection.
- __expiry_after               __: Number of seconds after which this snapcoll is considered expired by the snapshot TTL. A value of 0 indicates that the snapshot never expires, 1
                             indicates that the snapshot uses a group-level configured TTL value and any other value indicates the number of seconds.
- __metadata                   __: Key-value pairs that augment a snapshot collection's attributes.
- __force                      __: Forcibly delete the specified snapshot collection even if it is the last replicated snapshot. Doing so could lead to full re-seeding at the next
                             replication.

