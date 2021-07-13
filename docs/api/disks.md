# Table of Contents

* [nimbleclient.v1.api.disks](#nimbleclient.v1.api.disks)
  * [Disk](#nimbleclient.v1.api.disks.Disk)

<a name="nimbleclient.v1.api.disks"></a>
# nimbleclient.v1.api.disks

<a name="nimbleclient.v1.api.disks.Disk"></a>
## Disk

```python
class Disk(Resource)
```

Disks are used for storing user data.

__Parameters__

- __id                        __: ID of disk.
- __is_dfc                    __: Is disk part of dual flash carrier.
- __serial                    __: Disk serial number(N/A if empty).
- __path                      __: Disk SCSI device path.
- __shelf_serial              __: Serial number of the shelf the disk is attached to.
- __shelf_location            __: Identifies the controller, port, and chain position of the shelf the disk belongs to.
- __shelf_id                  __: Identifies the physical shelf the disk belongs to.
- __shelf_location_id         __: Identifies the position shelf the disk belongs to, as coded integer.
- __vshelf_id                 __: Identifies the local shelf ID the disk belongs to.
- __slot                      __: Disk slot number.
- __bank                      __: Disk bank number.
- __model                     __: Disk model name.
- __vendor                    __: Vendor name of the disk manufacturer.
- __firmware_version          __: Firmware version on the disk.
- __hba                       __: HBA ID the disk is connected to.
- __port                      __: HBA port number the disk is connected to.
- __size                      __: Disk size in bytes.
- __state                     __: Disk hardware state.
- __type                      __: Type of disk (HDD, SSD, N/A).
- __block_type                __: Native block type of the disk.
- __raid_id                   __: Raid ID.
- __raid_resync_percent       __: Percentage RAID rebuild completed on this disk.
- __raid_resync_current_speed __: Current RAID rebuild speed (bytes/sec).
- __raid_resync_average_speed __: Average RAID rebuild speed (bytes/sec).
- __raid_state                __: RAID status for the disk (N/A, okay, resynchronizing, spare, faulty).
- __disk_internal_stat_1      __: Internal disk statistic 1.
- __smart_attribute_list      __: S.M.A.R.T. attributes for the disk.
- __disk_op                   __: The intended operation to be performed on the specified disk.
- __force                     __: Forcibly add a disk.
- __array_name                __: Name of array the disk belongs to.
- __array_id                  __: ID of array the disk belongs to.
- __partial_response_ok       __: Indicate that it is okay to provide partially available response.

