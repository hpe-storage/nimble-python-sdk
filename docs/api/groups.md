# Table of Contents

* [nimbleclient.v1.api.groups](#nimbleclient.v1.api.groups)
  * [Group](#nimbleclient.v1.api.groups.Group)
    * [reboot](#nimbleclient.v1.api.groups.Group.reboot)
    * [halt](#nimbleclient.v1.api.groups.Group.halt)
    * [test\_alert](#nimbleclient.v1.api.groups.Group.test_alert)
    * [software\_update\_precheck](#nimbleclient.v1.api.groups.Group.software_update_precheck)
    * [software\_update\_start](#nimbleclient.v1.api.groups.Group.software_update_start)
    * [software\_download](#nimbleclient.v1.api.groups.Group.software_download)
    * [software\_cancel\_download](#nimbleclient.v1.api.groups.Group.software_cancel_download)
    * [software\_update\_resume](#nimbleclient.v1.api.groups.Group.software_update_resume)
    * [get\_group\_discovered\_list](#nimbleclient.v1.api.groups.Group.get_group_discovered_list)
    * [validate\_merge](#nimbleclient.v1.api.groups.Group.validate_merge)
    * [merge](#nimbleclient.v1.api.groups.Group.merge)
    * [get\_eula](#nimbleclient.v1.api.groups.Group.get_eula)
    * [check\_migrate](#nimbleclient.v1.api.groups.Group.check_migrate)
    * [migrate](#nimbleclient.v1.api.groups.Group.migrate)
    * [get\_timezone\_list](#nimbleclient.v1.api.groups.Group.get_timezone_list)
  * [GroupList](#nimbleclient.v1.api.groups.GroupList)
    * [reboot](#nimbleclient.v1.api.groups.GroupList.reboot)
    * [halt](#nimbleclient.v1.api.groups.GroupList.halt)
    * [test\_alert](#nimbleclient.v1.api.groups.GroupList.test_alert)
    * [software\_update\_precheck](#nimbleclient.v1.api.groups.GroupList.software_update_precheck)
    * [software\_update\_start](#nimbleclient.v1.api.groups.GroupList.software_update_start)
    * [software\_download](#nimbleclient.v1.api.groups.GroupList.software_download)
    * [software\_cancel\_download](#nimbleclient.v1.api.groups.GroupList.software_cancel_download)
    * [software\_update\_resume](#nimbleclient.v1.api.groups.GroupList.software_update_resume)
    * [get\_group\_discovered\_list](#nimbleclient.v1.api.groups.GroupList.get_group_discovered_list)
    * [validate\_merge](#nimbleclient.v1.api.groups.GroupList.validate_merge)
    * [merge](#nimbleclient.v1.api.groups.GroupList.merge)
    * [get\_eula](#nimbleclient.v1.api.groups.GroupList.get_eula)
    * [check\_migrate](#nimbleclient.v1.api.groups.GroupList.check_migrate)
    * [migrate](#nimbleclient.v1.api.groups.GroupList.migrate)
    * [get\_timezone\_list](#nimbleclient.v1.api.groups.GroupList.get_timezone_list)

<a name="nimbleclient.v1.api.groups"></a>
# nimbleclient.v1.api.groups

<a name="nimbleclient.v1.api.groups.Group"></a>
## Group

```python
class Group(Resource)
```

Group is a collection of arrays operating together organized into storage pools.

__Parameters__

- __id                                     __: Identifier of the group.
- __name                                   __: Name of the group.
- __smtp_server                            __: Hostname or IP Address of SMTP Server.
- __smtp_port                              __: Port number of SMTP Server.
- __smtp_auth_enabled                      __: Whether SMTP Server requires authentication.
- __smtp_auth_username                     __: Username to authenticate with SMTP Server.
- __smtp_auth_password                     __: Password to authenticate with SMTP Server.
- __smtp_encrypt_type                      __: Level of encryption for SMTP. Requires use of SMTP Authentication if encryption is enabled.
- __autosupport_enabled                    __: Whether to send autosupport.
- __allow_analytics_gui                    __: Specify whether to allow HPE Nimble Storage to use Google Analytics in the GUI.  HPE Nimble Storage uses Google Analytics to gather
                                         data related to GUI usage.  The data gathered is used to evaluate and improve the product.
- __allow_support_tunnel                   __: Whether to allow support tunnel.
- __proxy_server                           __: Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings.
- __proxy_port                             __: Proxy Port of HTTP Proxy Server.
- __proxy_username                         __: Username to authenticate with HTTP Proxy Server.
- __proxy_password                         __: Password to authenticate with HTTP Proxy Server.
- __alert_to_email_addrs                   __: Comma-separated list of email addresss to receive emails.
- __send_alert_to_support                  __: Whether to send alert to Support.
- __alert_from_email_addr                  __: From email address to use while sending emails.
- __alert_min_level                        __: Minimum level of alert to be notified.
- __isns_enabled                           __: Whether iSNS is enabled.
- __isns_server                            __: Hostname or IP Address of iSNS Server.
- __isns_port                              __: Port number for iSNS Server.
- __snmp_trap_enabled                      __: Whether to enable SNMP traps.
- __snmp_trap_host                         __: Hostname or IP Address to send SNMP traps.
- __snmp_trap_port                         __: Port number of SNMP trap host.
- __snmp_get_enabled                       __: Whether to accept SNMP get commands.
- __snmp_community                         __: Community string to be used with SNMP.
- __snmp_get_port                          __: Port number to which SNMP get requests should be sent.
- __snmp_sys_contact                       __: Name of the SNMP administrator.
- __snmp_sys_location                      __: Location of the group.
- __domain_name                            __: Domain name for this group.
- __dns_servers                            __: IP addresses for this group's dns servers.
- __ntp_server                             __: Either IP address or hostname of the NTP server for this group.
- __timezone                               __: Timezone in which this group is located.
- __user_inactivity_timeout                __: The amount of time in seconds that the user session is inactive before timing out.
- __syslogd_enabled                        __: Is syslogd enabled on this system.
- __syslogd_server                         __: Hostname of the syslogd server.
- __syslogd_port                           __: Port number for syslogd server.
- __syslogd_servers                        __: Hostname and/or port of the syslogd servers.
- __vvol_enabled                           __: Are vvols enabled on this group.
- __iscsi_enabled                          __: Whether iSCSI is enabled on this group.
- __fc_enabled                             __: Whether FC is enabled on this group.
- __unique_name_enabled                    __: Are new volume and volume collection names transformed on this group.
- __access_protocol_list                   __: Protocol used to access this group.
- __group_target_enabled                   __: Is group_target enabled on this group.
- __default_iscsi_target_scope             __: Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target.
- __tdz_enabled                            __: Is Target Driven Zoning (TDZ) enabled on this group.
- __tdz_prefix                             __: Target Driven Zoning (TDZ) prefix for peer zones created by TDZ.
- __group_target_name                      __: Iscsi target name for this group.
- __default_volume_reserve                 __: Amount of space to reserve for a volume as a percentage of volume size.
- __default_volume_warn_level              __: Default threshold for volume space usage as a percentage of volume size above which an alert is raised.
- __default_volume_limit                   __: Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its
                                         limit.
- __default_snap_reserve                   __: Amount of space to reserve for snapshots of a volume as a percentage of volume size.
- __default_snap_warn_level                __: Default threshold for snapshot space usage of a volume as a percentage of volume size above which an alert is raised.
- __default_snap_limit                     __: This attribute is deprecated. The array does not limit a volume's snapshot space usage. The attribute is ignored on input and returns
                                         max int64 value on output.
- __default_snap_limit_percent             __: This attribute is deprecated. The array does not limit a volume's snapshot space usage. The attribute is ignored on input and returns
                                         -1 on output.
- __alarms_enabled                         __: Whether alarm feature is enabled.
- __vss_validation_timeout                 __: The amount of time in seconds to validate Microsoft VSS application synchronization before timing out.
- __auto_switchover_enabled                __: Whether automatic switchover of Group management services feature is enabled.
- __software_subscription_enabled          __: Whether software subscription of Group management services feature is enabled.
- __auto_switchover_messages               __: List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found.
- __merge_state                            __: State of group merge.
- __merge_group_name                       __: Group that we're being merged with.
- __tlsv1_enabled                          __: Enable or disable TLSv1.0 and TLSv1.1.
- __cc_mode_enabled                        __: Enable or disable Common Criteria mode.
- __group_snapshot_ttl                     __: Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL.
- __autoclean_unmanaged_snapshots_ttl_unit __: Unit for unmanaged snapshot time to live.
- __autoclean_unmanaged_snapshots_enabled  __: Whether autoclean unmanaged snapshots feature is enabled.
- __leader_array_name                      __: Name of the array where the group Management Service is running.
- __leader_array_serial                    __: Serial number of the array where the group Management Service is running.
- __management_service_backup_array_name   __: Name of the array where backup the group Management Service is running.
- __management_service_backup_status       __: HA status of the group Management Service.
- __failover_mode                          __: Failover mode of the group Management Service.
- __witness_status                         __: Witness status from group Management Service array and group Management Service backup array.
- __member_list                            __: Members of this group.
- __compressed_vol_usage_bytes             __: Compressed usage of volumes in the group.
- __compressed_snap_usage_bytes            __: Compressed usage of snapshots in the group.
- __uncompressed_vol_usage_bytes           __: Uncompressed usage of volumes in the group.
- __uncompressed_snap_usage_bytes          __: Uncompressed usage of snapshots in the group.
- __usable_capacity_bytes                  __: Usable capacity bytes of the group.
- __usage                                  __: Used space of the group in bytes.
- __raw_capacity                           __: Total capacity of the group.
- __usable_cache_capacity                  __: Usable cache capacity of the group.
- __raw_cache_capacity                     __: Total cache capacity of the group.
- __snap_usage_populated                   __: Total snapshot usage as if each snapshot is deep copy of the volume.
- __pending_deletes                        __: Usage for blocks that are not yet deleted.
- __num_connections                        __: Number of connections to the group.
- __vol_compression_ratio                  __: Compression ratio of volumes in the group.
- __snap_compression_ratio                 __: Compression ratio of snapshots in the group.
- __compression_ratio                      __: Compression savings for the group expressed as ratio.
- __dedupe_ratio                           __: Dedupe savings for the group expressed as ratio.
- __clone_ratio                            __: Clone savings for the group expressed as ratio.
- __vol_thin_provisioning_ratio            __: Thin provisioning savings for volumes in the group expressed as ratio.
- __savings_ratio                          __: Overall savings in the group expressed as ratio.
- __data_reduction_ratio                   __: Space savings in the group that does not include thin-provisioning savings expressed as ratio.
- __savings_dedupe                         __: Space usage savings in the group due to deduplication.
- __savings_compression                    __: Space usage savings in the group due to compression.
- __savings_clone                          __: Space usage savings in the group due to cloning of volumes.
- __savings_vol_thin_provisioning          __: Space usage savings in the group due to thin provisioning of volumes.
- __savings_data_reduction                 __: Space usage savings in the group that does not include thin-provisioning savings.
- __savings                                __: Overall space usage savings in the group.
- __free_space                             __: Free space of the pool in bytes.
- __unused_reserve_bytes                   __: Reserved space that is not utilized.
- __usage_valid                            __: Indicates whether the usage of group is valid.
- __space_info_valid                       __: Is space info for this group valid.
- __version_current                        __: Version of software running on the group.
- __version_target                         __: Desired software version for the group.
- __version_rollback                       __: Rollback software version for the group.
- __update_state                           __: Group update state.
- __update_start_time                      __: Start time of last update.
- __update_end_time                        __: End time of last update.
- __update_array_names                     __: Arrays in the group undergoing update.
- __update_progress_msg                    __: Group update detailed progress message.
- __update_error_code                      __: If the software update has failed, this indicates the error code corresponding to the failure.
- __update_downloading                     __: Is software update package currently downloading.
- __update_download_error_code             __: If the software download has failed, this indicates the error code corresponding to the failure.
- __update_download_start_time             __: Start time of last update.
- __update_download_end_time               __: End time of last update.
- __iscsi_automatic_connection_method      __: Is iscsi reconnection automatic.
- __iscsi_connection_rebalancing           __: Does iscsi automatically rebalance connections.
- __repl_throttled_bandwidth               __: Current bandwidth throttle for replication, expressed either as megabits per second or as -1 to indicate that there is no throttle.
- __repl_throttled_bandwidth_kbps          __: Current bandwidth throttle for replication, expressed either as kilobits per second or as -1 to indicate that there is no throttle.
- __repl_throttle_list                     __: All the replication bandwidth limits on the system.
- __volume_migration_status                __: Status of data migration activity related to volumes being relocated to different pools.
- __array_unassign_migration_status        __: Data migration status for arrays being removed from their pool.
- __data_rebalance_status                  __: Status of data rebalancing operations for pools in the group.
- __scsi_vendor_id                         __: SCSI vendor ID.
- __encryption_config                      __: How encryption is configured for this group.
- __last_login                             __: Time and user of last login to this group.
- __num_snaps                              __: Number of snapshots in the group.
- __num_snapcolls                          __: Number of snapshot collections in this group.
- __date                                   __: Unix epoch time local to the group.
- __login_banner_message                   __: The message for the login banner that is displayed during user login activity.
- __login_banner_after_auth                __: Should the banner be displayed before the user credentials are prompted or after prompting the user credentials.
- __login_banner_reset                     __: This will reset the banner to the version of the installed NOS. When login_banner_after_auth is specified, login_banner_reset can not
                                         be set to true.
- __snap_retn_meter_high                   __: Threshold for considering a volume as high retention.
- __snap_retn_meter_very_high              __: Threshold for considering a volume as very high retention.

<a name="nimbleclient.v1.api.groups.Group.reboot"></a>
#### reboot

```python
 | reboot(**kwargs)
```

Reboot all arrays in the group.

__Parameters__

- __id __: ID of the group to reboot.
- __job_timeout__: Job timeout in seconds.

<a name="nimbleclient.v1.api.groups.Group.halt"></a>
#### halt

```python
 | halt(**kwargs)
```

Halt all arrays in the group.

__Parameters__

- __id    __: ID of the group to halt.
- __force __: Halt remaining arrays when one or more is unreachable.
- __job_timeout__: Job timeout in seconds.

<a name="nimbleclient.v1.api.groups.Group.test_alert"></a>
#### test\_alert

```python
 | test_alert(level, **kwargs)
```

Generate a test alert.

__Parameters__

- __id    __: ID of the group.
- __level __: Level of the test alert.

<a name="nimbleclient.v1.api.groups.Group.software_update_precheck"></a>
#### software\_update\_precheck

```python
 | software_update_precheck(**kwargs)
```

Run software update precheck.

__Parameters__

- __id                 __: ID of the group.
- __skip_precheck_mask __: Flag to allow skipping certain types of prechecks.

<a name="nimbleclient.v1.api.groups.Group.software_update_start"></a>
#### software\_update\_start

```python
 | software_update_start(**kwargs)
```

Update the group software to the downloaded version.

__Parameters__

- __id                    __: ID of the group.
- __skip_start_check_mask __: Flag to allow skipping certain types of checks.

<a name="nimbleclient.v1.api.groups.Group.software_download"></a>
#### software\_download

```python
 | software_download(version, **kwargs)
```

Download software update package.

__Parameters__

- __id      __: ID of the group.
- __version __: Version string to download.
- __force   __: Flag to force download.

<a name="nimbleclient.v1.api.groups.Group.software_cancel_download"></a>
#### software\_cancel\_download

```python
 | software_cancel_download(**kwargs)
```

Cancel ongoing download of software.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.Group.software_update_resume"></a>
#### software\_update\_resume

```python
 | software_update_resume(**kwargs)
```

Resume stopped software update.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.Group.get_group_discovered_list"></a>
#### get\_group\_discovered\_list

```python
 | get_group_discovered_list(**kwargs)
```

Get list of discovered groups with arrays that are initialized.

__Parameters__

- __id         __: ID of the group.
- __group_name __: Name of the group requested to be discovered.

<a name="nimbleclient.v1.api.groups.Group.validate_merge"></a>
#### validate\_merge

```python
 | validate_merge(src_group_ip, src_group_name, src_password, src_username, **kwargs)
```

Perform group merge validation.

__Parameters__

- __id                     __: ID of the group.
- __src_group_name         __: Name of the source group.
- __src_group_ip           __: IP address of the source group.
- __src_username           __: Username of the source group.
- __src_password           __: Password of the source group.
- __src_passphrase         __: Source group encryption passphrase.
- __skip_secondary_mgmt_ip __: Skip check for secondary management IP address.

<a name="nimbleclient.v1.api.groups.Group.merge"></a>
#### merge

```python
 | merge(src_group_ip, src_group_name, src_password, src_username, **kwargs)
```

Perform group merge with the specified group.

__Parameters__

- __id                     __: ID of the group.
- __src_group_name         __: Name of the source group.
- __src_group_ip           __: IP address of the source group.
- __src_username           __: Username of the source group.
- __src_password           __: Password of the source group.
- __src_passphrase         __: Source group encryption passphrase.
- __force                  __: Ignore warnings and forcibly merge specified group with this group.
- __skip_secondary_mgmt_ip __: Skip check for secondary management IP address.
- __job_timeout            __: Job timeout in seconds.

<a name="nimbleclient.v1.api.groups.Group.get_eula"></a>
#### get\_eula

```python
 | get_eula(**kwargs)
```

Get URL to download EULA contents.

__Parameters__

- __id     __: ID of the group.
- __locale __: Locale of EULA contents. Default is en.
- __format __: Format of EULA contents. Default is HTML.
- __phase  __: Phase of EULA contents. Default is setup.
- __force  __: Flag to force EULA.

<a name="nimbleclient.v1.api.groups.Group.check_migrate"></a>
#### check\_migrate

```python
 | check_migrate(**kwargs)
```

Check if the group Management Service can be migrated to the group Management Service backup array.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.Group.migrate"></a>
#### migrate

```python
 | migrate(**kwargs)
```

Migrate the group Management Service to the current group Management Service backup array.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.Group.get_timezone_list"></a>
#### get\_timezone\_list

```python
 | get_timezone_list(**kwargs)
```

Get list of group timezones.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.GroupList"></a>
## GroupList

```python
class GroupList(Collection)
```

<a name="nimbleclient.v1.api.groups.GroupList.reboot"></a>
#### reboot

```python
 | reboot(id, **kwargs)
```

Reboot all arrays in the group.

__Parameters__

- __id __: ID of the group to reboot.
- __job_timeout__: Job timeout in seconds.

<a name="nimbleclient.v1.api.groups.GroupList.halt"></a>
#### halt

```python
 | halt(id, **kwargs)
```

Halt all arrays in the group.

__Parameters__

- __id    __: ID of the group to halt.
- __force __: Halt remaining arrays when one or more is unreachable.
- __job_timeout__: Job timeout in seconds.

<a name="nimbleclient.v1.api.groups.GroupList.test_alert"></a>
#### test\_alert

```python
 | test_alert(id, level, **kwargs)
```

Generate a test alert.

__Parameters__

- __id    __: ID of the group.
- __level __: Level of the test alert.

<a name="nimbleclient.v1.api.groups.GroupList.software_update_precheck"></a>
#### software\_update\_precheck

```python
 | software_update_precheck(id, **kwargs)
```

Run software update precheck.

__Parameters__

- __id                 __: ID of the group.
- __skip_precheck_mask __: Flag to allow skipping certain types of prechecks.

<a name="nimbleclient.v1.api.groups.GroupList.software_update_start"></a>
#### software\_update\_start

```python
 | software_update_start(id, **kwargs)
```

Update the group software to the downloaded version.

__Parameters__

- __id                    __: ID of the group.
- __skip_start_check_mask __: Flag to allow skipping certain types of checks.

<a name="nimbleclient.v1.api.groups.GroupList.software_download"></a>
#### software\_download

```python
 | software_download(id, version, **kwargs)
```

Download software update package.

__Parameters__

- __id      __: ID of the group.
- __version __: Version string to download.
- __force   __: Flag to force download.

<a name="nimbleclient.v1.api.groups.GroupList.software_cancel_download"></a>
#### software\_cancel\_download

```python
 | software_cancel_download(id, **kwargs)
```

Cancel ongoing download of software.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.GroupList.software_update_resume"></a>
#### software\_update\_resume

```python
 | software_update_resume(id, **kwargs)
```

Resume stopped software update.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.GroupList.get_group_discovered_list"></a>
#### get\_group\_discovered\_list

```python
 | get_group_discovered_list(id, **kwargs)
```

Get list of discovered groups with arrays that are initialized.

__Parameters__

- __id         __: ID of the group.
- __group_name __: Name of the group requested to be discovered.

<a name="nimbleclient.v1.api.groups.GroupList.validate_merge"></a>
#### validate\_merge

```python
 | validate_merge(id, src_group_ip, src_group_name, src_password, src_username, **kwargs)
```

Perform group merge validation.

__Parameters__

- __id                     __: ID of the group.
- __src_group_name         __: Name of the source group.
- __src_group_ip           __: IP address of the source group.
- __src_username           __: Username of the source group.
- __src_password           __: Password of the source group.
- __src_passphrase         __: Source group encryption passphrase.
- __skip_secondary_mgmt_ip __: Skip check for secondary management IP address.

<a name="nimbleclient.v1.api.groups.GroupList.merge"></a>
#### merge

```python
 | merge(id, src_group_ip, src_group_name, src_password, src_username, **kwargs)
```

Perform group merge with the specified group.

__Parameters__

- __id                     __: ID of the group.
- __src_group_name         __: Name of the source group.
- __src_group_ip           __: IP address of the source group.
- __src_username           __: Username of the source group.
- __src_password           __: Password of the source group.
- __src_passphrase         __: Source group encryption passphrase.
- __force                  __: Ignore warnings and forcibly merge specified group with this group.
- __skip_secondary_mgmt_ip __: Skip check for secondary management IP address.
- __job_timeout            __: Job timeout in seconds.

<a name="nimbleclient.v1.api.groups.GroupList.get_eula"></a>
#### get\_eula

```python
 | get_eula(id, **kwargs)
```

Get URL to download EULA contents.

__Parameters__

- __id     __: ID of the group.
- __locale __: Locale of EULA contents. Default is en.
- __format __: Format of EULA contents. Default is HTML.
- __phase  __: Phase of EULA contents. Default is setup.
- __force  __: Flag to force EULA.

<a name="nimbleclient.v1.api.groups.GroupList.check_migrate"></a>
#### check\_migrate

```python
 | check_migrate(id, **kwargs)
```

Check if the group Management Service can be migrated to the group Management Service backup array.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.GroupList.migrate"></a>
#### migrate

```python
 | migrate(id, **kwargs)
```

Migrate the group Management Service to the current group Management Service backup array.

__Parameters__

- __id __: ID of the group.

<a name="nimbleclient.v1.api.groups.GroupList.get_timezone_list"></a>
#### get\_timezone\_list

```python
 | get_timezone_list(id, **kwargs)
```

Get list of group timezones.

__Parameters__

- __id __: ID of the group.

