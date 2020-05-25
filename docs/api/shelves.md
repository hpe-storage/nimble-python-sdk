
# nimbleclient.v1.api.shelves


## Shelf
```python
Shelf(self, id, attrs=None, client=None, collection=None)
```
Disk shelf and head unit houses disks and controller.

__Parameters__

- __id                   __: ID of shelf.
- __array_name           __: Name of array the shelf belongs to.
- __array_id             __: ID of array the shelf belongs to.
- __partial_response_ok  __: Indicate that it is okay to provide partially available response.
- __chassis_type         __: Chassis type.
- __ctrlrs               __: List of ctrlr info.
- __serial               __: The serial number of the chassis.
- __model                __: Model of the shelf or head unit.
- __model_ext            __: Extended model of the shelf or head unit.
- __chassis_sensors      __: List of chassis sensor readings.
- __psu_overall_status   __: The overall status for the PSUs.
- __fan_overall_status   __: The overall status for the fans on both controllers.
- __temp_overall_status  __: The overall status for the temperature on both controllers.
- __disk_sets            __: Attributes for the disk sets in this shelf.
- __activated            __: Activated state for shelf or disk set means it is available to store date on. An activated shelf may not be deactivated.
- __driveset             __: Driveset to activate.
- __force                __: Forcibly activate shelf.
- __accept_foreign       __: Accept the removal of data on the shelf disks and activate foreign shelf.
- __accept_dedupe_impact __: Accept the reduction or elimination of deduplication capability on the system as a result of activating a shelf that does not meet the necessary
                       deduplication requirements.
- __last_request         __: Indicates this is the last request in a series of shelf add requests.


## ShelfList
```python
ShelfList(self, client=None)
```

