
# nimbleclient.v1.api.active_directory_memberships


## ActiveDirectoryMembership
```python
ActiveDirectoryMembership(self,
                          id,
                          attrs=None,
                          client=None,
                          collection=None)
```
Manages the storage array's membership with the Active Directory.

__Parameters__

- __id                  __: Identifier for the Active Directory Domain.
- __description         __: Description for the Active Directory Domain.
- __name                __: Identifier for the Active Directory domain.
- __netbios             __: Netbios name for the Active Directory domain.
- __server_list         __: List of IP addresses or names for the backup domain controller.
- __computer_name       __: The name of the computer account in the domain controller.
- __organizational_unit __: The location for the computer account.
- __user                __: Name of the Activer Directory user with Administrator's privilege.
- __password            __: Password for the Active Directory user.
- __enabled             __: Active Directory authentication is currently enabled.


## ActiveDirectoryMembershipList
```python
ActiveDirectoryMembershipList(self, client=None)
```

