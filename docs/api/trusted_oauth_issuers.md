# Table of Contents

* [nimbleclient.v1.api.trusted\_oauth\_issuers](#nimbleclient.v1.api.trusted_oauth_issuers)
  * [TrustedOauthIssuer](#nimbleclient.v1.api.trusted_oauth_issuers.TrustedOauthIssuer)

<a name="nimbleclient.v1.api.trusted_oauth_issuers"></a>
# nimbleclient.v1.api.trusted\_oauth\_issuers

<a name="nimbleclient.v1.api.trusted_oauth_issuers.TrustedOauthIssuer"></a>
## TrustedOauthIssuer

```python
class TrustedOauthIssuer(Resource)
```

Oauth Credential Issuers that this device will trust.

__Parameters__

- __id       __: Identifier for the trusted oauth issuer record.
- __name     __: Issuer ID string.
- __jwks_url __: The URL from which the device will download the public key set for signature verification.
- __key_set  __: List of public keys for verifying signatures.

