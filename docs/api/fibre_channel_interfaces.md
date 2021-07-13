# Table of Contents

* [nimbleclient.v1.api.fibre\_channel\_interfaces](#nimbleclient.v1.api.fibre_channel_interfaces)
  * [FibreChannelInterface](#nimbleclient.v1.api.fibre_channel_interfaces.FibreChannelInterface)

<a name="nimbleclient.v1.api.fibre_channel_interfaces"></a>
# nimbleclient.v1.api.fibre\_channel\_interfaces

<a name="nimbleclient.v1.api.fibre_channel_interfaces.FibreChannelInterface"></a>
## FibreChannelInterface

```python
class FibreChannelInterface(Resource)
```

Represent information of specified Fibre Channel interfaces. Fibre Channel interfaces are hosted on Fibre Channel ports to provide data access.

__Parameters__

- __id                   __: Identifier for the Fibre Channel interface.
- __array_name_or_serial __: Name or serial number of array where the interface is hosted.
- __partial_response_ok  __: Indicate that it is ok to provide partially available response.
- __controller_name      __: Name (A or B) of the controller where the interface is hosted.
- __fc_port_id           __: ID of the port with which the interface is associated.
- __name                 __: Name of Fibre Channel interface.
- __wwnn                 __: WWNN (World Wide Node Name) for this Fibre Channel interface.
- __wwpn                 __: WWPN (World Wide Port Name) for this Fibre Channel interface.
- __peerzone             __: Active peer zone for this Fibre Channel interface.
- __online               __: Identify whether the Fibre Channel interface is online.
- __firmware_version     __: Version of the Fibre Channel firmware.
- __logical_port_number  __: Logical port number for the Fibre Channel port.
- __fc_port_name         __: Name of Fibre Channel port.
- __bus_location         __: PCI bus location of the HBA for this Fibre Channel port.
- __slot                 __: HBA slot number for this Fibre Channel port.
- __orientation          __: Orientation of FC ports on a HBA. An orientation of 'right_to_left' indicates that ports are ordered as 3,2,1,0 on the slot. Possible values:
                       'left_to_right', 'right_to_left'.
- __port                 __: HBA port number for this Fibre Channel port.
- __link_info            __: Information about the Fibre Channel link at which interface is operating.
- __fabric_info          __: Fibre Channel fabric information.

