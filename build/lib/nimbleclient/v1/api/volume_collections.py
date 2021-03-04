#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class VolumeCollection(Resource):
    """Manage volume collections. Volume collections are logical groups of volumes that share protection characteristics such as snapshot and replication schedules. Volume
    collections can be created from scratch or based on predefined protection templates.

    # Parameters
    id                            : Identifier for volume collection.
    prottmpl_id                   : Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input
                                    when creating a volume collection and is not outputed.
    name                          : Name of volume collection.
    full_name                     : Fully qualified name of volume collection.
    search_name                   : Name of volume collection used for object search.
    description                   : Text description of volume collection.
    repl_priority                 : Replication priority for the volume collection with the following choices: {normal | high}.
    pol_owner_name                : Owner group.
    replication_type              : Type of replication configured for the volume collection.
    synchronous_replication_type  : Type of synchronous replication configured for the volume collection.
    synchronous_replication_state : State of synchronous replication on the volume collection.
    app_sync                      : Application Synchronization.
    app_server                    : Application server hostname.
    app_id                        : Application ID running on the server. Application ID can only be specified if application synchronization is \\"vss\\".
    app_cluster_name              : If the application is running within a Windows cluster environment, this is the cluster name.
    app_service_name              : If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster
                                    environment.
    vcenter_hostname              : VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\":\\".
    vcenter_username              : Application VMware vCenter username.
    vcenter_password              : Application VMware vCenter password.
    agent_hostname                : Generic backup agent hostname. Custom port number can be specified with agent hostname using \\":\\".
    agent_username                : Generic backup agent username.
    agent_password                : Generic backup agent password.
    creation_time                 : Time when this volume collection was created.
    last_modified_time            : Time when this volume collection was last modified.
    volume_list                   : List of volumes associated with the volume collection.
    downstream_volume_list        : List of downstream volumes associated with the volume collection.
    upstream_volume_list          : List of upstream volumes associated with the volume collection.
    volume_count                  : Count of volumes associated with the volume collection.
    cache_pinned_volume_list      : List of cache pinned volumes associated with volume collection.
    last_snapcoll                 : Last snapshot collection on this volume collection.
    snapcoll_count                : Count of snapshot collections associated with volume collection.
    schedule_list                 : List of snapshot schedules associated with volume collection.
    replication_partner           : Replication partner for this volume collection.
    last_replicated_snapcoll      : Last replicated snapshot collection on this volume collection.
    last_replicated_snapcoll_list : List of snapshot collection information for the last replicated snapshot collection per schedule.
    protection_type               : Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup.
    lag_time                      : Replication lag time for volume collection.
    is_standalone_volcoll         : Indicates whether this is a standalone volume collection.
    total_repl_bytes              : Total size of volumes to be replicated for this volume collection.
    repl_bytes_transferred        : Total size of volumes replicated for this volume collection.
    is_handing_over               : Indicates whether a handover operation is in progress on this volume collection.
    handover_replication_partner  : Replication partner to which ownership is being transferred as part of handover operation.
    metadata                      : Key-value pairs that augment a volume collection's attributes.
    srep_last_sync                : Time when a synchronously replicated volume collection was last synchronized.
    srep_resync_percent           : Percentage of the resync progress for a synchronously replicated volume collection.
    """
    def promote(self, **kwargs):
        """Take ownership of the specified volume collection. The volumes associated with the volume collection will be set to online and be available for reading and writing.
        Replication will be disabled on the affected schedules and must be re-configured if desired. Snapshot retention for the affected schedules will be set to the greater of
        the current local or replica retention values. This operation is not supported for synchronous replication volume collections.

        # Parameters
        id : ID of the promoted volume collection.
        """

        return self._collection.promote(
            self.id,
            **kwargs
        )
    def demote(self, replication_partner_id, **kwargs):
        """Release ownership of the specified volume collection. The volumes associated with the volume collection will set to offline and a snapshot will be created, then full
        control over the volume collection will be transferred to the new owner. This option can be used following a promote to revert the volume collection back to its prior
        configured state. This operation does not alter the configuration on the new owner itself, but does require the new owner to be running in order to obtain its identity
        information. This operation is not supported for synchronous replication volume collections.

        # Parameters
        id                         : ID of the demoted volume collection.
        replication_partner_id     : ID of the new owner. If invoke_on_upstream_partner is provided, utilize the ID of the current owner i.e. upstream replication partner.
        invoke_on_upstream_partner : Invoke demote request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.
        """

        return self._collection.demote(
            self.id,
            replication_partner_id,
            **kwargs
        )
    def handover(self, replication_partner_id, **kwargs):
        """Gracefully transfer ownership of the specified volume collection. This action can be used to pass control of the volume collection to the downstream replication partner.
        Ownership and full control over the volume collection will be given to the downstream replication partner. The volumes associated with the volume collection will be set to
        offline prior to the final snapshot being taken and replicated, thus ensuring full data synchronization as part of the transfer. By default, the new owner will
        automatically begin replicating the volume collection back to this node when the handover completes.

        # Parameters
        id                         : ID of the volume collection be handed over to the downstream replication partner.
        replication_partner_id     : ID of the new owner.
        no_reverse                 : Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the
                                     volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default: 'false'.
        invoke_on_upstream_partner : Invoke handover request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.
        override_upstream_down     : Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This
                                     option is applicable for synchronous replication only. Default: 'false'.
        """

        return self._collection.handover(
            self.id,
            replication_partner_id,
            **kwargs
        )
    def abort_handover(self, **kwargs):
        """Abort in-progress handover. If for some reason a previously invoked handover request is unable to complete, this action can be used to cancel it. This operation is not
        supported for synchronous replication volume collections.

        # Parameters
        id : ID of the volume collection on which to abort handover.
        """

        return self._collection.abort_handover(
            self.id,
            **kwargs
        )
    def validate(self, **kwargs):
        """Validate a volume collection with either Microsoft VSS or VMware application synchronization.

        # Parameters
        id : ID of the volume collection that is to be validated.
        """

        return self._collection.validate(
            self.id,
            **kwargs
        )


class VolumeCollectionList(Collection):
    resource = VolumeCollection
    resource_type = "volume_collections"

    def promote(self, id, **kwargs):
        """Take ownership of the specified volume collection. The volumes associated with the volume collection will be set to online and be available for reading and writing.
        Replication will be disabled on the affected schedules and must be re-configured if desired. Snapshot retention for the affected schedules will be set to the greater of
        the current local or replica retention values. This operation is not supported for synchronous replication volume collections.

        # Parameters
        id : ID of the promoted volume collection.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'promote',
            id=id,
            **kwargs
        )

    def demote(self, id, replication_partner_id, **kwargs):
        """Release ownership of the specified volume collection. The volumes associated with the volume collection will set to offline and a snapshot will be created, then full
        control over the volume collection will be transferred to the new owner. This option can be used following a promote to revert the volume collection back to its prior
        configured state. This operation does not alter the configuration on the new owner itself, but does require the new owner to be running in order to obtain its identity
        information. This operation is not supported for synchronous replication volume collections.

        # Parameters
        id                         : ID of the demoted volume collection.
        replication_partner_id     : ID of the new owner. If invoke_on_upstream_partner is provided, utilize the ID of the current owner i.e. upstream replication partner.
        invoke_on_upstream_partner : Invoke demote request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'demote',
            id=id,
            replication_partner_id=replication_partner_id,
            **kwargs
        )

    def handover(self, id, replication_partner_id, **kwargs):
        """Gracefully transfer ownership of the specified volume collection. This action can be used to pass control of the volume collection to the downstream replication partner.
        Ownership and full control over the volume collection will be given to the downstream replication partner. The volumes associated with the volume collection will be set to
        offline prior to the final snapshot being taken and replicated, thus ensuring full data synchronization as part of the transfer. By default, the new owner will
        automatically begin replicating the volume collection back to this node when the handover completes.

        # Parameters
        id                         : ID of the volume collection be handed over to the downstream replication partner.
        replication_partner_id     : ID of the new owner.
        no_reverse                 : Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the
                                     volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default: 'false'.
        invoke_on_upstream_partner : Invoke handover request on upstream partner. Default: 'false'. This operation is not supported for synchronous replication volume vollections.
        override_upstream_down     : Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This
                                     option is applicable for synchronous replication only. Default: 'false'.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'handover',
            id=id,
            replication_partner_id=replication_partner_id,
            **kwargs
        )

    def abort_handover(self, id, **kwargs):
        """Abort in-progress handover. If for some reason a previously invoked handover request is unable to complete, this action can be used to cancel it. This operation is not
        supported for synchronous replication volume collections.

        # Parameters
        id : ID of the volume collection on which to abort handover.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'abort_handover',
            id=id,
            **kwargs
        )

    def validate(self, id, **kwargs):
        """Validate a volume collection with either Microsoft VSS or VMware application synchronization.

        # Parameters
        id : ID of the volume collection that is to be validated.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'validate',
            id=id,
            **kwargs
        )
