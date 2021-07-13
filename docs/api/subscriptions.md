# Table of Contents

* [nimbleclient.v1.api.subscriptions](#nimbleclient.v1.api.subscriptions)
  * [Subscription](#nimbleclient.v1.api.subscriptions.Subscription)

<a name="nimbleclient.v1.api.subscriptions"></a>
# nimbleclient.v1.api.subscriptions

<a name="nimbleclient.v1.api.subscriptions.Subscription"></a>
## Subscription

```python
class Subscription(Resource)
```

Subscriptions represent the list of object types or alerts that a websocket client is interested in getting notifications for. Each subscription belongs to a single
notification client.

__Parameters__

- __id                __: Identifier for subscription.
- __subscriber_id     __: Identifier for subscriber (notification client) that this subscription belongs to.
- __notification_type __: This indicates the type of notification being subscribed for.
- __object_type       __: The object type that the notification subscriber is interested in. This is relevant for and required only for audit log based notifications.
- __object_id         __: The object that the notification subscriber is interested in. Applies only to audit log based notifications.
- __operation         __: The operation that the notification subscriber is interested in. Applies only to audit log based notifications.
- __event_target_type __: The kind of events or alerts that the notification subscriber is interested in. Applies only to events based notifications.
- __event_severity    __: The severity of events that the notification subscriber is interested in. Applies only to events based notifications.

