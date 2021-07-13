# Table of Contents

* [nimbleclient.v1.api.shelves](#nimbleclient.v1.api.shelves)
  * [Shelf](#nimbleclient.v1.api.shelves.Shelf)
    * [identify](#nimbleclient.v1.api.shelves.Shelf.identify)
    * [evacuate](#nimbleclient.v1.api.shelves.Shelf.evacuate)
  * [ShelfList](#nimbleclient.v1.api.shelves.ShelfList)
    * [identify](#nimbleclient.v1.api.shelves.ShelfList.identify)
    * [evacuate](#nimbleclient.v1.api.shelves.ShelfList.evacuate)

<a name="nimbleclient.v1.api.shelves"></a>
# nimbleclient.v1.api.shelves

<a name="nimbleclient.v1.api.shelves.Shelf"></a>
## Shelf

```python
class Shelf(Resource)
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

<a name="nimbleclient.v1.api.shelves.Shelf.identify"></a>
#### identify

```python
 | identify(cid, status, **kwargs)
```

Turn on chassis identifier for a controller.

__Parameters__

- __id     __: ID of shelf.
- __cid    __: Possible values: 'A', 'B'.
- __status __: Status value of identifier to set.

<a name="nimbleclient.v1.api.shelves.Shelf.evacuate"></a>
#### evacuate

```python
 | evacuate(driveset, **kwargs)
```

Perform shelf evacuation.

__Parameters__

- __id       __: ID of shelf.
- __driveset __: Driveset to evacuate.
- __dry_run  __: Argument to perform a dry run, not the actual shelf evacuation.
- __start    __: Argument to perform the shelf evacuation.
- __cancel   __: Argument to cancel the shelf evacuation.
- __pause    __: Argument to pause the shelf evacuation.
- __resume   __: Argument to resume the shelf evacuation.

<a name="nimbleclient.v1.api.shelves.ShelfList"></a>
## ShelfList

```python
class ShelfList(Collection)
```

<a name="nimbleclient.v1.api.shelves.ShelfList.identify"></a>
#### identify

```python
 | identify(id, cid, status, **kwargs)
```

Turn on chassis identifier for a controller.

__Parameters__

- __id     __: ID of shelf.
- __cid    __: Possible values: 'A', 'B'.
- __status __: Status value of identifier to set.

<a name="nimbleclient.v1.api.shelves.ShelfList.evacuate"></a>
#### evacuate

```python
 | evacuate(id, driveset, **kwargs)
```

Perform shelf evacuation.

__Parameters__

- __id       __: ID of shelf.
- __driveset __: Driveset to evacuate.
- __dry_run  __: Argument to perform a dry run, not the actual shelf evacuation.
- __start    __: Argument to perform the shelf evacuation.
- __cancel   __: Argument to cancel the shelf evacuation.
- __pause    __: Argument to pause the shelf evacuation.
- __resume   __: Argument to resume the shelf evacuation.

