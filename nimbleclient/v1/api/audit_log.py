#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection
from ...exceptions import NimOSAPIOperationUnsupported


class AuditLog(Resource):
    '''
    View audit log.

    Parameters:
    - id                  : Identifier for the audit log record.
    - type                : Identifier for type of audit log record.
    - object_id           : Identifier of object operated upon.
    - object_name         : Name of object operated upon.
    - object_type         : Type of the object being operated upon.
    - scope               : Scope within which object exists, for example, name of the array for a NIC.
    - time                : Time when this operation was performed.
    - status              : Status of the operation -- success or failure.
    - error_code          : If the operation has failed, this indicates the error code corresponding to the failure.
    - user_id             : Identifier of the user who performed the operation.
    - user_name           : Username of the user who performed the operation.
    - user_full_name      : Full name of the user who performed the operation.
    - source_ip           : IP address from where the operation request originated.
    - ext_user_id         : The user id of an external user.
    - ext_user_group_id   : The group ID of an external user.
    - ext_user_group_name : The group name of an external user.
    - app_name            : Name of application from where the operation request was issued, for example, pam, VSS Agent, etc.
    - access_type         : Name of access on how the operation request was issued, for example, GUI, CLI or API.
    - category            : Category of the audit log record.
    - activity_type       : Type of activity performed, for example, create, update or delete.
    - activity            : Description of activity performed and recorded in audit log.
    '''

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")


class AuditLogList(Collection):
    resource = AuditLog
    resource_type = "audit_log"

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")

    def update(self, **kwargs):
        raise NimOSAPIOperationUnsupported("update operation not supported")
