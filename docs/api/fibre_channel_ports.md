# Table of Contents

* [nimbleclient.v1.api.fibre\_channel\_ports](#nimbleclient.v1.api.fibre_channel_ports)
  * [FibreChannelPort](#nimbleclient.v1.api.fibre_channel_ports.FibreChannelPort)

<a name="nimbleclient.v1.api.fibre_channel_ports"></a>
# nimbleclient.v1.api.fibre\_channel\_ports

<a name="nimbleclient.v1.api.fibre_channel_ports.FibreChannelPort"></a>
## FibreChannelPort

```python
class FibreChannelPort(Resource)
```

Fibre Channel ports provide data access. This API provides the list of all Fibre Channel ports configured on the arrays.

__Parameters__

- __id                   __: Identifier for the Fibre Channel port.
- __array_name_or_serial __: Name or serial number of the array.
- __controller_name      __: Name (A or B) of the controller to which the port belongs.
- __fc_port_name         __: Name of the Fibre Channel port.
- __bus_location         __: PCI bus location of the HBA (Host Bus Adapter) for this Fibre Channel port.
- __port                 __: HBA (Host Bus Adapter) port number for this Fibre Channel port.
- __slot                 __: HBA (Host Bus Adapter) slot number for this Fibre Channel port.
- __orientation          __: Orientation of FC ports on a HBA. An orientation of 'right_to_left' indicates that ports are ordered as 3,2,1,0 on the slot. Possible values:
                       'left_to_right', 'right_to_left'.
- __link_info            __: Information about the Fibre Channel link associated with this port.
- __rx_power             __: SFP RX power in uW.
- __tx_power             __: SFP TX power in uW.

