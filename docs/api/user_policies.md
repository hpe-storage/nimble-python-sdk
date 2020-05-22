
# nimbleclient.v1.api.user_policies


## UserPolicy
```python
UserPolicy(self, id, attrs=None, client=None, collection=None)
```
Manages the password policies configured for the group.

__Parameters__

- __id               __: Identifier for the security policy.
- __allowed_attempts __: Number of authentication attempts allowed before the user account is locked. Allowed range is [1, 10] inclusive. '0' indicates no limit.
- __min_length       __: Minimum length for user passwords. Allowed range is [8, 255] inclusive.
- __upper            __: Number of uppercase characters required in user passwords. Allowed range is [0, 255] inclusive.
- __lower            __: Number of lowercase characters required in user passwords. Allowed range is [0, 255] inclusive.
- __digit            __: Number of numerical characters required in user passwords. Allowed range is [0, 255] inclusive.
- __special          __: Number of special characters required in user passwords. Allowed range is [0, 255] inclusive.
- __previous_diff    __: Number of characters that must be different from the previous password. Allowed range is [1, 255] inclusive.
- __no_reuse         __: Number of times that a password must change before you can reuse a previous password. Allowed range is [1,20] inclusive.
- __max_sessions     __: Maximum number of sessions allowed for a group. Allowed range is [10, 1000] inclusive. '0' indicates no limit.


## UserPolicyList
```python
UserPolicyList(self, client=None)
```

