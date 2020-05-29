
# nimbleclient.v1.api.network_interfaces


## NetworkInterface
```python
NetworkInterface(self, id, attrs=None, client=None, collection=None)
```
Manage per array network interface configuration.

__Parameters__

- __id                   __: Identifier for the interface.
- __array_name_or_serial __: Name or serial of the array where the interface is hosted.
- __partial_response_ok  __: Indicate that it is ok to provide partially available response.
- __array_id             __: Identifier for the array.
- __controller_name      __: Name (A or B) of the controller where the interface is hosted.
- __controller_id        __: Identifier of the controller where the interface is hosted.
- __name                 __: Name of the interface.
- __mac                  __: MAC address of the interface.
- __is_present           __: Whether this interface is present on this controller.
- __link_speed           __: Speed of the link.
- __link_status          __: Status of the link.
- __mtu                  __: MTU on the link.
- __port                 __: Port number for this interface.
- __slot                 __: Slot number for this interface.
- __max_link_speed       __: Maximum speed of the link.
- __nic_type             __: Interface type.
- __ip_list              __: List of IP addresses assigned to this network interface.


## NetworkInterfaceList
```python
NetworkInterfaceList(self, client=None)
```

