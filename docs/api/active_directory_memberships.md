# Table of Contents

* [nimbleclient.v1.api.active\_directory\_memberships](#nimbleclient.v1.api.active_directory_memberships)
  * [ActiveDirectoryMembership](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership)
    * [remove](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.remove)
    * [report\_status](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.report_status)
    * [test\_user](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.test_user)
    * [test\_group](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.test_group)
  * [ActiveDirectoryMembershipList](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList)
    * [remove](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.remove)
    * [report\_status](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.report_status)
    * [test\_user](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.test_user)
    * [test\_group](#nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.test_group)

<a name="nimbleclient.v1.api.active_directory_memberships"></a>
# nimbleclient.v1.api.active\_directory\_memberships

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership"></a>
## ActiveDirectoryMembership

```python
class ActiveDirectoryMembership(Resource)
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

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.remove"></a>
#### remove

```python
 | remove(password, user, **kwargs)
```

Leaves the Active Directory domain.

__Parameters__

- __id       __: ID of the active directory.
- __user     __: Name of the Activer Directory user with the privilege to leave the domain.
- __password __: Password for the Active Directory user.
- __force    __: Use this option when there is an error when leaving the domain.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.report_status"></a>
#### report\_status

```python
 | report_status(**kwargs)
```

Reports the detail status of the Active Directory domain.

__Parameters__

- __id __: ID of the active directory.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.test_user"></a>
#### test\_user

```python
 | test_user(name, **kwargs)
```

Tests whether the user exist in the Active Directory. If the user is present, then the user's group and role information is reported.

__Parameters__

- __id   __: ID of the Active Directory.
- __name __: Name of the Active Directory user.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembership.test_group"></a>
#### test\_group

```python
 | test_group(name, **kwargs)
```

Tests whether the user group exist in the Active Directory.

__Parameters__

- __id   __: ID of the Active Directory.
- __name __: Name of the Active Directory group.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList"></a>
## ActiveDirectoryMembershipList

```python
class ActiveDirectoryMembershipList(Collection)
```

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.remove"></a>
#### remove

```python
 | remove(id, password, user, **kwargs)
```

Leaves the Active Directory domain.

__Parameters__

- __id       __: ID of the active directory.
- __user     __: Name of the Activer Directory user with the privilege to leave the domain.
- __password __: Password for the Active Directory user.
- __force    __: Use this option when there is an error when leaving the domain.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.report_status"></a>
#### report\_status

```python
 | report_status(id, **kwargs)
```

Reports the detail status of the Active Directory domain.

__Parameters__

- __id __: ID of the active directory.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.test_user"></a>
#### test\_user

```python
 | test_user(id, name, **kwargs)
```

Tests whether the user exist in the Active Directory. If the user is present, then the user's group and role information is reported.

__Parameters__

- __id   __: ID of the Active Directory.
- __name __: Name of the Active Directory user.

<a name="nimbleclient.v1.api.active_directory_memberships.ActiveDirectoryMembershipList.test_group"></a>
#### test\_group

```python
 | test_group(id, name, **kwargs)
```

Tests whether the user group exist in the Active Directory.

__Parameters__

- __id   __: ID of the Active Directory.
- __name __: Name of the Active Directory group.

