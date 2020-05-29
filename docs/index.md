# HPE Nimble Storage SDK for Python
This is a Python Software Development Kit (SDK) for [HPE Nimble Storage](http://hpe.com/storage/nimblestorage) arrays. The HPE Nimble Storage array has a Representational State Transfer (REST) web service application programming interface (API). The SDK implements a simple client library for communicating with the HPE Nimble Storage REST API. The Python Requests library is being used to communicate with the API over HTTPS.

The SDK provides a pythonic client library to interact with the HPE Nimble Storage REST API. The code abstracts the lower-level API calls into Python objects that you can easily incorporate into any automation or DevOps workflows. Use it to create, modify and delete most resources like volumes, volume collections, initiator groups and more, as well as perform other tasks like snapshotting, cloning, restoring data, etc.

# Synopsis
See [install](get_started/install/index.md), [using](get_started/using/index.md) and [example workflows](get_started/examples/index.md) for more elaborate examples.

```python
$ pip install nimble-sdk
$ python
Python 3.7.7 (default, Mar 10 2020, 15:43:03) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin 
Type "help", "copyright", "credits" or "license" for more information. 
>>> from nimbleclient import NimOSClient 
>>> api = NimOSClient("192.168.1.100", "admin", "admin")
>>> api.
api.access_control_records           api.fibre_channel_sessions           api.replication_partners
api.active_directory_memberships     api.folders                          api.shelves
api.alarms                           api.groups                           api.snapshot_collections
api.application_categories           api.initiator_groups                 api.snapshots
api.application_servers              api.initiators                       api.software_versions
api.arrays                           api.jobs                             api.space_domains
api.audit_log                        api.key_managers                     api.subnets
api.chap_users                       api.master_key                       api.tokens
api.controllers                      api.network_configs                  api.user_groups
api.disks                            api.network_interfaces               api.user_policies
api.events                           api.performance_policies             api.users
api.fibre_channel_configs            api.pools                            api.versions
api.fibre_channel_initiator_aliases  api.protection_schedules             api.volume_collections
api.fibre_channel_interfaces         api.protection_templates             api.volumes
api.fibre_channel_ports              api.protocol_endpoints               api.witnesses
```

# Requirements

The HPE Nimble Storage SDK for Python supports NimbleOS 5.1.x or later and requires a recent version of [Requests](https://requests.readthedocs.io) along with Python 3.6 or newer.
