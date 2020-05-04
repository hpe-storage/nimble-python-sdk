import os
import sys
from workflow_common import screen, get_config_vol_name, get_config_ig_name, login, config_file
from initiator_group_lifecycle import initiator_group_lifecycle
from volume_clone_lifecycle import volume_clone_lifecycle
from access_control_record_lifecycle import access_control_record_lifecycle
from create_volume import create_volume
from publish_volume import publish_volume
from detach_volume import detach_volume
from create_snapshot import create_snapshot
from delete_snapshot import delete_snapshot
from clone_volume import clone_volume
from protect_volume import protect_volume
from configure_encryption import configure_encryption


def usage(noisy):
    screen('Usage:', noisy)
    screen('\t{} --internal [--query_login] | --external'.format(__file__), noisy)
    sys.exit(1)


def run_internal(query_login, noisy):
    print(sys.argv)
    screen('\nRunning All Workflows Internally:', noisy)
    vol_name = get_config_vol_name()
    ig_name = get_config_ig_name()
    client = login(query_login, noisy)
    initiator_group_lifecycle(client, ig_name, noisy)
    volume_clone_lifecycle(client, vol_name, noisy)
    access_control_record_lifecycle(client, vol_name, ig_name, noisy)
    vol_id = create_volume(client, vol_name, noisy)
    acr_id = publish_volume(client, vol_id, noisy)
    snap_id = create_snapshot(client, vol_name, noisy)
    delete_snapshot(client, snap_id, noisy)
    clone_volume(client, vol_name, noisy)
    protect_volume(client, vol_id, noisy)
    configure_encryption(client, noisy)
    detach_volume(client, acr_id, noisy)


def run_external(query_login, noisy):
    if query_login:
        screen('\nERROR: --query_login is not supported in external mode. Please modify {} instead.\n'.
               format(config_file), noisy)
        usage(noisy)
    screen('\nRunning All Workflows Externally:', noisy)
    screen('\n===================================================================== initiator_group_lifecycle\n', noisy)
    os.system('python3 initiator_group_lifecycle.py')
    screen('\n======================================================================== volume_clone_lifecycle\n', noisy)
    os.system('python3 volume_clone_lifecycle.py')
    screen('\n=============================================================== access_control_record_lifecycle\n', noisy)
    os.system('python3 access_control_record_lifecycle.py')
    screen('\n================================================================================= create_volume\n', noisy)
    os.system('python3 create_volume.py')
    screen('\n================================================================================ publish_volume\n', noisy)
    os.system('python3 publish_volume.py')
    screen('\n=============================================================================== create_snapshot\n', noisy)
    os.system('python3 create_snapshot.py')
    screen('\n=============================================================================== delete_snapshot\n', noisy)
    os.system('python3 delete_snapshot.py')
    screen('\n================================================================================== clone_volume\n', noisy)
    os.system('python3 clone_volume.py')
    screen('\n================================================================================ protect_volume\n', noisy)
    os.system('python3 protect_volume.py')
    screen('\n========================================================================== configure_encryption\n', noisy)
    os.system('python3 configure_encryption.py')
    screen('\n================================================================================= detach_volume\n', noisy)
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
