
# nimbleclient.v1.api.events


## Event
```python
Event(self, id, attrs=None, client=None, collection=None)
```
View events.

__Parameters__

- __id          __: Identifier for the event record.
- __type        __: Type of the event record.
- __name        __: Name of alert macro to generate.
- __scope       __: The array name for array level event.
- __target      __: Name of object upon which the event occurred.
- __target_type __: Target type of the event record.
- __timestamp   __: Time when this event happened.
- __category    __: Category of the event record.
- __severity    __: Severity level of the event.
- __summary     __: Summary of the event.
- __activity    __: Description of the event.
- __alarm_id    __: The alarm ID if the event is related to an alarm.
- __params      __: Arguments provided for event creation in key-value structure. Until KV implementation for events, will ignore keys (though keys must be non-empty) and take
              values positionally.
- __tenant_id   __: Tenant ID of the event. This is used to determine what tenant context the event belongs to.


## EventList
```python
EventList(self, client=None)
```

