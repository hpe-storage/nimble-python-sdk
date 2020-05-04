#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class ChapUser(Resource):
    '''
    Manage Challenge-Response Handshake Authentication Protocol (CHAP) user accounts. CHAP users are one method of access control for iSCSI initiators. Each CHAP user has a CHAP
    password, sometimes called a CHAP secret. The CHAP passwords must match on the array and on the iSCSI initiator in order for the array to authenicate the initiator and allow
    it access. The CHAP user information must exist on both the array and the iSCSI initiator. Target authentication gives security only for the specific iSCSI target.

    Parameters:
    - id             : Identifier for the CHAP user.
    - name           : Name of CHAP user.
    - full_name      : CHAP user's fully qualified name.
    - search_name    : CHAP user name used for object search.
    - description    : Text description of CHAP user.
    - password       : CHAP secret.The CHAP secret should be between 12-16 characters and cannot contain spaces or most punctuation.
    - initiator_iqns : List of iSCSI initiators. To be configured with this CHAP user for iSCSI Group Target CHAP authentication. This attribute cannot be modified at the same
                       time with other attributes. If any specified initiator is already associated with another CHAP user, it will be replaced by this CHAP user for future CHAP
                       authentication.
    - creation_time  : Time when this CHAP user was created.
    - last_modified  : Time when this CHAP user was last modified.
    - vol_list       : List of volumes associated with this CHAP user.
    - vol_count      : Count of volumes associated with this CHAP user.
    '''


class ChapUserList(Collection):
    resource = ChapUser
    resource_type = "chap_users"
