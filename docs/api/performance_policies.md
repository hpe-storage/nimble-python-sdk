# Table of Contents

* [nimbleclient.v1.api.performance\_policies](#nimbleclient.v1.api.performance_policies)
  * [PerformancePolicy](#nimbleclient.v1.api.performance_policies.PerformancePolicy)

<a name="nimbleclient.v1.api.performance_policies"></a>
# nimbleclient.v1.api.performance\_policies

<a name="nimbleclient.v1.api.performance_policies.PerformancePolicy"></a>
## PerformancePolicy

```python
class PerformancePolicy(Resource)
```

Manage performance policies. A performance policy is a set of optimizations including block size, compression, and caching, to ensure that the volume's performance is the best
configuration for its intended use like databases or log files. By default, a volume uses the \\"default\\" performance policy, which is set to use 4096 byte blocks with full
compression and caching enabled. For replicated volumes, the same performance policy must exist on each replication partner.

__Parameters__

- __id                    __: Unique Identifier for the Performance Policy.
- __name                  __: Name of the Performance Policy.
- __full_name             __: Fully qualified name of the Performance Policy.
- __search_name           __: Name of the Performance Policy used for object search.
- __description           __: Description of a performance policy.
- __block_size            __: Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8
                        KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created.
- __compress              __: Flag denoting if data in the associated volume should be compressed.
- __cache                 __: Flag denoting if data in the associated volume should be cached.
- __cache_policy          __: Specifies how data of associated volume should be cached. Supports two policies, 'normal' and 'aggressive'. 'normal' policy caches data but skips in
                        certain conditions such as sequential I/O. 'aggressive' policy will accelerate caching of all data belonging to this volume, regardless of
                        sequentiality.
- __space_policy          __: Specifies the state of the volume upon space constraint violation such as volume limit violation or volumes above their volume reserve, if the pool
                        free space is exhausted. Supports two policies, 'offline' and 'non_writable'.
- __app_category          __: Specifies the application category of the associated volume.
- __dedupe_enabled        __: Specifies if dedupe is enabled for volumes created with this performance policy.
- __deprecated            __: Specifies if this performance policy is deprecated.
- __predefined            __: Specifies if this performance policy is predefined (read-only).
- __creation_time         __: Time when the performance policy was created.
- __last_modified         __: Time when the performance policy's configurations were last modified.
- __sample_rate           __: Sample rate value.
- __volume_count          __: Number of volumes using this performance policy.
- __dedupe_override_pools __: List of pools that override performance policy's dedupe setting.

