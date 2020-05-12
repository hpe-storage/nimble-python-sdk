# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
from workflow_common import screen, login, config_file
from initiator_group_lifecycle import initiator_group_lifecycle
from create_clone import create_clone
from create_access_control_record import create_access_control_record
from create_volume import create_volume
from publish_volume import publish_volume
from detach_volume import detach_volume
from create_snapshot import create_snapshot
from clone_and_publish_volume import clone_and_publish_volume
from protect_volume import protect_volume
from configure_encryption import configure_encryption


def usage(noisy):
    screen('Usage:', noisy)
    screen('\t{} --internal [--query_login] | --external'.format(__file__), noisy)
    sys.exit(1)


def run_internal(query_login, noisy):
    cleanup = True
    screen('\nRunning All Workflows Internally:', noisy)
    client = login(query_login, noisy)
    screen('\n\n===================================================================== initiator_group_lifecycle', noisy)
    initiator_group_lifecycle(client, noisy, cleanup)
    screen('\n\n================================================================================== create_clone', noisy)
    create_clone(client, noisy, cleanup)
    screen('\n\n================================================================== create_access_control_record', noisy)
    create_access_control_record(client, noisy, cleanup)
    screen('\n\n================================================================================= create_volume', noisy)
    create_volume(client, noisy, cleanup)
    screen('\n\n================================================================================ publish_volume', noisy)
    publish_volume(client, noisy, cleanup)
    screen('\n\n=============================================================================== create_snapshot', noisy)
    create_snapshot(client, noisy, cleanup)
    screen('\n\n====================================================================== clone_and_publish_volume', noisy)
    clone_and_publish_volume(client, noisy, cleanup)
    screen('\n\n================================================================================ protect_volume', noisy)
    protect_volume(client, noisy, cleanup)
    screen('\n\n========================================================================== configure_encryption', noisy)
    configure_encryption(client, noisy, cleanup)
    screen('\n\n================================================================================= detach_volume', noisy)
    detach_volume(client, noisy, cleanup)


def run_external(query_login, noisy):
    if query_login:
        screen('\nERROR: --query_login is not supported in external mode. Please modify {} instead.\n'.
               format(config_file), noisy)
        usage(noisy)
    screen('\nRunning All Workflows Externally:', noisy)
    screen('\n\n===================================================================== initiator_group_lifecycle', noisy)
    os.system('python3 initiator_group_lifecycle.py')
    screen('\n\n================================================================================== create_clone', noisy)
    os.system('python3 create_clone.py')
    screen('\n\n================================================================== create_access_control_record', noisy)
    os.system('python3 create_access_control_record.py')
    screen('\n\n================================================================================= create_volume', noisy)
    os.system('python3 create_volume.py')
    screen('\n\n================================================================================ publish_volume', noisy)
    os.system('python3 publish_volume.py')
    screen('\n\n=============================================================================== create_snapshot', noisy)
    os.system('python3 create_snapshot.py')
    screen('\n\n====================================================================== clone_and_publish_volume', noisy)
    os.system('python3 clone_and_publish_volume.py')
    screen('\n\n================================================================================ protect_volume', noisy)
    os.system('python3 protect_volume.py')
    screen('\n\n========================================================================== configure_encryption', noisy)
    os.system('python3 configure_encryption.py')
    screen('\n\n================================================================================= detach_volume', noisy)
    os.system('python3 detach_volume.py')


def verify_input(noisy):
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        usage(noisy)
    else:
        filename = os.path.basename(__file__)
        valid_flags = [filename, '--internal', '--external', '--query_login']
        for item in sys.argv:
            if item not in valid_flags:
                usage(noisy)


if __name__ == '__main__':
    noisy = True
    verify_input(noisy)
    query_login = True if '--query_login' in sys.argv else False
    if '--external' in sys.argv:
        run_external(query_login, noisy)
    elif '--internal' in sys.argv:
        run_internal(query_login, noisy)
