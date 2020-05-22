
# nimbleclient.v1.api.replication_partners


## ReplicationPartner
```python
ReplicationPartner(self, id, attrs=None, client=None, collection=None)
```
Manage replication partner. Replication partners let one storage array talk to another for replication purposes. The two arrays must be able to communicate over a network, and
use ports 4213 and 4214. Replication partners have the same name as the remote group. Replication partners can be reciprocal, upstream (the source of replicas), or downstream
(the receiver of replicas) partners.

__Parameters__

- __id                               __: Identifier for a replication partner.
- __name                             __: Name of replication partner.
- __full_name                        __: Fully qualified name of replication partner.
- __search_name                      __: Name of replication partner used for object search.
- __description                      __: Description of replication partner.
- __partner_type                     __: Replication partner type. Possible values are group or pool.
- __alias                            __: Name this group uses to identify itself to this partner.
- __secret                           __: Replication partner shared secret, used for mutual authentication of the partners.
- __creation_time                    __: Time when this replication partner was created.
- __last_modified                    __: Time when this replication partner was last modified.
- __control_port                     __: Port number of partner control interface.
- __hostname                         __: IP address or hostname of partner interface.  This must be the partner's Group Management IP address.
- __port_range_start                 __: For tunnel_endpoint partner types, first port available on the ssh proxy available for reverse forwarding. It must be guaranteed that the
                                   proxy has the next N ports reserved for this partner, where N is the count of DSDs in this group. This attribute is only valid for
                                   tunnel_endpoint partner type.
- __proxy_hostname                   __: IP address of tunnel endpoint. Only valid for tunnel_endpoint partner types.
- __proxy_user                       __: User to authenticate with tunnel endpoint. Only valid for tunnel_endpoint partner types.
- __repl_hostname                    __: IP address or hostname of partner data interface.
- __data_port                        __: Port number of partner data interface.
- __is_alive                         __: Whether the partner is available, and responding to pings.
- __partner_group_uid                __: Replication partner group uid.
- __last_keepalive_error             __: Most recent error while attempting to ping the partner.
- __cfg_sync_status                  __: Indicates whether all volumes and volume collections have been synced to the partner.
- __last_sync_error                  __: Most recent error seen while attempting to sync objects to the partner.
- __array_serial                     __: Serial number of group leader array of the partner.
- __version                          __: Replication version of the partner.
- __pool_id                          __: The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are
                                   always created in the same pool as their parent volume.
- __pool_name                        __: The pool name where volumes replicated from this partner will be created.
- __folder_id                        __: The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners.
- __folder_name                      __: The Folder name within the pool where volumes replicated from this partner will be created.
- __match_folder                     __: Indicates whether to match the upstream volume's folder on the downstream.
- __paused                           __: Indicates whether replication traffic from/to this partner has been halted.
- __unique_name                      __: Indicates whether this partner actively mangles object names to avoid name conflicts during replication.
- __subnet_label                     __: Label of the subnet used to replicate to this partner.
- __subnet_type                      __: Type of the subnet used to replicate to this partner.
- __throttles                        __: Throttles used while replicating from/to this partner.
- __throttled_bandwidth              __: Current bandwidth throttle for this partner, expressed either as megabits per second or as the largest possible 64-bit signed integer
                                   (9223372036854775807) to indicate that there is no throttle. This attribute is superseded by throttled_bandwidth_current.
- __throttled_bandwidth_current      __: Current bandwidth throttle for this partner, expressed either as megabits per second or as -1 to indicate that there is no throttle.
- __throttled_bandwidth_kbps         __: Current bandwidth throttle for this partner, expressed either as kilobits per second or as the largest possible 64-bit signed integer
                                   (9223372036854775807) to indicate that there is no throttle. This attribute is superseded by throttled_bandwidth_current_kbps.
- __throttled_bandwidth_current_kbps __: Current bandwidth throttle for this partner, expressed either as kilobits per second or as -1 to indicate that there is no throttle.
- __subnet_network                   __: Subnet used to replicate to this partner.
- __subnet_netmask                   __: Subnet mask used to replicate to this partner.
- __volume_collection_list           __: List of volume collections that are replicating from/to this partner.
- __volume_collection_list_count     __: Count of volume collections that are replicating from/to this partner.
- __volume_list                      __: List of volumes that are replicating from/to this partner.
- __volume_list_count                __: Count of volumes that are replicating from/to this partner.
- __replication_direction            __: Direction of replication configured with this partner.


## ReplicationPartnerList
```python
ReplicationPartnerList(self, client=None)
```

