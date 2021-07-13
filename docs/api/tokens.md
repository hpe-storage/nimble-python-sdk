# Table of Contents

* [nimbleclient.v1.api.tokens](#nimbleclient.v1.api.tokens)
  * [Token](#nimbleclient.v1.api.tokens.Token)
    * [report\_user\_details](#nimbleclient.v1.api.tokens.Token.report_user_details)
  * [TokenList](#nimbleclient.v1.api.tokens.TokenList)
    * [report\_user\_details](#nimbleclient.v1.api.tokens.TokenList.report_user_details)

<a name="nimbleclient.v1.api.tokens"></a>
# nimbleclient.v1.api.tokens

<a name="nimbleclient.v1.api.tokens.Token"></a>
## Token

```python
class Token(Resource)
```

Manage user's session information.

# Parameters
id            : Object identifier for the session token.
session_token : Token used for authentication.
username      : User name for the session.
password      : Password for the user. A password is required for creating a token.
app_name      : Application name.
sdk_name      : SDK name.
source_ip     : IP address from which the session originates.
creation_time : Time when this token was created.
last_modified : Time when this token was last modified.
expiry_time   : Time when this token will expire.
server_uuid   : Non mandatory 36 character uuid returned by the server. Currently only the witness REST server returns one.
grant_type    : OAuth grant type, currently only support 'urn:ietf:params:oauth:grant-type:jwt-bearer'.
assertion     : OAuth assertion, currently expecting a JWT token.

<a name="nimbleclient.v1.api.tokens.Token.report_user_details"></a>
#### report\_user\_details

```python
 | report_user_details(**kwargs)
```

Reports the user details for this token.

__Parameters__

- __id __: ID for the session token.

<a name="nimbleclient.v1.api.tokens.TokenList"></a>
## TokenList

```python
class TokenList(Collection)
```

<a name="nimbleclient.v1.api.tokens.TokenList.report_user_details"></a>
#### report\_user\_details

```python
 | report_user_details(id, **kwargs)
```

Reports the user details for this token.

__Parameters__

- __id __: ID for the session token.

