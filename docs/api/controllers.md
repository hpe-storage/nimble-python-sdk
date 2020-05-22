
# nimbleclient.v1.api.controllers


## Controller
```python
Controller(self, id, attrs=None, client=None, collection=None)
```
Controller is a redundant collection of hardware capable of running the array software.

__Parameters__

- __id                  __: Identifier of the controller.
- __name                __: Name of the controller.
- __array_name          __: Name of the array containing this controller.
- __array_id            __: Rest ID of the array containing this controller.
- __partial_response_ok __: Indicate that it is ok to provide partially available response.
- __serial              __: Serial number for this controller.
- __hostname            __: Host name for the controller.
- __support_address     __: IP address used for support.
- __support_netmask     __: IP netmask used for support.
- __support_nic         __: Network card used for support.
- __power_status        __: Overall power supply status for the controller.
- __fan_status          __: Overall fan status for the controller.
- __temperature_status  __: Overall temperature status for the controller.
- __power_supplies      __: Status for each power supply in the controller.
- __fans                __: Status for each fan in the controller.
- __temperature_sensors __: Status for temperature sensor in the controller.
- __partition_status    __: Status of the system's raid partitions.
- __ctrlr_side          __: Identifies which controller this is on its array.
- __state               __: Indicates whether this controller is active or not.
- __nvme_cards_enabled  __: Indicates if the NVMe accelerator card is enabled.
- __nvme_cards          __: List of NVMe accelerator cards.
- __asup_time           __: Time of the last autosupport by the controller.


## ControllerList
```python
ControllerList(self, client=None)
```

