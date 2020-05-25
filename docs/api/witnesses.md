
# nimbleclient.v1.api.witnesses


## Witness
```python
Witness(self, id, attrs=None, client=None, collection=None)
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


## WitnessList
```python
WitnessList(self, client=None)
```

