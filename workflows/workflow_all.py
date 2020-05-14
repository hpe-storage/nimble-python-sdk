# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
from workflow_common import screen, login, config_file
from create_and_update_initiator_group import create_and_update_initiator_group
from create_clone import create_clone
from create_access_control_record import create_access_control_record
from create_volume import create_volume
from publish_volume import publish_volume
from detach_volume import detach_volume
from create_snapshot import create_snapshot
from clone_and_publish_volume import clone_and_publish_volume
from protect_volume import protect_volume
from configure_encryption import configure_encryption
from list_objects import list_objects


def usage(noisy):
    screen('Usage:', noisy)
    screen('\t{} [--cleanup] [--query_login] [--internal | --external]'.format(__file__), noisy)
    sys.exit(1)


def _get_workflows(client, noisy, cleanup):
    wf_list = [create_volume(client, noisy, cleanup),
               create_snapshot(client, noisy, cleanup),
               publish_volume(client, noisy, cleanup),
               detach_volume(client, noisy, cleanup),
               create_clone(client, noisy, cleanup),
               clone_and_publish_volume(client, noisy, cleanup),
               create_access_control_record(client, noisy, cleanup),
               create_and_update_initiator_group(client, noisy, cleanup),
               protect_volume(client, noisy, cleanup),
               configure_encryption(client, noisy, cleanup),
               list_objects(client, noisy, cleanup)
               ]
    return wf_list


def _get_workflow_files():
    wf_list = ['create_volume.py',
               'create_snapshot.py',
               'publish_volume.py',
               'detach_volume.py',
               'create_clone.py',
               'clone_and_publish_volume.py',
               'create_access_control_record.py',
               'create_and_update_initiator_group.py',
               'protect_volume.py',
               'configure_encryption.py',
               'list_objects.py'
               ]
    return wf_list


def run_internal(query_login, cleanup, noisy):
    screen('\nRunning All Workflows Internally:', noisy)
    client = login(query_login, noisy)
    sep = '===================================================================================================='
    wf_list = _get_workflows(client, noisy, cleanup)
    wf_count = len(wf_list)
    success_count = 0
    for i in range(len(wf_list)):
        screen('\n\n\n{}[{}/{}]'.format(sep, i+1, wf_count), noisy)
        res = wf_list[i].run()
        if res:
            success_count += 1
    screen('\n\n{} of {} workflows SUCCEEDED'.format(success_count, wf_count), noisy)


def run_external2(query_login, cleanup, noisy):
    if query_login:
        screen('\nERROR: --query_login is not supported in external mode. Please modify {} instead.\n'.
               format(config_file), noisy)
        usage(noisy)
    cleanup_flag = '--cleanup' if cleanup is True else ''
    screen('\nRunning All Workflows Externally:', noisy)
    sep = '===================================================================================================='
    wf_list = _get_workflow_files()
    wf_count = len(wf_list)
    for i in range(len(wf_list)):
        screen('\n\n\n{}[{}/{}]'.format(sep, i+1, wf_count), noisy)
        screen('{} {}'.format(wf_list[i], cleanup_flag), noisy)
        os.system('python3 {} {}'.format(wf_list[i], cleanup_flag))


def verify_input(noisy):
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        usage(noisy)
    else:
        filename = os.path.basename(__file__)
        valid_flags = [filename, '--internal', '--external', '--query_login', '--cleanup']
        for item in sys.argv:
            if item not in valid_flags:
                usage(noisy)


if __name__ == '__main__':
    noisy = True
    verify_input(noisy)
    query_login = True if '--query_login' in sys.argv else False
    cleanup = True if '--cleanup' in sys.argv else False
    if '--external' in sys.argv:
        run_external2(query_login, cleanup, noisy)
    elif '--internal' in sys.argv:
        run_internal(query_login, cleanup, noisy)
