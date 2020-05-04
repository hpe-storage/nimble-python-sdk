import os
import sys
import traceback
from workflow_common import screen, get_config_ig_name, handle_params, login
from nimbleclient.v1 import NimOSAPIError


def initiator_group_lifecycle(client, ig_name, noisy):
    try:
        screen('\nWORKFLOW: Initiator Group Lifecycle:', noisy)
        # Create an initiator group
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Add initiators
        initiators = [
                {
                    "label": "itor1",
                    "ip_address": "1.1.1.1",
                    "iqn": "iqn.1992-01.com.example:storage.tape1.sys1.xyz"
                }
            ]
        # Note that we re-assign ig so as to capture the update
        ig = client.initiator_groups.update(id=ig.attrs['id'], description='add initiators',
                                            iscsi_initiators=initiators)
        screen('\tAdded initiator: {}'.format(ig.attrs['iscsi_initiators'][0]['label']), noisy)
        # Delete an initiator group
        client.initiator_groups.delete(id=ig.id)
        screen('\tDeleted initiator group: {}'.format(ig.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    initiator_group_lifecycle(client, get_config_ig_name(), noisy)
