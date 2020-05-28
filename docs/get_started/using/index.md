# Using the SDK

Refer to the API reference for indivual resource manipulations. This introduction illustrate how to use the SDK and the more advanced features. HPE Nimble Storage specific workflows can be found in the [example workflows](../examples/index.md) section.

[TOC]

## Using python interactively

From scratch on a `python` prompt.

```python
$ python
Python 3.7.7 (default, Mar 10 2020, 15:43:03)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from nimbleclient import NimOSClient
>>> import pprint
>>> api = NimOSClient('192.168.1.128', 'admin', 'admin')
>>>
```

!!! note
    All the examples below uses `pprint` for formatting purposes only.

## Manipulating resources

Simple interactions with the `volumes` endpoint. Refer to the [volumes](../../api/volumes.md) API reference for more details.

### Create a volume

```python
>>> api.volumes.create('myvol1', size=1024, description='My first volume')
<Volume(id=0649686580b78e0b16000000000000000000000004, name=myvol1)>
```

### Create a volume with custom metadata

```python
>>> meta_data = {'mykey1': 'myval1', 'mykey2': 'myval2'}
>>> api.volumes.create('myvol2', size=2048, description='My second volume', metadata=meta_data)
<Volume(id=0649686580b78e0b16000000000000000000000005, name=myvol2)>
```

### List volumes

```python
>>> pprint.pprint(api.volumes.list())
[<Volume(id=0649686580b78e0b16000000000000000000000004, name=myvol1)>,
 <Volume(id=0649686580b78e0b16000000000000000000000005, name=myvol2)>]
```

### Fetch volume attributes

```python
>>> pprint.pprint(api.volumes.get('0649686580b78e0b16000000000000000000000005').attrs)
{'access_control_records': None,
 'agent_type': 'none',
 'app_category': 'Other',
 'app_uuid': '',
 'avg_stats_last_5mins': {'combined_iops': 0,
                          'combined_latency': 0,
                          'combined_throughput': 0,
                          'read_iops': 0,
                          'read_latency': 0,
                          'read_throughput': 0,
                          'write_iops': 0,
                          'write_latency': 0,
                          'write_throughput': 0},
 'base_snap_id': '',
 'base_snap_name': '',
 'block_size': 4096,
 'cache_needed_for_pin': 2147483648,
 'cache_pinned': False,
 'cache_policy': 'normal',
 'caching_enabled': True,
 'cksum_last_verified': 0,
 'clone': False,
 'content_repl_errors_found': False,
 'creation_time': 1573161873,
 'dedupe_enabled': False,
 'description': 'My second volume',
 'dest_pool_id': '',
 'dest_pool_name': '',
 'encryption_cipher': 'none',
 'fc_sessions': None,
 'folder_id': '',
 'folder_name': '',
 'full_name': 'default:/myvol2',
 'id': '0649686580b78e0b16000000000000000000000005',
 'iscsi_sessions': None,
 'iscsi_target_scope': 'group',
 'last_content_snap_br_cg_uid': 0,
 'last_content_snap_br_gid': 0,
 'last_content_snap_id': 0,
 'last_modified': 1573161873,
 'last_replicated_snap': None,
 'last_snap': None,
 'limit': 100,
 'limit_iops': -1,
 'limit_mbps': -1,
 'metadata': [{'key': 'mykey2', 'value': 'myval2'},
              {'key': 'mykey1', 'value': 'myval1'}],
 'move_aborting': False,
 'move_bytes_migrated': 0,
 'move_bytes_remaining': 0,
 'move_est_compl_time': 0,
 'move_start_time': 0,
 'multi_initiator': False,
 'name': 'myvol2',
 'needs_content_repl': False,
 'num_connections': 0,
 'num_fc_connections': 0,
 'num_iscsi_connections': 0,
 'num_snaps': 0,
 'offline_reason': None,
 'online': True,
 'online_snaps': None,
 'owned_by_group': 'nva-test-grp',
 'owned_by_group_id': '0049686580b78e0b16000000000000000000000001',
 'parent_vol_id': '',
 'parent_vol_name': '',
 'perfpolicy_id': '0349686580b78e0b16000000000000000000000001',
 'perfpolicy_name': 'default',
 'pinned_cache_size': 0,
 'pool_id': '0a49686580b78e0b16000000000000000000000001',
 'pool_name': 'default',
 'previously_deduped': False,
 'projected_num_snaps': 0,
 'protection_type': 'unprotected',
 'read_only': False,
 'replication_role': 'no_replication',
 'reserve': 0,
 'search_name': 'myvol2',
 'serial_number': '2ee4231f34e21d4b6c9ce900966ee6fe',
 'size': 2048,
 'snap_limit': 9223372036854775807,
 'snap_limit_percent': -1,
 'snap_reserve': 0,
 'snap_usage_compressed_bytes': 0,
 'snap_usage_populated_bytes': 0,
 'snap_usage_uncompressed_bytes': 0,
 'snap_warn_level': 0,
 'space_usage_level': 'normal',
 'srep_last_sync': 0,
 'srep_resync_percent': 0,
 'target_name': 'iqn.2007-11.com.nimblestorage:nva-test-grp-g49686580b78e0b16',
 'thinly_provisioned': True,
 'total_usage_bytes': 0,
 'upstream_cache_pinned': False,
 'usage_valid': True,
 'vol_state': 'online',
 'vol_usage_compressed_bytes': 0,
 'vol_usage_mapped_bytes': 0,
 'vol_usage_uncompressed_bytes': 0,
 'volcoll_id': '',
 'volcoll_name': '',
 'vpd_ieee0': '2ee4231f34e21d4b',
 'vpd_ieee1': '6c9ce900966ee6fe',
 'vpd_t10': 'Nimble  2ee4231f34e21d4b6c9ce900966ee6fe',
 'warn_level': 0}
```

## Assign a volume to an object

```python
>>> vol = api.volumes.get(name='myvol1')
<Volume(id=0601a32bf8f45646a500000000000000000000070d, name=vol-3)>
```

## Access object attributes

```python
>>> vol = api.volumes.get(name='myvol2')
>>> pprint.pprint(vol.attrs['metadata'])
[{'key': 'mykey2', 'value': 'myval2'}, {'key': 'mykey1', 'value': 'myval1'}]
```

## Update volume attributes

```python
>>> vol.update(id=vol.attrs['id'], description='My new cool description')
>>> vol.reload()
>>> pprint.pprint(vol.attrs['description'])
'My new cool description'
```

## Access object methods

```python
>>> vol.offline()
{ 'offline_reason': 'user', 'online': False } # Full object representation omitted 
>>> vol.delete()
{}
```

## Pagination

The `list` operation of an API resource comes with `limit` and `from_id` attributes that provide means to paginate objects and perform operations in batches. The below example uses the `volumes` resource to paginate volume objects.

```python
>>> pprint.pprint(api.volumes.list(limit=3))
[<Volume(id=0649686580b78e0b16000000000000000000000004, name=myvol1)>,
 <Volume(id=0649686580b78e0b16000000000000000000000005, name=myvol2)>,
 <Volume(id=0649686580b78e0b16000000000000000000000006, name=myvol3)>]
>>>
>>> pprint.pprint(api.volumes.list(limit=3, from_id='0649686580b78e0b16000000000000000000000006'))
[<Volume(id=0649686580b78e0b16000000000000000000000007, name=myvol4)>,
 <Volume(id=0649686580b78e0b16000000000000000000000008, name=myvol5)>,
 <Volume(id=0649686580b78e0b16000000000000000000000009, name=myvol6)>]
>>>
>>> pprint.pprint(api.volumes.list(limit=3, from_id='0649686580b78e0b16000000000000000000000009'))
[<Volume(id=0649686580b78e0b1600000000000000000000000a, name=myvol7)>]
>>>
```

## Field filters
    
Most of the time a developer have a vague idea of what he's looking for and what attributes are of interest. Using field filters one way to satisfy the need and optimize the payload.

### List only resources with a certain name

```python
>>> pprint.pprint(api.volumes.list(name='myvol1'))
[<Volume(id=0649686580b78e0b16000000000000000000000004, name=myvol1)>]
```

### Expand object with limited resource attributes

```python
>>> pprint.pprint(api.volumes.list(name='myvol1', detail=True, fields='name,id,size,online,clone')[0].attrs)
{'clone': False,
 'id': '0649686580b78e0b16000000000000000000000004',
 'name': 'myvol1',
 'online': True,
 'size': 1024}
```

## Using Fields

Each API resource comes with "Fields" class which allow complex querying of the resource. The class naming convention is the resource name in singular without underscores in camelcase. Example:

- `volumes` -> `VolumeFields`
- `volume_collections` - `VolumeCollectionFields`
- `protection_templates` - `ProtectionTemplateFields`

!!! note
    The volume named "myvol2" in previous steps that was deleted has to be recreated for the next set of examples to make sense.

### Search for a volume wildcard

```python
>>> from nimbleclient import *
>>> from nimbleclient.v1 import VolumeFields
>>> pprint.pprint(api.volumes.list(filter=and_(VolumeFields.name.contains('vol'))))
[<Volume(id=0649686580b78e0b16000000000000000000000004, name=myvol1)>,
 <Volume(id=0649686580b78e0b16000000000000000000000006, name=myvol2)>]
```

### Combining multiple Fields

```python
>>> myfilter = and_(
... VolumeFields.name.contains('vol'),
... VolumeFields.metadata('mykey1') == 'myval1'
... )
>>> pprint.pprint(api.volumes.list(detail=True, filter=myfilter, fields='id,name,size,metadata'))
[<Volume(id=0649686580b78e0b16000000000000000000000006, name=myvol2)>]
>>> pprint.pprint(api.volumes.list(detail=True, filter=myfilter, fields='name,size,metadata'
... )[0].attrs)
{'metadata': [{'key': 'mykey2', 'value': 'myval2'},
              {'key': 'mykey1', 'value': 'myval1'}],
 'name': 'myvol2',
 'size': 2048}
```

### Complex Fields with AND and OR operators

```python
>>> myfilter = and_(
...     VolumeFields.name.contains('vol'),
...     VolumeFields.online == 'true',
...     or_(
...         VolumeFields.protection_type == 'unprotected',
...         and_(
...             VolumeFields.size <= '4096',
...             VolumeFields.encryption_cipher == None,
...         )
...     )
... )
>>> pprint.pprint(api.volumes.list(detail=True, filter=myfilter, fields='id,name,size,metadata'))
[<Volume(id=0649686580b78e0b16000000000000000000000004, name=myvol1)>,
 <Volume(id=0649686580b78e0b16000000000000000000000006, name=myvol2)>]
```
