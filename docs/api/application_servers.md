
# nimbleclient.v1.api.application_servers


## ApplicationServer
```python
ApplicationServer(self, id, attrs=None, client=None, collection=None)
```
An application server is an external agent that collaborates with an array to manage storage resources; for example, Volume Shadow Copy Service (VSS) or VMware.

__Parameters__

- __id            __: Identifier for the application server.
- __name          __: Name for the application server.
- __hostname      __: Application server hostname.
- __port          __: Application server port number.
- __username      __: Application server username.
- __description   __: Text description of application server.
- __password      __: Application server password.
- __server_type   __: Application server type ({invalid|vss|vmware|cisco|stack_vision|container_node}).
- __metadata      __: Key-value pairs that augment an application server's attributes.
- __creation_time __: Time when this application server was created.
- __last_modified __: Time when this application server was last modified.


## ApplicationServerList
```python
ApplicationServerList(self, client=None)
```

