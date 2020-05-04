#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection


class ApplicationServer(Resource):
    '''
    An application server is an external agent that collaborates with an array to manage storage resources; for example, Volume Shadow Copy Service (VSS) or VMware.

    Parameters:
    - id            : Identifier for the application server.
    - name          : Name for the application server.
    - hostname      : Application server hostname.
    - port          : Application server port number.
    - username      : Application server username.
    - description   : Text description of application server.
    - password      : Application server password.
    - server_type   : Application server type ({invalid|vss|vmware|cisco|stack_vision|container_node}).
    - metadata      : Key-value pairs that augment an application server's attributes.
    - creation_time : Time when this application server was created.
    - last_modified : Time when this application server was last modified.
    '''


class ApplicationServerList(Collection):
    resource = ApplicationServer
    resource_type = "application_servers"
