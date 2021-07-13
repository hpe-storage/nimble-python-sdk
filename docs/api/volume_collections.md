# Table of Contents

* [nimbleclient.v1.api.volume\_collections](#nimbleclient.v1.api.volume_collections)
  * [VolumeCollection](#nimbleclient.v1.api.volume_collections.VolumeCollection)
    * [promote](#nimbleclient.v1.api.volume_collections.VolumeCollection.promote)
    * [demote](#nimbleclient.v1.api.volume_collections.VolumeCollection.demote)
    * [handover](#nimbleclient.v1.api.volume_collections.VolumeCollection.handover)
    * [abort\_handover](#nimbleclient.v1.api.volume_collections.VolumeCollection.abort_handover)
    * [validate](#nimbleclient.v1.api.volume_collections.VolumeCollection.validate)
  * [VolumeCollectionList](#nimbleclient.v1.api.volume_collections.VolumeCollectionList)
    * [promote](#nimbleclient.v1.api.volume_collections.VolumeCollectionList.promote)
    * [demote](#nimbleclient.v1.api.volume_collections.VolumeCollectionList.demote)
    * [handover](#nimbleclient.v1.api.volume_collections.VolumeCollectionList.handover)
    * [abort\_handover](#nimbleclient.v1.api.volume_collections.VolumeCollectionList.abort_handover)
    * [validate](#nimbleclient.v1.api.volume_collections.VolumeCollectionList.validate)

<a name="nimbleclient.v1.api.volume_collections"></a>
# nimbleclient.v1.api.volume\_collections

<a name="nimbleclient.v1.api.volume_collections.VolumeCollection"></a>
## VolumeCollection

```python
class VolumeCollection(Resource)
```

Manage volume collections. Volume collections are logical groups of volumes that share protection characteristics such as snapshot and replication schedules. Volume
collections can be created from scratch or based on predefined protection templates.

__Parameters__

- __id                            __: Identifier for volume collection.
- __prottmpl_id                   __: Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input
                                when creating a volume collection and is not outputed.
- __name                          __: Name of volume collection.
- __full_name                     __: Fully qualified name of volume collection.
- __search_name                   __: Name of volume collection used for object search.
- __description                   __: Text description of volume collection.
- __repl_priority                 __: Replication priority for the volume collection with the following choices: {normal | high}.
- __pol_owner_name                __: Owner group.
- __replication_type              __: Type of replication configured for the volume collection.
- __synchronous_replication_type  __: Type of synchronous replication configured for the volume collection.
- __synchronous_replication_state __: State of synchronous replication on the volume collection.
- __app_sync                      __: Application Synchronization.
- __app_server                    __: Application server hostname.
- __app_id                        __: Application ID running on the server. Application ID can only be specified if application synchronization is \\"vss\\".
- __app_cluster_name              __: If the application is running within a Windows cluster environment, this is the cluster name.
- __app_service_name              __: If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster
                                environment.
- __vcenter_hostname              __: VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\":\\".
- __vcenter_username              __: Application VMware vCenter username.
- __vcenter_password              __: Application VMware vCenter password.
- __agent_hostname                __: Generic backup agent hostname. Custom port number can be specified with agent hostname using \\":\\".
- __agent_username                __: Generic backup agent username.
- __agent_password                __: Generic backup agent password.
- __creation_time                 __: Time when this volume collection was created.
- __last_modified_time            __: Time when this volume collection was last modified.
- __volume_list                   __: List of volumes associated with the volume collection.
- __downstream_volume_list        __: List of downstream volumes associated with the volume collection.
- __upstream_volume_list          __: List of upstream volumes associated with the volume collection.
- __volume_count                  __: Count of volumes associated with the volume collection.
- __cache_pinned_volume_list      __: List of cache pinned volumes associated with volume collection.
- __last_snapcoll                 __: Last snapshot collection on this volume collection.
- __snapcoll_count                __: Count of snapshot collections associated with volume collection.
- __schedule_list                 __: List of snapshot schedules associated with volume collection.
- __replication_partner           __: Replication partner for this volume collection.
- __last_replicated_snapcoll      __: Last replicated snapshot collection on this volume collection.
- __last_replicated_snapcoll_list __: List of snapshot collection information for the last replicated snapshot collection per schedule.
- __protection_type               __: Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup.
- __lag_time                      __: Replication lag time for volume collection.
- __is_standalone_volcoll         __: Indicates whether this is a standalone volume collection.
- __total_repl_bytes              __: Total size of volumes to be replicated for this volume collection.
- __repl_bytes_transferred        __: Total size of volumes replicated for this volume collection.
- __is_handing_over               __: Indicates whether a handover operation is in progress on this volume collection.
- __handover_replication_partner  __: Replication partner to which ownership is being transferred as part of handover operation.
- __metadata                      __: Key-value pairs that augment a volume collection's attributes.
- __srep_last_sync                __: Time when a synchronously replicated volume collection was last synchronized.
- __srep_resync_percent           __: Percentage of the resync progress for a synchronously replicated volume collection.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollection.promote"></a>
#### promote

```python
 | promote(**kwargs)
```

Take ownership of the specified volume collection. The volumes associated with the volume collection will be set to online and be available for reading and writing.
Replication will be disabled on the affected schedules and must be re-configured if desired. Snapshot retention for the affected schedules will be set to the greater of
the current local or replica retention values. This operation is not supported for synchronous replication volume collections.

__Parameters__

- __id __: ID of the promoted volume collection.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollection.demote"></a>
#### demote

```python
 | demote(replication_partner_id, **kwargs)
```

Release ownership of the specified volume collection. The volumes associated with the volume collection will set to offline and a snapshot will be created, then full
control over the volume collection will be transferred to the new owner. This option can be used following a promote to revert the volume collection back to its prior
configured state. This operation does not alter the configuration on the new owner itself, but does require the new owner to be running in order to obtain its identity
information. This operation is not supported for synchronous replication volume collections.

__Parameters__

- __id                         __: ID of the demoted volume collection.
- __replication_partner_id     __: ID of the new owner. If invoke_on_upstream_partner is provided, utilize the ID of the current owner i.e. upstream replication partner.
- __invoke_on_upstream_partner __: Invoke demote request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollection.handover"></a>
#### handover

```python
 | handover(replication_partner_id, **kwargs)
```

Gracefully transfer ownership of the specified volume collection. This action can be used to pass control of the volume collection to the downstream replication partner.
Ownership and full control over the volume collection will be given to the downstream replication partner. The volumes associated with the volume collection will be set to
offline prior to the final snapshot being taken and replicated, thus ensuring full data synchronization as part of the transfer. By default, the new owner will
automatically begin replicating the volume collection back to this node when the handover completes.

__Parameters__

- __id                         __: ID of the volume collection be handed over to the downstream replication partner.
- __replication_partner_id     __: ID of the new owner.
- __no_reverse                 __: Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the
- __volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default__: 'false'.
- __invoke_on_upstream_partner __: Invoke handover request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.
- __override_upstream_down     __: Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This
- __option is applicable for synchronous replication only. Default__: 'false'.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollection.abort_handover"></a>
#### abort\_handover

```python
 | abort_handover(**kwargs)
```

Abort in-progress handover. If for some reason a previously invoked handover request is unable to complete, this action can be used to cancel it. This operation is not
supported for synchronous replication volume collections.

__Parameters__

- __id __: ID of the volume collection on which to abort handover.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollection.validate"></a>
#### validate

```python
 | validate(**kwargs)
```

Validate a volume collection with either Microsoft VSS or VMware application synchronization.

__Parameters__

- __id __: ID of the volume collection that is to be validated.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollectionList"></a>
## VolumeCollectionList

```python
class VolumeCollectionList(Collection)
```

<a name="nimbleclient.v1.api.volume_collections.VolumeCollectionList.promote"></a>
#### promote

```python
 | promote(id, **kwargs)
```

Take ownership of the specified volume collection. The volumes associated with the volume collection will be set to online and be available for reading and writing.
Replication will be disabled on the affected schedules and must be re-configured if desired. Snapshot retention for the affected schedules will be set to the greater of
the current local or replica retention values. This operation is not supported for synchronous replication volume collections.

__Parameters__

- __id __: ID of the promoted volume collection.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollectionList.demote"></a>
#### demote

```python
 | demote(id, replication_partner_id, **kwargs)
```

Release ownership of the specified volume collection. The volumes associated with the volume collection will set to offline and a snapshot will be created, then full
control over the volume collection will be transferred to the new owner. This option can be used following a promote to revert the volume collection back to its prior
configured state. This operation does not alter the configuration on the new owner itself, but does require the new owner to be running in order to obtain its identity
information. This operation is not supported for synchronous replication volume collections.

__Parameters__

- __id                         __: ID of the demoted volume collection.
- __replication_partner_id     __: ID of the new owner. If invoke_on_upstream_partner is provided, utilize the ID of the current owner i.e. upstream replication partner.
- __invoke_on_upstream_partner __: Invoke demote request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollectionList.handover"></a>
#### handover

```python
 | handover(id, replication_partner_id, **kwargs)
```

Gracefully transfer ownership of the specified volume collection. This action can be used to pass control of the volume collection to the downstream replication partner.
Ownership and full control over the volume collection will be given to the downstream replication partner. The volumes associated with the volume collection will be set to
offline prior to the final snapshot being taken and replicated, thus ensuring full data synchronization as part of the transfer. By default, the new owner will
automatically begin replicating the volume collection back to this node when the handover completes.

__Parameters__

- __id                         __: ID of the volume collection be handed over to the downstream replication partner.
- __replication_partner_id     __: ID of the new owner.
- __no_reverse                 __: Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the
- __volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default__: 'false'.
- __invoke_on_upstream_partner __: Invoke handover request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.
- __override_upstream_down     __: Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This
- __option is applicable for synchronous replication only. Default__: 'false'.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollectionList.abort_handover"></a>
#### abort\_handover

```python
 | abort_handover(id, **kwargs)
```

Abort in-progress handover. If for some reason a previously invoked handover request is unable to complete, this action can be used to cancel it. This operation is not
supported for synchronous replication volume collections.

__Parameters__

- __id __: ID of the volume collection on which to abort handover.

<a name="nimbleclient.v1.api.volume_collections.VolumeCollectionList.validate"></a>
#### validate

```python
 | validate(id, **kwargs)
```

Validate a volume collection with either Microsoft VSS or VMware application synchronization.

__Parameters__

- __id __: ID of the volume collection that is to be validated.

