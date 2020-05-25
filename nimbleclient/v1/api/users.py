#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class User(Resource):
    """Represents users configured to manage the system.

    # Parameters
    id                 : Identifier for the user.
    name               : Name of the user.
    search_name        : Name of the user used for object search.
    description        : Description of the user.
    role_id            : Identifier for the user's role.
    role               : Role of the user.
    password           : User's login password.
    auth_password      : Authorization password for changing password.
    inactivity_timeout : The amount of time that the user session is inactive before timing out. A value of 0 indicates that the timeout is taken from the group setting.
    creation_time      : Time when this user was created.
    last_modified      : Time when this user was last modified.
    full_name          : Fully qualified name of the user.
    email_addr         : Email address of the user.
    disabled           : User is currently disabled.
    auth_lock          : User was locked due to failed logins.
    last_login         : Last login time.
    last_logout        : Last logout time.
    logged_in          : User is currently logged in.
    """

    def unlock(self):
        """Unlocks user account locked due to failed logins.

        # Parameters
        id : ID for the user.
        """

        return self._collection.unlock(
            self.id
        )


class UserList(Collection):
    resource = User
    resource_type = "users"

    def unlock(self, id):
        """Unlocks user account locked due to failed logins.

        # Parameters
        id : ID for the user.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'unlock',
            id=id
        )
