#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class MasterKey(Resource):
    """Manage the master key. Data encryption keys for volumes are encrypted by using a master key that must be initialized before encrypted volumes can be created. The master key in
    turn is protected by a passphrase that is set when the master key is created. The passphrase may have to be entered to enable the master key when it is not available, for
    example, after an array reboot.

    # Parameters
    id             : Identifier of the master key.
    name           : Name of the master key. The only allowed value is "default".
    passphrase     : Passphrase used to protect the master key, required during creation, enabling/disabling the key and change the passphrase to a new value.
    new_passphrase : When changing the passphrase, this attribute specifies the new value of the passphrase.
    active         : Whether the master key is active or not.
    purge_age      : Default minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge keys immediately.
    """
    def purge_inactive(self, **kwargs):
        """Purges encryption keys that have been inactive for the age or longer. If you do not specify an age, the keys will be purged immediately.

        # Parameters
        id  : Identifier for the master key.
        age : Minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge the keys immediately.
        """

        return self._collection.purge_inactive(
            self.id,
            **kwargs
        )


class MasterKeyList(Collection):
    resource = MasterKey
    resource_type = "master_key"

    def purge_inactive(self, id, **kwargs):
        """Purges encryption keys that have been inactive for the age or longer. If you do not specify an age, the keys will be purged immediately.

        # Parameters
        id  : Identifier for the master key.
        age : Minimum age (in hours) of inactive encryption keys to be purged. '0' indicates to purge the keys immediately.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'purge_inactive',
            id=id,
            **kwargs
        )
