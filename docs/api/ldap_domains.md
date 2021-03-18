
# nimbleclient.v1.api.ldap_domains


## LdapDomain
```python
LdapDomain(self, id, attrs=None, client=None, collection=None)
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


## LdapDomainList
```python
LdapDomainList(self, client=None)
```

