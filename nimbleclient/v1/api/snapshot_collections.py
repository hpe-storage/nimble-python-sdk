#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class SnapshotCollection(Resource):
    '''
    Snapshot collections are collections of scheduled snapshots that are taken from volumes sharing a volume collection. Snapshot collections are replicated in the order that the
    collections were taken.

    Parameters:
    - id                         : Identifier for snapshot collection.
    - name                       : Name of snapshot collection.
    - description                : Text description of snapshot collection.
    - volcoll_name               : Volume collection name.
    - volcoll_id                 : Parent volume collection ID.
    - origin_name                : Origination group name/ID.
    - is_replica                 : Indicates if snapshot collection was created as a replica.
    - srep_owner_name            : Name of the partner where the snapshots in this snapshot collection reside.
    - srep_owner_id              : ID of the partner where snapshots for this snapshot collection reside which were created by synchronous replication. Field will be null if no
                                   peer snapshot_collection was created by synchronous replication.
    - peer_snapcoll_id           : ID of the peer snapshot collection created by synchronous replication. Field will be null if no peer snapshot_collection was created by
                                   synchronous replication.
    - is_complete                : Is complete.
    - is_manual                  : Is manual.
    - is_external_trigger        : Is externally triggered.
    - is_unmanaged               : Indicates whether a snapshot collection is unmanaged. This is based on the state of individual snapshots.
    - is_manually_managed        : Indicates whether a snapshot collection is managed.
    - repl_status                : Replication status.
    - repl_start_time            : Replication start time.
    - repl_complete_time         : Replication complete time.
    - repl_bytes_transferred     : Number of bytes transferred after replication completes.
    - creation_time              : Time when this snapshot collection was created.
    - last_modified              : Time when this snapshot collection was last modified.
    - online_status              : Online status of snapcoll. This is based on the online status of the individual snapshots.
    - vol_snap_attr_list         : List of snapshot attributes for snapshots being created as part of snapshot collection creation.
    - snapshots_list             : List of snapshots in the snapshot collection.
    - replicate                  : True if this snapshot collection has been marked for replication. This attribute cannot be updated for synchronous replication.
    - replicate_to               : Specifies the partner name that the snapshots in this snapshot collection are replicated to.
    - start_online               : Start with snapshot set online.
    - allow_writes               : Allow applications to write to created snapshot(s). Mandatory and must be set to 'true' for VSS application synchronized snapshots.
    - disable_appsync            : Do not perform application synchronization for this snapshot, create a crash-consistent snapshot instead.
    - snap_verify                : Run verification tool on this snapshot. This option can only be used with a volume collection that has application synchronization.
    - skip_db_consistency_check  : Skip consistency check for database files on this snapshot. This option only applies to volume collections with application synchronization set
                                   to VSS, application ID set to MS Exchange 2010 or later with Database Availability Group (DAG), snap_verify option set to true, and
                                   disable_appsync option set to false.
    - sched_id                   : ID of protection schedule of snapshot collection.
    - sched_name                 : Name of protection schedule of snapshot collection.
    - invoke_on_upstream_partner : Invoke snapshot request on upstream partner. This operation is not supported for synchronous replication volume vollections.
    - agent_type                 : External management agent type for snapshots being created as part of snapshot collection.
    - expiry_after               : Number of seconds after which this snapcoll is considered expired by the snapshot TTL. A value of 0 indicates that the snapshot never expires, 1
                                   indicates that the snapshot uses a group-level configured TTL value and any other value indicates the number of seconds.
    - metadata                   : Key-value pairs that augment a snapshot collection's attributes.
    - force                      : Forcibly delete the specified snapshot collection even if it is the last replicated snapshot. Doing so could lead to full re-seeding at the next
                                   replication.
    '''


class SnapshotCollectionList(Collection):
    resource = SnapshotCollection
    resource_type = "snapshot_collections"
