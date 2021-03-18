
# nimbleclient.v1.api.subscribers


## Subscriber
```python
Subscriber(self, id, attrs=None, client=None, collection=None)
```
Subscribers are websocket based notification clients that can subscribe to interesting operations and events and recieve notifications whenever the subscribed to operations
and events happen on the array.

__Parameters__

- __id                     __: Identifier for subscriber.
- __type                   __: This is generally used to indicate the type of subscriber e.g. SMIS/GUI/ThirdParty etc. This is free form and doesn't need to be unique.
- __renew_interval         __: The interval in seconds within which the subscriber is expected to send a renew message over the websocket channel in case there is no traffic on the
                         websocket channel.
- __renew_response_timeout __: The interval in seconds after the subscriber sends a renew message within which the subscriber expects to get a response.
- __is_connected           __: True if the subscriber has an active websocket connection.
- __notification_count     __: Number of notifications sent to subscriber.
- __force                  __: Forcibly modify a connected subscriber.


## SubscriberList
```python
SubscriberList(self, client=None)
```

