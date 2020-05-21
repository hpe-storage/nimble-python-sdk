#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection
from ...exceptions import NimOSAPIOperationUnsupported


class Disk(Resource):
    """Disks are used for storing user data.

    # Parameters
    id                        : ID of disk.
    is_dfc                    : Is disk part of dual flash carrier.
    serial                    : Disk serial number(N/A if empty).
    path                      : Disk SCSI device path.
    shelf_serial              : Serial number of the shelf the disk is attached to.
    shelf_location            : Identifies the controller, port, and chain position of the shelf the disk belongs to.
    shelf_id                  : Identifies the physical shelf the disk belongs to.
    shelf_location_id         : Identifies the position shelf the disk belongs to, as coded integer.
    vshelf_id                 : Identifies the local shelf ID the disk belongs to.
    slot                      : Disk slot number.
    bank                      : Disk bank number.
    model                     : Disk model name.
    vendor                    : Vendor name of the disk manufacturer.
    firmware_version          : Firmware version on the disk.
    hba                       : HBA ID the disk is connected to.
    port                      : HBA port number the disk is connected to.
    size                      : Disk size in bytes.
    state                     : Disk hardware state.
    type                      : Type of disk (HDD, SSD, N/A).
    block_type                : Native block type of the disk.
    raid_id                   : Raid ID.
    raid_resync_percent       : Percentage RAID rebuild completed on this disk.
    raid_resync_current_speed : Current RAID rebuild speed (bytes/sec).
    raid_resync_average_speed : Average RAID rebuild speed (bytes/sec).
    raid_state                : RAID status for the disk (N/A, okay, resynchronizing, spare, faulty).
    disk_internal_stat_1      : Internal disk statistic 1.
    smart_attribute_list      : S.M.A.R.T. attributes for the disk.
    disk_op                   : The intended operation to be performed on the specified disk.
    force                     : Forcibly add a disk.
    array_name                : Name of array the disk belongs to.
    array_id                  : ID of array the disk belongs to.
    partial_response_ok       : Indicate that it is okay to provide partially available response.
    """

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")


class DiskList(Collection):
    resource = Disk
    resource_type = "disks"

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")