#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class Array(Resource):
    """Retrieve information of specified arrays. The array is the management and configuration for the underlying physical hardware array box.

    # Parameters
    id                            : Identifier for array.
    name                          : The user provided name of the array. It is also the array's hostname.
    force                         : Forcibly delete the specified array.
    full_name                     : The array's fully qualified name.
    search_name                   : The array name used for object search.
    status                        : Reachability status of the array in the group.
    role                          : Role of the array in the group.
    group_state                   : State of the array in the group.
    pool_name                     : Name of pool to which this is a member.
    pool_id                       : ID of pool to which this is a member.
    model                         : Array model.
    serial                        : Serial number of the array.
    version                       : Software version of the array.
    is_sfa                        : True if this array supports SFA; false otherwise.
    creation_time                 : Time when this array object was created.
    last_modified                 : Time when this array object was last modified.
    usage_valid                   : Indicates whether the usage of array is valid.
    usable_capacity_bytes         : The usable capacity of the array in bytes.
    usable_cache_capacity_bytes   : The usable cache capacity of the array in bytes.
    raw_capacity_bytes            : The raw capacity of the array in bytes.
    vol_usage_bytes               : The compressed usage of volumes in array.
    vol_usage_uncompressed_bytes  : The uncompressed usage of volumes in array. This is the pre-reduced usage.
    vol_compression               : The compression rate of volumes in array expressed as ratio.
    vol_saved_bytes               : The saved space of volumes in array.
    snap_usage_bytes              : The compressed usage of snapshots in array.
    snap_usage_uncompressed_bytes : The uncompressed usage of snapshots in array. This is the pre-reduced usage.
    snap_compression              : The compression rate of snapshots in array expressed as ratio.
    snap_space_reduction          : The space reduction rate of snapshots in array expressed as ratio.
    snap_saved_bytes              : The saved space of snapshots in array.
    pending_delete_bytes          : The pending delete bytes in array.
    available_bytes               : The available space of array.
    usage                         : Used space of the array in bytes.
    all_flash                     : Whether it is an all-flash array.
    dedupe_capacity_bytes         : The dedupe capacity of a hybrid array. Does not apply to all-flash arrays.
    dedupe_usage_bytes            : The dedupe usage of a hybrid array. Does not apply to all-flash arrays.
    is_fully_dedupe_capable       : Is array fully capable to dedupe its usable capacity.
    extended_model                : Extended model of the array.
    is_supported_hw_config        : Whether it is a supported hardware config.
    gig_nic_port_count            : Count of 1G NIC Ports installed on the array.
    ten_gig_sfp_nic_port_count    : Count of 10G SFP NIC Ports installed on the array.
    ten_gig_t_nic_port_count      : Count of 10G BaseT NIC Ports installed on the array.
    fc_port_count                 : Count of Fibre Channel Ports installed on the array.
    public_key                    : Public key of the array.
    upgrade                       : The array upgrade data.
    create_pool                   : Whether to create associated pool during array create.
    pool_description              : Text description of the pool to be created during array creation.
    allow_lower_limits            : A True setting will allow you to add an array with lower limits to a pool with higher limits.
    ctrlr_a_support_ip            : Controller A Support IP Address.
    ctrlr_b_support_ip            : Controller B Support IP Address.
    nic_list                      : List NICs information. Used when creating an array.
    model_sub_type                : Array model sub type.
    zconf_ipaddrs                 : List of link-local zero-configuration addresses of the array.
    secondary_mgmt_ip             : Secondary management IP address for the Group.
    """
    def failover(self, **kwargs):
        """Perform a failover on the specified array.

        # Parameters
        id    : ID of the array to perform failover on.
        force : Initiate failover without performing any precheck.
        job_timeout: Job timeout in seconds.
        """

        return self._collection.failover(
            self.id,
            **kwargs
        )
    def halt(self, **kwargs):
        """Halt the specified array. Restarting the array will require physically powering it back on.

        # Parameters
        id : ID of the array to halt.
        job_timeout: Job timeout in seconds.
        """

        return self._collection.halt(
            self.id,
            **kwargs
        )
    def reboot(self, **kwargs):
        """Reboot the specified array.

        # Parameters
        id : ID of the array to reboot.
        job_timeout: Job timeout in seconds.
        """

        return self._collection.reboot(
            self.id,
            **kwargs
        )


class ArrayList(Collection):
    resource = Array
    resource_type = "arrays"

    def failover(self, id, **kwargs):
        """Perform a failover on the specified array.

        # Parameters
        id    : ID of the array to perform failover on.
        force : Initiate failover without performing any precheck.
        job_timeout: Job timeout in seconds.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'failover',
            id=id,
            **kwargs
        )

    def halt(self, id, **kwargs):
        """Halt the specified array. Restarting the array will require physically powering it back on.

        # Parameters
        id : ID of the array to halt.
        job_timeout: Job timeout in seconds.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'halt',
            id=id,
            **kwargs
        )

    def reboot(self, id, **kwargs):
        """Reboot the specified array.

        # Parameters
        id : ID of the array to reboot.
        job_timeout: Job timeout in seconds.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'reboot',
            id=id,
            **kwargs
        )
