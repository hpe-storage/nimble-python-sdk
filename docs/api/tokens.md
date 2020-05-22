
# nimbleclient.v1.api.tokens


## Token
```python
Token(self, id, attrs=None, client=None, collection=None)
```
Manage user's session information.

__Parameters__

- __id            __: Object identifier for the session token.
- __session_token __: Token used for authentication.
- __username      __: User name for the session.
- __password      __: Password for the user. A password is required for creating a token.
- __app_name      __: Application name.
- __sdk_name      __: SDK name.
- __source_ip     __: IP address from which the session originates.
- __creation_time __: Time when this token was created.
- __last_modified __: Time when this token was last modified.
- __expiry_time   __: Time when this token will expire.
- __server_uuid   __: Non mandatory 36 character uuid returned by the server. Currently only the witness REST server returns one.


## TokenList
```python
TokenList(self, client=None)
```

