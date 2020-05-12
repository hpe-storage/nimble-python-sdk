# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, cleanup_initiator_group, KEY_IG
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, ig_name, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_initiator_group(client, ig_name, noisy)


def force_cleanup(client, ig_name, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    do_cleanup(client, ig_name, noisy=False)


def initiator_group_lifecycle(client, noisy, cleanup):
    config = read_config()
    ig_name = config[KEY_IG]
    try:
        screen('\nWORKFLOW: Initiator Group Lifecycle:', noisy)
        # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
        if client.initiator_groups.get(name=ig_name) is not None:
            force_cleanup(client, ig_name, noisy)
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
        if cleanup:
            do_cleanup(client, ig_name, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    initiator_group_lifecycle(client, noisy, cleanup)
