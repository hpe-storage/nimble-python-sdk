# Table of Contents

* [nimbleclient.v1.api.witnesses](#nimbleclient.v1.api.witnesses)
  * [Witness](#nimbleclient.v1.api.witnesses.Witness)
    * [test](#nimbleclient.v1.api.witnesses.Witness.test)
  * [WitnessList](#nimbleclient.v1.api.witnesses.WitnessList)
    * [test](#nimbleclient.v1.api.witnesses.WitnessList.test)

<a name="nimbleclient.v1.api.witnesses"></a>
# nimbleclient.v1.api.witnesses

<a name="nimbleclient.v1.api.witnesses.Witness"></a>
## Witness

```python
class Witness(Resource)
```

Manage witness host configuration.

__Parameters__

- __id                       __: Identifier of the witness configuration.
- __username                 __: Username of witness. This has to be a non-root that can login to the witness host.
- __password                 __: Password of witness.
- __host                     __: Hostname or ip addresses of witness.
- __port                     __: Port of witness.
- __secure_mode              __: To verify the witness host against CA cert and to apply possible security modes.
- __auto_switchover_messages __: List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found.

<a name="nimbleclient.v1.api.witnesses.Witness.test"></a>
#### test

```python
 | test(**kwargs)
```

Tests and validates witness configuration between the array and the witness.

__Parameters__

- __id __: ID of the witness.

<a name="nimbleclient.v1.api.witnesses.WitnessList"></a>
## WitnessList

```python
class WitnessList(Collection)
```

<a name="nimbleclient.v1.api.witnesses.WitnessList.test"></a>
#### test

```python
 | test(id, **kwargs)
```

Tests and validates witness configuration between the array and the witness.

__Parameters__

- __id __: ID of the witness.

