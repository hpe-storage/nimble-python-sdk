# Table of Contents

* [nimbleclient.v1.api.space\_domains](#nimbleclient.v1.api.space_domains)
  * [SpaceDomain](#nimbleclient.v1.api.space_domains.SpaceDomain)

<a name="nimbleclient.v1.api.space_domains"></a>
# nimbleclient.v1.api.space\_domains

<a name="nimbleclient.v1.api.space_domains.SpaceDomain"></a>
## SpaceDomain

```python
class SpaceDomain(Resource)
```

A space domain is created for each application category and block size for each each pool.

__Parameters__

- __id                       __: Identifier for the space domain.
- __pool_id                  __: Identifier associated with the pool in the storage pool table.
- __pool_name                __: Name of the pool containing the space domain.
- __app_category_id          __: Identifier of the application category associated with the space domain.
- __app_category_name        __: Name of the application category associated with the space domain.
- __perf_policy_names        __: Name of the performance policies associated with the space domain.
- __sample_rate              __: Sample rate value.
- __volume_count             __: Number of volumes belonging to the space domain.
- __deduped_volume_count     __: Number of deduplicated volumes belonging to the space domain.
- __volumes                  __: Volumes belonging to the space domain.
- __block_size               __: Block size in bytes of volumes belonging to the space domain.
- __deduped                  __: Volumes in space domain are deduplicated by default.
- __encrypted                __: Volumes in space domain are encrypted.
- __usage                    __: Physical space usage of volumes in the space domain.
- __vol_logical_usage        __: Logical usage of volumes in the space domain.
- __snap_logical_usage       __: Logical usage of snapshots in the space domain.
- __vol_mapped_usage         __: Mapped usage of volumes in the space domain, useful for computing clone savings.
- __logical_dedupe_usage     __: Logical space usage of volumes when deduped.
- __physical_dedupe_usage    __: Physical space usage of volumes including snapshots when deduped.
- __savings_compression      __: Space usage savings in the space domain due to compression.
- __savings_dedupe           __: Space usage savings in the space domain due to deduplication.
- __savings_clone            __: Space usage savings in the space domain due to cloning of volumes.
- __compressed_usage_bytes   __: Compressed usage of volumes and snapshots in the space domain.
- __uncompressed_usage_bytes __: Uncompressed usage of volumes and snapshots in the space domain.
- __compression_ratio        __: Compression savings for the space domain expressed as ratio.
- __dedupe_ratio             __: Deduplication savings for the space domain expressed as ratio.
- __clone_ratio              __: Clone savings for the space domain expressed as ratio.

