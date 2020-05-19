
# nimbleclient.v1.api.software_versions


## SoftwareVersion
```python
SoftwareVersion(self, id, attrs=None, client=None, collection=None)
```
Show the software version.

__Parameters__

- __version                __: Software version, used as identifier in URL.
- __signature              __: Keyed hash of download package.
- __name                   __: Name of version.
- __status                 __: Status of version.
- __total_bytes            __: Size of version.
- __downloaded_bytes       __: Number of bytes downloaded for the version.
- __blacklist_reason       __: Reason for blacklisting the version. Empty if version is not blacklisted.
- __release_date           __: Date when software version was released.
- __is_manually_downloaded __: Whether or not the version was downloaded manually.
- __release_status         __: Release status of software version.
- __no_partial_response    __: Indicate that it is not ok to provide partially available response.


## SoftwareVersionList
```python
SoftwareVersionList(self, client=None)
```

