# HPE Nimble Storage SDK for Python
This is a Python Software Development Kit (SDK) for [HPE Nimble Storage](http://hpe.com/storage/nimblestorage) arrays. The HPE Nimble Storage array has a Representational State Transfer (REST) web service application programming interface (API). The SDK implements a simple client library for communicating with the HPE Nimble Storage REST API. The Python Requests library is being used to communicate with the API over HTTPS.

The SDK provides a pythonic client library to interact with the HPE Nimble Storage REST API. The code abstracts the lower-level API calls into Python objects that you can easily incorporate into any automation or DevOps workflows. Use it to create, modify and delete most resources like volumes, volume collections, initiator groups and more, as well as perform other tasks like snapshotting, cloning, restoring data, etc.

# Synopsis

See the [documentation](https://hpe-storage.github.io/nimble-python-sdk) on how to [install](https://hpe-storage.github.io/nimble-python-sdk/get_started/install/index.html), [use](https://hpe-storage.github.io/nimble-python-sdk/get_started/using/index.html) and some pre-cocked [workflows](https://hpe-storage.github.io/nimble-python-sdk/get_started/examples/index.html) for more elaborate examples.

```python
$ pip install nimble-sdk
$ python
Python 3.7.7 (default, Mar 10 2020, 15:43:03) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin 
Type "help", "copyright", "credits" or "license" for more information. 
>>> from nimbleclient import NimOSClient 
>>> api = NimOSClient("192.168.1.100", "admin", "admin")
>>> api.
api.access_control_records           api.folders                          api.snapshot_collections
api.active_directory_memberships     api.groups                           api.snapshots
api.alarms                           api.initiator_groups                 api.software_versions
api.application_categories           api.initiators                       api.space_domains
api.application_servers              api.jobs                             api.subnets
api.arrays                           api.key_managers                     api.support
api.audit_log                        api.master_key                       api.tokens
api.chap_users                       api.network_configs                  api.user_groups
api.controllers                      api.network_interfaces               api.user_policies
api.disks                            api.performance_policies             api.users
api.events                           api.pools                            api.versions
api.fibre_channel_configs            api.protection_schedules             api.volume_collections
api.fibre_channel_initiator_aliases  api.protection_templates             api.volumes
api.fibre_channel_interfaces         api.protocol_endpoints               api.witnesses
api.fibre_channel_ports              api.replication_partners
api.fibre_channel_sessions           api.shelves
```

# Requirements

The HPE Nimble Storage SDK for Python supports NimbleOS 5.1.x or later and requires a recent version of [Requests](https://requests.readthedocs.io) along with Python 3.6 or newer.

# Contributing

Contributing guidelines are available in the [official documentation](https://hpe-storage.github.io/nimble-python-sdk/legal/contributing/index.html).

# Community

Join the HPE DEV slack by signing up at [slack.hpedev.io](slack.hpedev.io). HPE employees may sign in direct at [hpedev.slack.com](hpedev.slack.com) with a valid HPE address. We hang out in `#NimbleStorage`.

# License

See [LICENSE](LICENSE)
