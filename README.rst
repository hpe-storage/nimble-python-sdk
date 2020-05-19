Nimble Python SDK
=================
The Nimble Python SDK (client library) is a utility that can be leveraged to manage HPE Nimble Storage arrays. The HPE Nimble Storage array has a REST API web service interface. This SDK implements a simple interface for talking with that REST interface. The python requests library is used to communicate with the REST interface.

This library provides a pythonic interface to the HPE Nimble REST API. The code abstracts the lower-level API calls into python objects that you can easily incorporate into any automation or devops workflow. Use it to create, modify and delete most resources like volumes, volume collections, and initiator groups as well as perform other tasks like snapshotting, cloning, and restoring data.

Requirements
------------
-   Python 3.6+.
-   Nimble Storage array (Nimble OS	Version 5.x and later)

Installing
----------

The Nimble Python SDK can be installed with `pip <https://pip.pypa.io>`. To install the latest version from `pypi <http://pypi.org>`:

    $ pip install nimble-sdk

Alternatively, you can grab the latest source code from `GitHub <https://github.com/hpe-storage/nimble-python-sdk>`:

    $ git clone https://github.com/hpe-storage/nimble-python-sdk.git
    $ python setup.py install


Download
--------

The Nimble Python SDK is available on PyPI `https://pypi.org/project/hpe-nimble-sdk`


Documentation
-------------

The Nimble Python SDK has usage and reference documentation at `nimble-sdk.readthedocs.io <https://scod.hpedev.io/storage_automation/nimble_python_sdk/index.html>`.


Getting Started
---------------

You can now import the module `nimbleclient` and use it in any python script/application.

.. code-block:: pycon

    python3.7
    Python 3.7.4 (default, Sep  7 2019, 18:27:02)
    [Clang 10.0.1 (clang-1001.0.46.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    >>> from nimbleclient import NimOSClient
    >>> import pprint
    >>> client = NimOSClient("1.1.1.1", "admin", "admin")
    >>>
    >>> client.volumes.create("vol-1", size=1024, description="Test volume1 for SDK")
    <Volume(id=0601a32bf8f45646a5000000000000000000000687, name=vol-1)>
    >>>
    >>> meta_data = {'k1': 'v1', 'k2': 'v2'}
    >>> client.volumes.create("vol-2", size=2048, description="Test volume2 for SDK", metadata=meta_data)
    <Volume(id=0601a32bf8f45646a5000000000000000000000688, name=vol-2)>
    >>>
    >>> pprint.pprint(client.volumes.list())
    [<Volume(id=0601a32bf8f45646a5000000000000000000000687, name=vol-1)>,
    <Volume(id=0601a32bf8f45646a5000000000000000000000688, name=vol-2)>]
    >>>
    >>> pprint.pprint(client.volumes.get("0601a32bf8f45646a5000000000000000000000687").attrs)
    {'access_control_records': None,
    'block_size': 4096,
    'creation_time': 1589770865,
    'dedupe_enabled': False,
    'description': '',
    'encryption_cipher': 'aes_256_xts',
    'full_name': 'default:/vol-1',
    'id': '0601a32bf8f45646a5000000000000000000000687',
     ...
    'iscsi_sessions': None,
    'limit': 100,
    'limit_iops': -1,
    'limit_mbps': -1,
    'metadata': None,
    'multi_initiator': False,
    'name': 'vol-1',
    'online': True,
    'perfpolicy_name': 'default',
    'pool_name': 'default',
    'read_only': False,
    'search_name': 'vol-1',
    'size': 10,
    'thinly_provisioned': True,
    'vol_state': 'online',
    'warn_level': 80}
    >>>
    >>> client.volumes.create("vol-3", size="1024", description="Test volume for SDK", metadata=meta_data)
    <Volume(id=0601a32bf8f45646a500000000000000000000070d, name=vol-3)>
    >>> vol = client.volumes.get(name="vol-3")
    <Volume(id=0601a32bf8f45646a500000000000000000000070d, name=vol-3)>
    >>>
    >>> pprint.pprint(vol.attrs['metadata'])
    [{'key': 'k1', 'value': 'v1'},
     {'key': 'k2', 'value': 'v2'},]
    >>> 
    >>> new_meta_data = {'foo': 'bar', 'tom': 'cat'}
    >>> vol.update(id="0601a32bf8f45646a500000000000000000000070d", metadata=new_meta_data)
    >>>
    >>> pprint.pprint(vol.attrs['metadata'])
    [{'key': 'k1', 'value': 'v1'},
     {'key': 'k2', 'value': 'v2'},
     {'key': 'foo', 'value': 'bar'},
     {'key': 'tom', 'value': 'cat'}]
    >>>
    >>> vol.offline()
    {'agent_type': 'none', 'app_category': 'Other', 'app_uuid': '', 'avg_stats_last_5mins': {'combined_iops': 0, 'combined_latency': 0, 'combined_throughput': 0, 'read_iops': 0, 'read_latency': 0, 'read_throughput': 0, 'write_iops': 0, 'write_latency': 0, 'write_throughput': 0}, 'base_snap_id': '', 'base_snap_name': '', 'block_size': 4096, 'cache_needed_for_pin': 10485760, 'cache_pinned': False, 'cache_policy': 'normal', 'caching_enabled': True, 'cksum_last_verified': 0, 'clone': False, 'content_repl_errors_found': False, 'creation_time': 1589770865, 'dedupe_enabled': False, 'description': '', 'dest_pool_id': '', 'dest_pool_name': '', 'encryption_cipher': 'aes_256_xts', 'folder_id': '', 'folder_name': '', 'full_name': 'default:/vol-1', 'id': '0601a32bf8f45646a5000000000000000000000687', 'last_content_snap_br_cg_uid': 0, 'last_content_snap_br_gid': 0, 'last_content_snap_id': 0, 'last_modified': 1589860023, 'last_replicated_snap': None, 'last_snap': None, 'limit': 100, 'limit_iops': -1, 'limit_mbps': -1, 'metadata': [{'key': 'foo', 'value': 'bar'}, {'key': 'tom', 'value': 'cat'}], 'move_aborting': False, 'move_bytes_migrated': 0, 'move_bytes_remaining': 0, 'move_est_compl_time': 0, 'move_start_time': 0, 'multi_initiator': False, 'name': 'vol-1', 'needs_content_repl': False, 'num_connections': 0, 'num_fc_connections': 0, 'num_iscsi_connections': 0, 'num_snaps': 0, 'offline_reason': 'user', 'online': False, 'online_snaps': None, 'owned_by_group': 'group-suneeth-vm1', 'owned_by_group_id': '0001a32bf8f45646a5000000000000000000000001', 'parent_vol_id': '', 'parent_vol_name': '', 'perfpolicy_id': '0301a32bf8f45646a5000000000000000000000001', 'perfpolicy_name': 'default', 'pinned_cache_size': 0, 'pool_id': '0a01a32bf8f45646a5000000000000000000000001', 'pool_name': 'default', 'previously_deduped': False, 'projected_num_snaps': 0, 'protection_type': 'unprotected', 'read_only': False, 'reserve': 0, 'search_name': 'vol-1', 'serial_number': '0a79f6e41098fea26c9ce9005d6df5f5', 'size': 10, 'snap_limit': 9223372036854775807, 'snap_limit_percent': -1, 'snap_reserve': 0, 'snap_usage_compressed_bytes': 0, 'snap_usage_populated_bytes': 0, 'snap_usage_uncompressed_bytes': 0, 'snap_warn_level': 0, 'space_usage_level': 'normal', 'target_name': 'iqn.2007-11.com.nimblestorage:vol-1-v01a32bf8f45646a5.00000687.f5f56d5d', 'thinly_provisioned': True, 'total_usage_bytes': 0, 'upstream_cache_pinned': False, 'usage_valid': True, 'vol_state': 'offline', 'vol_usage_compressed_bytes': 0, 'vol_usage_uncompressed_bytes': 0, 'volcoll_id': '', 'volcoll_name': '', 'vpd_ieee0': '0a79f6e41098fea2', 'vpd_ieee1': '6c9ce9005d6df5f5', 'vpd_t10': 'Nimble  0a79f6e41098fea26c9ce9005d6df5f5', 'warn_level': 80, 'iscsi_sessions': None, 'fc_sessions': None, 'access_control_records': None}
    >>> 
    >>> vol.delete()
    {}

    
**Query with simple URL filters and fields:**

.. code-block:: pycon

    >>> 
    >>> pprint.pprint(client.volumes.list(name="vol-1"))
    [<Volume(id=0601a32bf8f45646a5000000000000000000000687, name=vol-1)>]
    >>>
    >>> pprint.pprint(client.volumes.list(name="vol-1", detail=True, fields="name,id,size,online,clone")[0].attrs)
    {'clone': False,
     'id': '0601a32bf8f45646a5000000000000000000000687',
     'name': 'vol-1',
     'online': True,
     'size': 10}
    >>> 
    >>> pprint.pprint(client.volumes.list(
    ... detail=True,
    ... fields="name,size,online,metadata,limit_iops",
    ... size=1
    ... )[0].attrs)
    {'limit_iops': -1, 'metadata': None, 'name': 'v1', 'online': False, 'size': 1}
    >>>

**Query with complex filters and fields (Advanced Criteria):**

.. code-block:: pycon

    >>>
    >>> from nimbleclient.v1 import VolumeFields
    >>> 
    >>> pprint.pprint(client.volumes.list(filter=and_(VolumeFields.name.contains('vol-'))))
    [<Volume(id=0601a32bf8f45646a5000000000000000000000688, name=vol-2)>,
    <Volume(id=0601a32bf8f45646a5000000000000000000000687, name=vol-1)>]
    >>>>
    >>> filter1 = and_(
    ... VolumeFields.name.contains('pvc-'),
    ... VolumeFields.metadata("csp_ns_NIM_destroy_on_delete") == "false"
    ... )
    >>> pprint.pprint(client.volumes.list(
    ... detail=True,
    ... filter=filter1,
    ... fields="name,size,online,metadata,limit_iops",
    ... ))
    [<Volume(id=None, name=pvc-922040d3-563b-11ea-9000-005056966823)>,
    <Volume(id=None, name=pvc-92c6a7c5-4c2f-11ea-9000-005056966823)>]
    >>>
    >>> pprint.pprint(client.volumes.list(
    ... detail=True,
    ... filter=filter1,
    ... fields="name,size,online,metadata,limit_iops",
    ... )[0].attrs)
    {'limit_iops': -1,
    'metadata': [{'key': 'csp_ns_NIM_destroy_on_delete', 'value': 'false'},
              {'key': 'csp_ns_NIM_sync_on_detach', 'value': 'false'}],
    'name': 'pvc-922040d3-563b-11ea-9000-005056966823',
    'online': False,
    'size': 2048}
    >>>

**Muliple *_AND* and *_OR* operators can be used to construct more complex filters:**
.. code-block:: pycon

    >>> filter1 = and_(
    ...     VolumeFields.name.contains('pvc-'),
    ...     VolumeFields.online == True,
    ...     or_(
    ...         VolumeFields.app_uuid == 'container',
    ...         and_(
    ...             VolumeFields.size >= '4096',
    ...             VolumeFields.encryption_cipher == None,
    ...         )
    ...     )
    ... )

Contributing
------------

The Nimble Python SDK happily accepts contributions. Please see our
`contributing documentation <https://github.com/hpe-storage/nimble-python-sdk/blob/master/CONTRIBUTING.md>`
for some tips on getting started.


Maintainers
-----------

- `@suneeth51 <https://github.com/suneeth51>`__ (Suneethkumar Byadarahalli)
- `@ar-india <https://github.com/ar-india>`__ (Alok Ranjan)
- `@rgcostea <https://github.com/rgcostea>`__ (George Costea)

👋
