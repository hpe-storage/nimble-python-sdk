# Table of Contents

* [nimbleclient.v1.api.master\_key](#nimbleclient.v1.api.master_key)
  * [MasterKey](#nimbleclient.v1.api.master_key.MasterKey)
    * [purge\_inactive](#nimbleclient.v1.api.master_key.MasterKey.purge_inactive)
  * [MasterKeyList](#nimbleclient.v1.api.master_key.MasterKeyList)
    * [purge\_inactive](#nimbleclient.v1.api.master_key.MasterKeyList.purge_inactive)

<a name="nimbleclient.v1.api.master_key"></a>
# nimbleclient.v1.api.master\_key

<a name="nimbleclient.v1.api.master_key.MasterKey"></a>
## MasterKey

```python
class MasterKey(Resource)
```

Manage the master key. Data encryption keys for volumes are encrypted by using a master key that must be initialized before encrypted volumes can be created. The master key in
turn is protected by a passphrase that is set when the master key is created. The passphrase may have to be entered to enable the master key when it is not available, for
example, after an array reboot.

__Parameters__

- __id             __: Identifier of the master key.
- __name           __: Name of the master key. The only allowed value is "default".
- __passphrase     __: Passphrase used to protect the master key, required during creation, enabling/disabling the key and change the passphrase to a new value.
- __halfkey        __: When changing the passphrase, this authenticates the change operation, for support use only.
- __new_passphrase __: When changing the passphrase, this attribute specifies the new value of the passphrase.
- __active         __: Whether the master key is active or not.
- __purge_age      __: Default minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge keys immediately.

<a name="nimbleclient.v1.api.master_key.MasterKey.purge_inactive"></a>
#### purge\_inactive

```python
 | purge_inactive(**kwargs)
```

Purges encryption keys that have been inactive for the age or longer. If you do not specify an age, the keys will be purged immediately.

__Parameters__

- __id  __: Identifier for the master key.
- __age __: Minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge the keys immediately.

<a name="nimbleclient.v1.api.master_key.MasterKeyList"></a>
## MasterKeyList

```python
class MasterKeyList(Collection)
```

<a name="nimbleclient.v1.api.master_key.MasterKeyList.purge_inactive"></a>
#### purge\_inactive

```python
 | purge_inactive(id, **kwargs)
```

Purges encryption keys that have been inactive for the age or longer. If you do not specify an age, the keys will be purged immediately.

__Parameters__

- __id  __: Identifier for the master key.
- __age __: Minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge the keys immediately.

