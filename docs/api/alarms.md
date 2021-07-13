# Table of Contents

* [nimbleclient.v1.api.alarms](#nimbleclient.v1.api.alarms)
  * [Alarm](#nimbleclient.v1.api.alarms.Alarm)
    * [acknowledge](#nimbleclient.v1.api.alarms.Alarm.acknowledge)
    * [unacknowledge](#nimbleclient.v1.api.alarms.Alarm.unacknowledge)
  * [AlarmList](#nimbleclient.v1.api.alarms.AlarmList)
    * [acknowledge](#nimbleclient.v1.api.alarms.AlarmList.acknowledge)
    * [unacknowledge](#nimbleclient.v1.api.alarms.AlarmList.unacknowledge)

<a name="nimbleclient.v1.api.alarms"></a>
# nimbleclient.v1.api.alarms

<a name="nimbleclient.v1.api.alarms.Alarm"></a>
## Alarm

```python
class Alarm(Resource)
```

View alarms.

__Parameters__

- __id                     __: Identifier for the alarm.
- __type                   __: Identifier for type of alarm.
- __array                  __: The array name where the alarm is generated.
- __curr_onset_event_id    __: Identifier for the current onset event.
- __object_id              __: Identifier of object operated upon.
- __object_name            __: Name of object operated upon.
- __object_type            __: Type of the object being operated upon.
- __onset_time             __: Time when this alarm was triggered.
- __ack_time               __: Time when this alarm was acknowledged.
- __status                 __: Status of the operation -- open or acknowledged.
- __user_id                __: Identifier of the user who acknowledged the alarm.
- __user_name              __: Username of the user who acknowledged the alarm.
- __user_full_name         __: Full name of the user who acknowledged the alarm.
- __category               __: Category of the alarm.
- __severity               __: Severity level of the event.
- __remind_every           __: Frequency of notification. This number and the remind_every_unit define how frequent one alarm notification is sent. For example, a value of 1 with
                         the 'remind_every_unit' of 'days' results in one notification every day.
- __remind_every_unit      __: Time unit over which to send the number of notification specified in 'remind_every'. For example, a value of 'days' with a 'remind_every' of '1'
                         results in one notification every day.
- __activity               __: Description of activity performed and recorded in alarm.
- __next_notification_time __: Time when next reminder for the alarm will be sent.

<a name="nimbleclient.v1.api.alarms.Alarm.acknowledge"></a>
#### acknowledge

```python
 | acknowledge(**kwargs)
```

Acknowledge an alarm.

__Parameters__

- __id                __: ID of the acknowledged alarm.
- __remind_every      __: Notification frequency unit.
- __remind_every_unit __: Period unit.

<a name="nimbleclient.v1.api.alarms.Alarm.unacknowledge"></a>
#### unacknowledge

```python
 | unacknowledge(**kwargs)
```

Unacknowledge an alarm.

__Parameters__

- __id __: ID of the acknowledged alarm.

<a name="nimbleclient.v1.api.alarms.AlarmList"></a>
## AlarmList

```python
class AlarmList(Collection)
```

<a name="nimbleclient.v1.api.alarms.AlarmList.acknowledge"></a>
#### acknowledge

```python
 | acknowledge(id, **kwargs)
```

Acknowledge an alarm.

__Parameters__

- __id                __: ID of the acknowledged alarm.
- __remind_every      __: Notification frequency unit.
- __remind_every_unit __: Period unit.

<a name="nimbleclient.v1.api.alarms.AlarmList.unacknowledge"></a>
#### unacknowledge

```python
 | unacknowledge(id, **kwargs)
```

Unacknowledge an alarm.

__Parameters__

- __id __: ID of the acknowledged alarm.

