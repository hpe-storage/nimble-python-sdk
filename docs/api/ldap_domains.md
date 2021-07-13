# Table of Contents

* [nimbleclient.v1.api.ldap\_domains](#nimbleclient.v1.api.ldap_domains)
  * [LdapDomain](#nimbleclient.v1.api.ldap_domains.LdapDomain)
    * [test\_user](#nimbleclient.v1.api.ldap_domains.LdapDomain.test_user)
    * [test\_group](#nimbleclient.v1.api.ldap_domains.LdapDomain.test_group)
    * [report\_status](#nimbleclient.v1.api.ldap_domains.LdapDomain.report_status)
  * [LdapDomainList](#nimbleclient.v1.api.ldap_domains.LdapDomainList)
    * [test\_user](#nimbleclient.v1.api.ldap_domains.LdapDomainList.test_user)
    * [test\_group](#nimbleclient.v1.api.ldap_domains.LdapDomainList.test_group)
    * [report\_status](#nimbleclient.v1.api.ldap_domains.LdapDomainList.report_status)

<a name="nimbleclient.v1.api.ldap_domains"></a>
# nimbleclient.v1.api.ldap\_domains

<a name="nimbleclient.v1.api.ldap_domains.LdapDomain"></a>
## LdapDomain

```python
class LdapDomain(Resource)
```

Manages the storage array's membership with LDAP servers.

__Parameters__

- __id                     __: Identifier for the LDAP Domain.
- __domain_name            __: Domain name.
- __domain_description     __: Description of the domain.
- __domain_enabled         __: Indicates whether the LDAP domain is currently active or not.
- __server_uri_list        __: A set of up to 3 LDAP URIs.
- __bind_user              __: Full Distinguished Name of LDAP admin user. If empty, attempt to bind anonymously.
- __bind_password          __: Password for the Full Distinguished Name of LDAP admin user.  This parameter is mandatory if the bind_user is given.
- __base_dn                __: The Distinguished Name of the base object from which to start all searches.
- __user_search_filter     __: Limit the results returned based on specific search criteria.
- __user_search_base_list  __: A set of upto 10 Relative Distinguished Names, relative to the Base DN, from which to search for User objects.
- __group_search_filter    __: Limit the results returned based on specific search criteria.
- __group_search_base_list __: A set of upto 10 Relative Distinguished Names, relative to the Base DN, from which to search for Group objects.
- __schema_type            __: Enum values are OpenLDAP or AD.

<a name="nimbleclient.v1.api.ldap_domains.LdapDomain.test_user"></a>
#### test\_user

```python
 | test_user(user, **kwargs)
```

Tests whether the user exist in the given LDAP Domain.

__Parameters__

- __id   __: Unique identifier for the LDAP Domain.
- __user __: Name of the LDAP Domain user.

<a name="nimbleclient.v1.api.ldap_domains.LdapDomain.test_group"></a>
#### test\_group

```python
 | test_group(group, **kwargs)
```

Tests whether the user group exist in the given LDAP Domain.

__Parameters__

- __id    __: Unique identifier for the LDAP Domain.
- __group __: Name of the group.

<a name="nimbleclient.v1.api.ldap_domains.LdapDomain.report_status"></a>
#### report\_status

```python
 | report_status(**kwargs)
```

Reports the LDAP connectivity status of the given LDAP ID.

__Parameters__

- __id __: Unique identifier for the LDAP Domain.

<a name="nimbleclient.v1.api.ldap_domains.LdapDomainList"></a>
## LdapDomainList

```python
class LdapDomainList(Collection)
```

<a name="nimbleclient.v1.api.ldap_domains.LdapDomainList.test_user"></a>
#### test\_user

```python
 | test_user(id, user, **kwargs)
```

Tests whether the user exist in the given LDAP Domain.

__Parameters__

- __id   __: Unique identifier for the LDAP Domain.
- __user __: Name of the LDAP Domain user.

<a name="nimbleclient.v1.api.ldap_domains.LdapDomainList.test_group"></a>
#### test\_group

```python
 | test_group(id, group, **kwargs)
```

Tests whether the user group exist in the given LDAP Domain.

__Parameters__

- __id    __: Unique identifier for the LDAP Domain.
- __group __: Name of the group.

<a name="nimbleclient.v1.api.ldap_domains.LdapDomainList.report_status"></a>
#### report\_status

```python
 | report_status(id, **kwargs)
```

Reports the LDAP connectivity status of the given LDAP ID.

__Parameters__

- __id __: Unique identifier for the LDAP Domain.

