
# nimbleclient.v1.api.audit_log


## AuditLog
```python
AuditLog(self, id, attrs=None, client=None, collection=None)
```
View audit log.

__Parameters__

- __id                  __: Identifier for the audit log record.
- __type                __: Identifier for type of audit log record.
- __object_id           __: Identifier of object operated upon.
- __object_name         __: Name of object operated upon.
- __object_type         __: Type of the object being operated upon.
- __scope               __: Scope within which object exists, for example, name of the array for a NIC.
- __time                __: Time when this operation was performed.
- __status              __: Status of the operation -- success or failure.
- __error_code          __: If the operation has failed, this indicates the error code corresponding to the failure.
- __user_id             __: Identifier of the user who performed the operation.
- __user_name           __: Username of the user who performed the operation.
- __user_full_name      __: Full name of the user who performed the operation.
- __source_ip           __: IP address from where the operation request originated.
- __ext_user_id         __: The user id of an external user.
- __ext_user_group_id   __: The group ID of an external user.
- __ext_user_group_name __: The group name of an external user.
- __app_name            __: Name of application from where the operation request was issued, for example, pam, VSS Agent, etc.
- __access_type         __: Name of access on how the operation request was issued, for example, GUI, CLI or API.
- __category            __: Category of the audit log record.
- __activity_type       __: Type of activity performed, for example, create, update or delete.
- __activity            __: Description of activity performed and recorded in audit log.


## AuditLogList
```python
AuditLogList(self, client=None)
```

