# Table of Contents

* [nimbleclient.v1.api.key\_managers](#nimbleclient.v1.api.key_managers)
  * [KeyManager](#nimbleclient.v1.api.key_managers.KeyManager)
    * [remove](#nimbleclient.v1.api.key_managers.KeyManager.remove)
    * [migrate\_keys](#nimbleclient.v1.api.key_managers.KeyManager.migrate_keys)
  * [KeyManagerList](#nimbleclient.v1.api.key_managers.KeyManagerList)
    * [remove](#nimbleclient.v1.api.key_managers.KeyManagerList.remove)
    * [migrate\_keys](#nimbleclient.v1.api.key_managers.KeyManagerList.migrate_keys)

<a name="nimbleclient.v1.api.key_managers"></a>
# nimbleclient.v1.api.key\_managers

<a name="nimbleclient.v1.api.key_managers.KeyManager"></a>
## KeyManager

```python
class KeyManager(Resource)
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

<a name="nimbleclient.v1.api.key_managers.KeyManager.remove"></a>
#### remove

```python
 | remove(**kwargs)
```

Remove external key manager. You must migrate the keys to an inactive external key manager before removing the active key manager. If you remove the active external key
manager the passphrase is used to enable the internal key manager.

__Parameters__

- __id         __: ID of the external key manager.
- __passphrase __: Passphrase used to protect the master key, required during deletion of external key manager.

<a name="nimbleclient.v1.api.key_managers.KeyManager.migrate_keys"></a>
#### migrate\_keys

```python
 | migrate_keys(**kwargs)
```

Migrate volume encryption keys from the active key manager to the destination id given in the input. After successfully migrating the encryption keys, the destination key
manager is made the active key manager.

__Parameters__

- __id __: ID of the destination external key manager.

<a name="nimbleclient.v1.api.key_managers.KeyManagerList"></a>
## KeyManagerList

```python
class KeyManagerList(Collection)
```

<a name="nimbleclient.v1.api.key_managers.KeyManagerList.remove"></a>
#### remove

```python
 | remove(id, **kwargs)
```

Remove external key manager. You must migrate the keys to an inactive external key manager before removing the active key manager. If you remove the active external key
manager the passphrase is used to enable the internal key manager.

__Parameters__

- __id         __: ID of the external key manager.
- __passphrase __: Passphrase used to protect the master key, required during deletion of external key manager.

<a name="nimbleclient.v1.api.key_managers.KeyManagerList.migrate_keys"></a>
#### migrate\_keys

```python
 | migrate_keys(id, **kwargs)
```

Migrate volume encryption keys from the active key manager to the destination id given in the input. After successfully migrating the encryption keys, the destination key
manager is made the active key manager.

__Parameters__

- __id __: ID of the destination external key manager.

