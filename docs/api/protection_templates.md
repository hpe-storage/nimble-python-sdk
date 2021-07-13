# Table of Contents

* [nimbleclient.v1.api.protection\_templates](#nimbleclient.v1.api.protection_templates)
  * [ProtectionTemplate](#nimbleclient.v1.api.protection_templates.ProtectionTemplate)

<a name="nimbleclient.v1.api.protection_templates"></a>
# nimbleclient.v1.api.protection\_templates

<a name="nimbleclient.v1.api.protection_templates.ProtectionTemplate"></a>
## ProtectionTemplate

```python
class ProtectionTemplate(Resource)
```

Manage protection templates. Protection templates are sets of snapshot schedules, replication schedules, and retention limits that can be used to prefill the protection
information when creating new volume collections. A volume collection, once created, is not affected by edits to the protection template that was used to create it. All the
volumes assigned to a volume collection use the same settings. You cannot edit or delete the predefined protection templates provided by storage array, but you can create
custom protection templates as needed.

__Parameters__

- __id               __: Identifier for protection template.
- __name             __: User provided identifier.
- __full_name        __: Fully qualified name of protection template.
- __search_name      __: Name of protection template used for object search.
- __description      __: Text description of protection template.
- __repl_priority    __: Replication priority for the protection template with the following choices: {normal | high}.
- __app_sync         __: Application synchronization ({none|vss|vmware|generic}).
- __app_server       __: Application server hostname.
- __app_id           __: Application ID running on the server. Application ID can only be specified if application synchronization is VSS.
- __app_cluster_name __: If the application is running within a Windows cluster environment then this is the cluster name.
- __app_service_name __: If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment.
- __vcenter_hostname __: VMware vCenter hostname. Custom port number can be specified with vCenter hostname using :.
- __vcenter_username __: VMware vCenter username.
- __vcenter_password __: VMware vCenter password.
- __agent_hostname   __: Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\":\\".
- __agent_username   __: Generic Backup agent username.
- __agent_password   __: Generic Backup agent password.
- __creation_time    __: Time when this protection template was created.
- __last_modified    __: Time when this protection template was last modified.
- __schedule_list    __: List of schedules for this protection policy.

