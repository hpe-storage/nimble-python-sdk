
# nimbleclient.v1.api.master_key


## MasterKey
```python
MasterKey(self, id, attrs=None, client=None, collection=None)
```
Manage the master key. Data encryption keys for volumes are encrypted by using a master key that must be initialized before encrypted volumes can be created. The master key in
turn is protected by a passphrase that is set when the master key is created. The passphrase may have to be entered to enable the master key when it is not available, for
example, after an array reboot.

__Parameters__

- __id             __: Identifier of the master key.
- __name           __: Name of the master key. The only allowed value is "default".
- __passphrase     __: Passphrase used to protect the master key, required during creation, enabling/disabling the key and change the passphrase to a new value.
- __new_passphrase __: When changing the passphrase, this attribute specifies the new value of the passphrase.
- __active         __: Whether the master key is active or not.
- __purge_age      __: Default minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge keys immediately.


## MasterKeyList
```python
MasterKeyList(self, client=None)
```

