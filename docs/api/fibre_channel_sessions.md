# Table of Contents

* [nimbleclient.v1.api.fibre\_channel\_sessions](#nimbleclient.v1.api.fibre_channel_sessions)
  * [FibreChannelSession](#nimbleclient.v1.api.fibre_channel_sessions.FibreChannelSession)

<a name="nimbleclient.v1.api.fibre_channel_sessions"></a>
# nimbleclient.v1.api.fibre\_channel\_sessions

<a name="nimbleclient.v1.api.fibre_channel_sessions.FibreChannelSession"></a>
## FibreChannelSession

```python
class FibreChannelSession(Resource)
```

Fibre Channel session is created when Fibre Channel initiator connects to this group.

__Parameters__

- __id             __: Unique identifier of the Fibre Channel session.
- __initiator_info __: Information about the Fibre Channel initiator.
- __target_info    __: Information about the Fibre Channel target.

