# Table of Contents

* [nimbleclient.v1.api.protection\_schedules](#nimbleclient.v1.api.protection_schedules)
  * [ProtectionSchedule](#nimbleclient.v1.api.protection_schedules.ProtectionSchedule)

<a name="nimbleclient.v1.api.protection_schedules"></a>
# nimbleclient.v1.api.protection\_schedules

<a name="nimbleclient.v1.api.protection_schedules.ProtectionSchedule"></a>
## ProtectionSchedule

```python
class ProtectionSchedule(Resource)
```

Manage protection schedules used in protection templates.

__Parameters__

- __id                                  __: Identifier for protection schedule.
- __name                                __: Name of snapshot schedule to create.
- __description                         __: Description of the schedule.
- __volcoll_or_prottmpl_type            __: Type of the protection policy this schedule is attached to. Valid values are protection_template and volume_collection.
- __volcoll_or_prottmpl_id              __: Identifier of the protection policy (protection_template or volume_collection) in which this protection schedule is attached to.
- __period                              __: Repeat interval for snapshots with respect to the period_unit.  For example, a value of 2 with the 'period_unit' of 'hours' results in
                                      one snapshot every 2 hours.
- __period_unit                         __: Time unit over which to take the number of snapshots specified in 'period'. For example, a value of 'days' with a 'period' of '1' results
                                      in one snapshot every day.
- __at_time                             __: Time of day when snapshot should be taken. In case repeat frequency specifies more than one snapshot in a day then the until_time option
                                      specifies until what time of day to take snapshots.
- __until_time                          __: Time of day to stop taking snapshots. Applicable only when repeat frequency specifies more than one snapshot in a day.
- __days                                __: Specifies which days snapshots should be taken.
- __num_retain                          __: Number of snapshots to retain. If replication is enabled on this schedule the array will always retain the latest replicated snapshot,
                                      which may exceed the specified retention value. This is necessary to ensure efficient replication performance.
- __downstream_partner                  __: Specifies the partner name if snapshots created by this schedule should be replicated.
- __downstream_partner_name             __: Specifies the partner name if snapshots created by this schedule should be replicated.
- __downstream_partner_id               __: Specifies the partner ID if snapshots created by this schedule should be replicated. In an update operation, if snapshots should be
                                      replicated, set this attribute to the ID of the replication partner. If snapshots should not be replicated, set this attribute to the
                                      empty string.
- __upstream_partner_name               __: Specifies the partner name from which snapshots created by this schedule are replicated.
- __upstream_partner_id                 __: Specifies the partner ID from which snapshots created by this schedule are replicated.
- __replicate_every                     __: Specifies which snapshots should be replicated. If snapshots are replicated and this option is not specified, every snapshot is
                                      replicated.
- __num_retain_replica                  __: Number of snapshots to retain on the replica.
- __repl_alert_thres                    __: Replication alert threshold in seconds. If the replication of a snapshot takes more than this amount of time to complete an alert will be
                                      generated. Enter 0 to disable this alert.
- __snap_verify                         __: Run verification tool on snapshot created by this schedule. This option can only be used with snapshot schedules of a protection template
                                      that has application synchronization. The tool used to verify snapshot depends on the type of application. For example, if application
                                      synchronization is VSS and the application ID is Exchange, eseutil tool is run on the snapshots. If verification fails, the logs are not
                                      truncated.
- __skip_db_consistency_check           __: Skip consistency check for database files on snapshots created by this schedule. This option only applies to snapshot schedules of a
                                      protection template with application synchronization set to VSS, application ID set to MS Exchange 2010 or later w/DAG, this schedule's
                                      snap_verify option set to yes, and its disable_appsync option set to false. Skipping consistency checks is only recommended if each
                                      database in a DAG has multiple copies.
- __disable_appsync                     __: Disables application synchronized snapshots and creates crash consistent snapshots instead.
- __schedule_type                       __: Normal schedules have internal timers which drive snapshot creation. An externally driven schedule has no internal timers. All snapshot
                                      activity is driven by an external trigger. In other words, these schedules are used only for externally driven manual snapshots.
- __active                              __: A schedule is active only if it is owned by the same owner as the volume collection. Only active schedules of a volume collection
                                      participate in the creation of snapshots and replication.
- __creation_time                       __: Time when this protection schedule was created.
- __last_modified                       __: Time when this protection schedule was last modified.
- __last_mod_sched_time                 __: Time when the timing of the protection schedule was last modified.
- __last_replicated_snapcoll_name       __: Specifies the name of last replicated snapshot collection.
- __last_replicated_snapcoll_id         __: Specifies the snapshot collection ID of last replicated snapshot collection.
- __last_replicated_at_time             __: Time when last snapshot collection was replicated.
- __last_snap_time                      __: Time when last snapshot was taken.
- __next_snap_time                      __: Time when next snapshot will be taken.
- __next_repl_snap_time                 __: Time when next snapshot will be replicated.
- __snap_counter                        __: This is only used by custom read handler for internal calculations.
- __sched_owner_id                      __: Identifier of the group that owns this schedule.
- __sched_owner_name                    __: Name of the group that owns this schedule.
- __last_config_change_time             __: The last timing configutation changed.
- __currently_replicating_snapcoll_name __: The name of the currently replicating snapshot collection if one exists, the empty string otherwise.
- __vol_status_list                     __: The list of the replication status of volumes undergoing replication.
- __sync_repl_vol_status_list           __: A list of the replication status of volumes undergoing synchronous replication.
- __use_downstream_for_DR               __: Break synchronous replication for the specified volume collection and present downstream volumes to host(s). Downstream volumes in the
                                      volume collection will be set to online and presented to the host(s) using new serial and LUN numbers. No changes will be made to the
                                      upstream volumes, their serial and LUN numbers, and their online state. The existing ACLs on the upstream volumes will be copied to the
                                      downstream volumes. Use this in conjunction with an empty downstream_partner_id. This unconfigures synchronous replication when the
                                      partner is removed from the last replicating schedule in the specified volume collection and presents the downstream volumes to host(s).
                                      Host(s) will need to be configured to access the new volumes with the newly assigned serial and LUN numbers. Use this option to expose
                                      downstream volumes in a synchronously replicated volume collection to host(s) only when the upstream partner is confirmed to be down and
                                      there is no communication between partners. Do not execute this operation if a previous Group Management Service takeover has been
                                      performed on a different array. Do not perform a subsequent Group Management Service takeover on a different array as it will lead to
                                      irreconcilable conflicts. This limitation is cleared once the Group management service backup array has successfully synchronized after
                                      reconnection.

