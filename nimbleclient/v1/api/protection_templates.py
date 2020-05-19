#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class ProtectionTemplate(Resource):
    """Manage protection templates. Protection templates are sets of snapshot schedules, replication schedules, and retention limits that can be used to prefill the protection
    information when creating new volume collections. A volume collection, once created, is not affected by edits to the protection template that was used to create it. All the
    volumes assigned to a volume collection use the same settings. You cannot edit or delete the predefined protection templates provided by storage array, but you can create
    custom protection templates as needed.

    # Parameters
    id               : Identifier for protection template.
    name             : User provided identifier.
    full_name        : Fully qualified name of protection template.
    search_name      : Name of protection template used for object search.
    description      : Text description of protection template.
    repl_priority    : Replication priority for the protection template with the following choices: {normal | high}.
    app_sync         : Application synchronization ({none|vss|vmware|generic}).
    app_server       : Application server hostname.
    app_id           : Application ID running on the server. Application ID can only be specified if application synchronization is VSS.
    app_cluster_name : If the application is running within a Windows cluster environment then this is the cluster name.
    app_service_name : If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment.
    vcenter_hostname : VMware vCenter hostname. Custom port number can be specified with vCenter hostname using :.
    vcenter_username : VMware vCenter username.
    vcenter_password : VMware vCenter password.
    agent_hostname   : Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\":\\".
    agent_username   : Generic Backup agent username.
    agent_password   : Generic Backup agent password.
    creation_time    : Time when this protection template was created.
    last_modified    : Time when this protection template was last modified.
    schedule_list    : List of schedules for this protection policy.
    """


class ProtectionTemplateList(Collection):
    resource = ProtectionTemplate
    resource_type = "protection_templates"
