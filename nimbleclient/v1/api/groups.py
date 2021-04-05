#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection
from ...exceptions import NimOSAPIOperationUnsupported


class Group(Resource):
    """Group is a collection of arrays operating together organized into storage pools.

    # Parameters
    id                                     : Identifier of the group.
    name                                   : Name of the group.
    smtp_server                            : Hostname or IP Address of SMTP Server.
    smtp_port                              : Port number of SMTP Server.
    smtp_auth_enabled                      : Whether SMTP Server requires authentication.
    smtp_auth_username                     : Username to authenticate with SMTP Server.
    smtp_auth_password                     : Password to authenticate with SMTP Server.
    smtp_encrypt_type                      : Level of encryption for SMTP. Requires use of SMTP Authentication if encryption is enabled.
    autosupport_enabled                    : Whether to send autosupport.
    allow_analytics_gui                    : Specify whether to allow HPE Nimble Storage to use Google Analytics in the GUI.  HPE Nimble Storage uses Google Analytics to gather
                                             data related to GUI usage.  The data gathered is used to evaluate and improve the product.
    allow_support_tunnel                   : Whether to allow support tunnel.
    proxy_server                           : Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings.
    proxy_port                             : Proxy Port of HTTP Proxy Server.
    proxy_username                         : Username to authenticate with HTTP Proxy Server.
    proxy_password                         : Password to authenticate with HTTP Proxy Server.
    alert_to_email_addrs                   : Comma-separated list of email addresss to receive emails.
    send_alert_to_support                  : Whether to send alert to Support.
    alert_from_email_addr                  : From email address to use while sending emails.
    alert_min_level                        : Minimum level of alert to be notified.
    isns_enabled                           : Whether iSNS is enabled.
    isns_server                            : Hostname or IP Address of iSNS Server.
    isns_port                              : Port number for iSNS Server.
    snmp_trap_enabled                      : Whether to enable SNMP traps.
    snmp_trap_host                         : Hostname or IP Address to send SNMP traps.
    snmp_trap_port                         : Port number of SNMP trap host.
    snmp_get_enabled                       : Whether to accept SNMP get commands.
    snmp_community                         : Community string to be used with SNMP.
    snmp_get_port                          : Port number to which SNMP get requests should be sent.
    snmp_sys_contact                       : Name of the SNMP administrator.
    snmp_sys_location                      : Location of the group.
    domain_name                            : Domain name for this group.
    dns_servers                            : IP addresses for this group's dns servers.
    ntp_server                             : Either IP address or hostname of the NTP server for this group.
    timezone                               : Timezone in which this group is located.
    user_inactivity_timeout                : The amount of time in seconds that the user session is inactive before timing out.
    syslogd_enabled                        : Is syslogd enabled on this system.
    syslogd_server                         : Hostname of the syslogd server.
    syslogd_port                           : Port number for syslogd server.
    syslogd_servers                        : Hostname and/or port of the syslogd servers.
    vvol_enabled                           : Are vvols enabled on this group.
    iscsi_enabled                          : Whether iSCSI is enabled on this group.
    fc_enabled                             : Whether FC is enabled on this group.
    unique_name_enabled                    : Are new volume and volume collection names transformed on this group.
    access_protocol_list                   : Protocol used to access this group.
    group_target_enabled                   : Is group_target enabled on this group.
    default_iscsi_target_scope             : Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target.
    tdz_enabled                            : Is Target Driven Zoning (TDZ) enabled on this group.
    tdz_prefix                             : Target Driven Zoning (TDZ) prefix for peer zones created by TDZ.
    group_target_name                      : Iscsi target name for this group.
    default_volume_reserve                 : Amount of space to reserve for a volume as a percentage of volume size.
    default_volume_warn_level              : Default threshold for volume space usage as a percentage of volume size above which an alert is raised.
    default_volume_limit                   : Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its
                                             limit.
    default_snap_reserve                   : Amount of space to reserve for snapshots of a volume as a percentage of volume size.
    default_snap_warn_level                : Default threshold for snapshot space usage of a volume as a percentage of volume size above which an alert is raised.
    default_snap_limit                     : This attribute is deprecated. The array does not limit a volume's snapshot space usage. The attribute is ignored on input and returns
                                             max int64 value on output.
    default_snap_limit_percent             : This attribute is deprecated. The array does not limit a volume's snapshot space usage. The attribute is ignored on input and returns
                                             -1 on output.
    alarms_enabled                         : Whether alarm feature is enabled.
    vss_validation_timeout                 : The amount of time in seconds to validate Microsoft VSS application synchronization before timing out.
    auto_switchover_enabled                : Whether automatic switchover of Group management services feature is enabled.
    software_subscription_enabled          : Whether software subscription of Group management services feature is enabled.
    auto_switchover_messages               : List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found.
    merge_state                            : State of group merge.
    merge_group_name                       : Group that we're being merged with.
    tlsv1_enabled                          : Enable or disable TLSv1.0 and TLSv1.1.
    cc_mode_enabled                        : Enable or disable Common Criteria mode.
    group_snapshot_ttl                     : Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL.
    autoclean_unmanaged_snapshots_ttl_unit : Unit for unmanaged snapshot time to live.
    autoclean_unmanaged_snapshots_enabled  : Whether autoclean unmanaged snapshots feature is enabled.
    leader_array_name                      : Name of the array where the group Management Service is running.
    leader_array_serial                    : Serial number of the array where the group Management Service is running.
    management_service_backup_array_name   : Name of the array where backup the group Management Service is running.
    management_service_backup_status       : HA status of the group Management Service.
    failover_mode                          : Failover mode of the group Management Service.
    witness_status                         : Witness status from group Management Service array and group Management Service backup array.
    member_list                            : Members of this group.
    compressed_vol_usage_bytes             : Compressed usage of volumes in the group.
    compressed_snap_usage_bytes            : Compressed usage of snapshots in the group.
    uncompressed_vol_usage_bytes           : Uncompressed usage of volumes in the group.
    uncompressed_snap_usage_bytes          : Uncompressed usage of snapshots in the group.
    usable_capacity_bytes                  : Usable capacity bytes of the group.
    usage                                  : Used space of the group in bytes.
    raw_capacity                           : Total capacity of the group.
    usable_cache_capacity                  : Usable cache capacity of the group.
    raw_cache_capacity                     : Total cache capacity of the group.
    snap_usage_populated                   : Total snapshot usage as if each snapshot is deep copy of the volume.
    pending_deletes                        : Usage for blocks that are not yet deleted.
    num_connections                        : Number of connections to the group.
    vol_compression_ratio                  : Compression ratio of volumes in the group.
    snap_compression_ratio                 : Compression ratio of snapshots in the group.
    compression_ratio                      : Compression savings for the group expressed as ratio.
    dedupe_ratio                           : Dedupe savings for the group expressed as ratio.
    clone_ratio                            : Clone savings for the group expressed as ratio.
    vol_thin_provisioning_ratio            : Thin provisioning savings for volumes in the group expressed as ratio.
    savings_ratio                          : Overall savings in the group expressed as ratio.
    data_reduction_ratio                   : Space savings in the group that does not include thin-provisioning savings expressed as ratio.
    savings_dedupe                         : Space usage savings in the group due to deduplication.
    savings_compression                    : Space usage savings in the group due to compression.
    savings_clone                          : Space usage savings in the group due to cloning of volumes.
    savings_vol_thin_provisioning          : Space usage savings in the group due to thin provisioning of volumes.
    savings_data_reduction                 : Space usage savings in the group that does not include thin-provisioning savings.
    savings                                : Overall space usage savings in the group.
    free_space                             : Free space of the pool in bytes.
    unused_reserve_bytes                   : Reserved space that is not utilized.
    usage_valid                            : Indicates whether the usage of group is valid.
    space_info_valid                       : Is space info for this group valid.
    version_current                        : Version of software running on the group.
    version_target                         : Desired software version for the group.
    version_rollback                       : Rollback software version for the group.
    update_state                           : Group update state.
    update_start_time                      : Start time of last update.
    update_end_time                        : End time of last update.
    update_array_names                     : Arrays in the group undergoing update.
    update_progress_msg                    : Group update detailed progress message.
    update_error_code                      : If the software update has failed, this indicates the error code corresponding to the failure.
    update_downloading                     : Is software update package currently downloading.
    update_download_error_code             : If the software download has failed, this indicates the error code corresponding to the failure.
    update_download_start_time             : Start time of last update.
    update_download_end_time               : End time of last update.
    iscsi_automatic_connection_method      : Is iscsi reconnection automatic.
    iscsi_connection_rebalancing           : Does iscsi automatically rebalance connections.
    repl_throttled_bandwidth               : Current bandwidth throttle for replication, expressed either as megabits per second or as -1 to indicate that there is no throttle.
    repl_throttled_bandwidth_kbps          : Current bandwidth throttle for replication, expressed either as kilobits per second or as -1 to indicate that there is no throttle.
    repl_throttle_list                     : All the replication bandwidth limits on the system.
    volume_migration_status                : Status of data migration activity related to volumes being relocated to different pools.
    array_unassign_migration_status        : Data migration status for arrays being removed from their pool.
    data_rebalance_status                  : Status of data rebalancing operations for pools in the group.
    scsi_vendor_id                         : SCSI vendor ID.
    encryption_config                      : How encryption is configured for this group.
    last_login                             : Time and user of last login to this group.
    num_snaps                              : Number of snapshots in the group.
    num_snapcolls                          : Number of snapshot collections in this group.
    date                                   : Unix epoch time local to the group.
    login_banner_message                   : The message for the login banner that is displayed during user login activity.
    login_banner_after_auth                : Should the banner be displayed before the user credentials are prompted or after prompting the user credentials.
    login_banner_reset                     : This will reset the banner to the version of the installed NOS. When login_banner_after_auth is specified, login_banner_reset can not
                                             be set to true.
    snap_retn_meter_high                   : Threshold for considering a volume as high retention.
    snap_retn_meter_very_high              : Threshold for considering a volume as very high retention.
    """
    def reboot(self, **kwargs):
        """Reboot all arrays in the group.

        # Parameters
        id : ID of the group to reboot.
        job_timeout: Job timeout in seconds.
        """

        return self._collection.reboot(
            self.id,
            **kwargs
        )
    def halt(self, **kwargs):
        """Halt all arrays in the group.

        # Parameters
        id    : ID of the group to halt.
        force : Halt remaining arrays when one or more is unreachable.
        job_timeout: Job timeout in seconds.
        """

        return self._collection.halt(
            self.id,
            **kwargs
        )
    def test_alert(self, level, **kwargs):
        """Generate a test alert.

        # Parameters
        id    : ID of the group.
        level : Level of the test alert.
        """

        return self._collection.test_alert(
            self.id,
            level,
            **kwargs
        )
    def software_update_precheck(self, **kwargs):
        """Run software update precheck.

        # Parameters
        id                 : ID of the group.
        skip_precheck_mask : Flag to allow skipping certain types of prechecks.
        """

        return self._collection.software_update_precheck(
            self.id,
            **kwargs
        )
    def software_update_start(self, **kwargs):
        """Update the group software to the downloaded version.

        # Parameters
        id                    : ID of the group.
        skip_start_check_mask : Flag to allow skipping certain types of checks.
        """

        return self._collection.software_update_start(
            self.id,
            **kwargs
        )
    def software_download(self, version, **kwargs):
        """Download software update package.

        # Parameters
        id      : ID of the group.
        version : Version string to download.
        force   : Flag to force download.
        """

        return self._collection.software_download(
            self.id,
            version,
            **kwargs
        )
    def software_cancel_download(self, **kwargs):
        """Cancel ongoing download of software.

        # Parameters
        id : ID of the group.
        """

        return self._collection.software_cancel_download(
            self.id,
            **kwargs
        )
    def software_update_resume(self, **kwargs):
        """Resume stopped software update.

        # Parameters
        id : ID of the group.
        """

        return self._collection.software_update_resume(
            self.id,
            **kwargs
        )
    def get_group_discovered_list(self, **kwargs):
        """Get list of discovered groups with arrays that are initialized.

        # Parameters
        id         : ID of the group.
        group_name : Name of the group requested to be discovered.
        """

        return self._collection.get_group_discovered_list(
            self.id,
            **kwargs
        )
    def validate_merge(self, src_group_ip, src_group_name, src_password, src_username, **kwargs):
        """Perform group merge validation.

        # Parameters
        id                     : ID of the group.
        src_group_name         : Name of the source group.
        src_group_ip           : IP address of the source group.
        src_username           : Username of the source group.
        src_password           : Password of the source group.
        src_passphrase         : Source group encryption passphrase.
        skip_secondary_mgmt_ip : Skip check for secondary management IP address.
        """

        return self._collection.validate_merge(
            self.id,
            src_group_ip,
            src_group_name,
            src_password,
            src_username,
            **kwargs
        )
    def merge(self, src_group_ip, src_group_name, src_password, src_username, **kwargs):
        """Perform group merge with the specified group.

        # Parameters
        id                     : ID of the group.
        src_group_name         : Name of the source group.
        src_group_ip           : IP address of the source group.
        src_username           : Username of the source group.
        src_password           : Password of the source group.
        src_passphrase         : Source group encryption passphrase.
        force                  : Ignore warnings and forcibly merge specified group with this group.
        skip_secondary_mgmt_ip : Skip check for secondary management IP address.
        job_timeout            : Job timeout in seconds.
        """

        return self._collection.merge(
            self.id,
            src_group_ip,
            src_group_name,
            src_password,
            src_username,
            **kwargs
        )
    def get_eula(self, **kwargs):
        """Get URL to download EULA contents.

        # Parameters
        id     : ID of the group.
        locale : Locale of EULA contents. Default is en.
        format : Format of EULA contents. Default is HTML.
        phase  : Phase of EULA contents. Default is setup.
        force  : Flag to force EULA.
        """

        return self._collection.get_eula(
            self.id,
            **kwargs
        )
    def check_migrate(self, **kwargs):
        """Check if the group Management Service can be migrated to the group Management Service backup array.

        # Parameters
        id : ID of the group.
        """

        return self._collection.check_migrate(
            self.id,
            **kwargs
        )
    def migrate(self, **kwargs):
        """Migrate the group Management Service to the current group Management Service backup array.

        # Parameters
        id : ID of the group.
        """

        return self._collection.migrate(
            self.id,
            **kwargs
        )
    def get_timezone_list(self, **kwargs):
        """Get list of group timezones.

        # Parameters
        id : ID of the group.
        """

        return self._collection.get_timezone_list(
            self.id,
            **kwargs
        )

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")


class GroupList(Collection):
    resource = Group
    resource_type = "groups"

    def reboot(self, id, **kwargs):
        """Reboot all arrays in the group.

        # Parameters
        id : ID of the group to reboot.
        job_timeout: Job timeout in seconds.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'reboot',
            id=id,
            **kwargs
        )

    def halt(self, id, **kwargs):
        """Halt all arrays in the group.

        # Parameters
        id    : ID of the group to halt.
        force : Halt remaining arrays when one or more is unreachable.
        job_timeout: Job timeout in seconds.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'halt',
            id=id,
            **kwargs
        )

    def test_alert(self, id, level, **kwargs):
        """Generate a test alert.

        # Parameters
        id    : ID of the group.
        level : Level of the test alert.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'test_alert',
            id=id,
            level=level,
            **kwargs
        )

    def software_update_precheck(self, id, **kwargs):
        """Run software update precheck.

        # Parameters
        id                 : ID of the group.
        skip_precheck_mask : Flag to allow skipping certain types of prechecks.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'software_update_precheck',
            id=id,
            **kwargs
        )

    def software_update_start(self, id, **kwargs):
        """Update the group software to the downloaded version.

        # Parameters
        id                    : ID of the group.
        skip_start_check_mask : Flag to allow skipping certain types of checks.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'software_update_start',
            id=id,
            **kwargs
        )

    def software_download(self, id, version, **kwargs):
        """Download software update package.

        # Parameters
        id      : ID of the group.
        version : Version string to download.
        force   : Flag to force download.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'software_download',
            id=id,
            version=version,
            **kwargs
        )

    def software_cancel_download(self, id, **kwargs):
        """Cancel ongoing download of software.

        # Parameters
        id : ID of the group.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'software_cancel_download',
            id=id,
            **kwargs
        )

    def software_update_resume(self, id, **kwargs):
        """Resume stopped software update.

        # Parameters
        id : ID of the group.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'software_update_resume',
            id=id,
            **kwargs
        )

    def get_group_discovered_list(self, id, **kwargs):
        """Get list of discovered groups with arrays that are initialized.

        # Parameters
        id         : ID of the group.
        group_name : Name of the group requested to be discovered.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'get_group_discovered_list',
            id=id,
            **kwargs
        )

    def validate_merge(self, id, src_group_ip, src_group_name, src_password, src_username, **kwargs):
        """Perform group merge validation.

        # Parameters
        id                     : ID of the group.
        src_group_name         : Name of the source group.
        src_group_ip           : IP address of the source group.
        src_username           : Username of the source group.
        src_password           : Password of the source group.
        src_passphrase         : Source group encryption passphrase.
        skip_secondary_mgmt_ip : Skip check for secondary management IP address.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'validate_merge',
            id=id,
            src_group_ip=src_group_ip,
            src_group_name=src_group_name,
            src_password=src_password,
            src_username=src_username,
            **kwargs
        )

    def merge(self, id, src_group_ip, src_group_name, src_password, src_username, **kwargs):
        """Perform group merge with the specified group.

        # Parameters
        id                     : ID of the group.
        src_group_name         : Name of the source group.
        src_group_ip           : IP address of the source group.
        src_username           : Username of the source group.
        src_password           : Password of the source group.
        src_passphrase         : Source group encryption passphrase.
        force                  : Ignore warnings and forcibly merge specified group with this group.
        skip_secondary_mgmt_ip : Skip check for secondary management IP address.
        job_timeout            : Job timeout in seconds.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'merge',
            id=id,
            src_group_ip=src_group_ip,
            src_group_name=src_group_name,
            src_password=src_password,
            src_username=src_username,
            **kwargs
        )

    def get_eula(self, id, **kwargs):
        """Get URL to download EULA contents.

        # Parameters
        id     : ID of the group.
        locale : Locale of EULA contents. Default is en.
        format : Format of EULA contents. Default is HTML.
        phase  : Phase of EULA contents. Default is setup.
        force  : Flag to force EULA.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'get_eula',
            id=id,
            **kwargs
        )

    def check_migrate(self, id, **kwargs):
        """Check if the group Management Service can be migrated to the group Management Service backup array.

        # Parameters
        id : ID of the group.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'check_migrate',
            id=id,
            **kwargs
        )

    def migrate(self, id, **kwargs):
        """Migrate the group Management Service to the current group Management Service backup array.

        # Parameters
        id : ID of the group.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'migrate',
            id=id,
            **kwargs
        )

    def get_timezone_list(self, id, **kwargs):
        """Get list of group timezones.

        # Parameters
        id : ID of the group.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'get_timezone_list',
            id=id,
            **kwargs
        )

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")
