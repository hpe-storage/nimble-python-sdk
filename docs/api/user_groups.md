# Table of Contents

* [nimbleclient.v1.api.user\_groups](#nimbleclient.v1.api.user_groups)
  * [UserGroup](#nimbleclient.v1.api.user_groups.UserGroup)

<a name="nimbleclient.v1.api.user_groups"></a>
# nimbleclient.v1.api.user\_groups

<a name="nimbleclient.v1.api.user_groups.UserGroup"></a>
## UserGroup

```python
class UserGroup(Resource)
```

Represents Active Directory groups configured to manage the system.

__Parameters__

- __id                 __: Identifier for the user group.
- __name               __: Name of the user group.
- __description        __: Description of the user group.
- __role_id            __: Identifier for the user group's role.
- __role               __: Role of the user.
- __inactivity_timeout __: The amount of time that the user session is inactive before timing out. A value of 0 indicates that the timeout is taken from the group setting.
- __creation_time      __: Time when this user was created.
- __last_modified      __: Time when this user was last modified.
- __disabled           __: User is currently disabled.
- __external_id        __: External ID of the user group. In Active Directory, it is the group's SID (Security Identifier).
- __domain_id          __: Identifier of the domain this user group belongs to.
- __domain_name        __: Role of the user.

