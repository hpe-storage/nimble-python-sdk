
# nimbleclient.v1.api.users


## User
```python
User(self, id, attrs=None, client=None, collection=None)
```
Represents users configured to manage the system.

__Parameters__

- __id                 __: Identifier for the user.
- __name               __: Name of the user.
- __search_name        __: Name of the user used for object search.
- __description        __: Description of the user.
- __role_id            __: Identifier for the user's role.
- __role               __: Role of the user.
- __password           __: User's login password.
- __auth_password      __: Authorization password for changing password.
- __inactivity_timeout __: The amount of time that the user session is inactive before timing out. A value of 0 indicates that the timeout is taken from the group setting.
- __creation_time      __: Time when this user was created.
- __last_modified      __: Time when this user was last modified.
- __full_name          __: Fully qualified name of the user.
- __email_addr         __: Email address of the user.
- __disabled           __: User is currently disabled.
- __auth_lock          __: User was locked due to failed logins.
- __last_login         __: Last login time.
- __last_logout        __: Last logout time.
- __logged_in          __: User is currently logged in.


## UserList
```python
UserList(self, client=None)
```

