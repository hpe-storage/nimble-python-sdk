
# nimbleclient.v1.api.volume_collections


## VolumeCollection
```python
VolumeCollection(self, id, attrs=None, client=None, collection=None)
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
- __app_id                        __: Application ID running on the server. Application ID can only be specified if application synchronization is \"vss\".
- __app_cluster_name              __: If the application is running within a Windows cluster environment, this is the cluster name.
- __app_service_name              __: If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster
                                environment.
- __vcenter_hostname              __: VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \":\".
- __vcenter_username              __: Application VMware vCenter username.
- __vcenter_password              __: Application VMware vCenter password.
- __agent_hostname                __: Generic backup agent hostname. Custom port number can be specified with agent hostname using \":\".
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


## VolumeCollectionList
```python
VolumeCollectionList(self, client=None)
```

