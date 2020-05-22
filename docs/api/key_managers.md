
# nimbleclient.v1.api.key_managers


## KeyManager
```python
KeyManager(self, id, attrs=None, client=None, collection=None)
```
Key Manager stores encryption keys for the array volumes / dedupe domains.

__Parameters__

- __id          __: Identifier for External Key Manager.
- __name        __: Name of external key manager.
- __description __: Description of external key manager.
- __hostname    __: Hostname or IP Address for the External Key Manager.
- __port        __: Port number for the External Key Manager.
- __protocol    __: KMIP protocol supported by External Key Manager.
- __username    __: External Key Manager username. String up to 255 printable characters.
- __password    __: External Key Manager user password. String up to 255 printable characters.
- __active      __: Whether the given key manager is active or not.
- __status      __: Connection status of a given external key manager.
- __vendor      __: KMIP vendor name.


## KeyManagerList
```python
KeyManagerList(self, client=None)
```

