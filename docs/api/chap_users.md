
# nimbleclient.v1.api.chap_users


## ChapUser
```python
ChapUser(self, id, attrs=None, client=None, collection=None)
```
Manage Challenge-Response Handshake Authentication Protocol (CHAP) user accounts. CHAP users are one method of access control for iSCSI initiators. Each CHAP user has a CHAP
password, sometimes called a CHAP secret. The CHAP passwords must match on the array and on the iSCSI initiator in order for the array to authenicate the initiator and allow
it access. The CHAP user information must exist on both the array and the iSCSI initiator. Target authentication gives security only for the specific iSCSI target.

__Parameters__

- __id             __: Identifier for the CHAP user.
- __name           __: Name of CHAP user.
- __full_name      __: CHAP user's fully qualified name.
- __search_name    __: CHAP user name used for object search.
- __description    __: Text description of CHAP user.
- __password       __: CHAP secret.The CHAP secret should be between 12-16 characters and cannot contain spaces or most punctuation.
- __initiator_iqns __: List of iSCSI initiators. To be configured with this CHAP user for iSCSI Group Target CHAP authentication. This attribute cannot be modified at the same time
                 with other attributes. If any specified initiator is already associated with another CHAP user, it will be replaced by this CHAP user for future CHAP
                 authentication.
- __creation_time  __: Time when this CHAP user was created.
- __last_modified  __: Time when this CHAP user was last modified.
- __vol_list       __: List of volumes associated with this CHAP user.
- __vol_count      __: Count of volumes associated with this CHAP user.


## ChapUserList
```python
ChapUserList(self, client=None)
```

