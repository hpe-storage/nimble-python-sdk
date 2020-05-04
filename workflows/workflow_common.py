import sys
import json
import getpass
from nimbleclient.v1 import Client, NimOSAuthenticationError

config_file = 'workflow_config.json'


def screen(msg, noisy, end='\n'):
    if noisy:
        print(msg, end=end)


def usage(file, noisy=True):
    screen('Usage:', noisy)
    screen('\t{} [--query_login]'.format(file), noisy)
    sys.exit(1)


def read_config():
    data = None
    config_dict = None
    with open(config_file, 'r') as myfile:
        data = myfile.read()
    if data is not None:
        config_dict = json.loads(data)
    return config_dict


def get_config_vol_name():
    config_dict = read_config()
    return config_dict['vol_name']


def get_config_ig_name():
    config_dict = read_config()
    return config_dict['ig_name']


def handle_params(file, param_list):
    query_login = False
    if len(param_list) == 2 and param_list[1] == '--query_login':
        query_login = True
    elif (len(param_list) == 2 and param_list[1] != '--query_login') or (len(param_list) > 2):
        usage(file)
    return query_login


def login(query_login, noisy):
    client = None
    if query_login:
        hostname = input('Enter the hostname: ')
        username = input('Enter the username: ')
        password = getpass.getpass(prompt='Enter the password: ', stream=None)
    else:
        config_dict = read_config()
        hostname = config_dict['hostname']
        username = config_dict['username']
        password = config_dict['password']
    screen('\nAttempting to establish connection to array:', noisy)
    screen('\tHostname: {}'.format(hostname), noisy)
    screen('\tUsername: {}'.format(username), noisy)
    # Instantiate nimble client object
    try:
        client = Client(hostname, username, password)
        screen('\tConnection successful!', noisy)
    except NimOSAuthenticationError:
        screen('ERROR: Invalid credentials.', noisy)
        sys.exit(1)
    return client


def cleanup(client, target_dict, noisy):
    screen('\nDoing Cleanup:', noisy)
    if 'acr_id_list' in target_dict.keys():
        for item in target_dict['acr_id_list']:
            acr = client.access_control_records.get(item)
            if acr is not None:
                client.access_control_records.delete(id=acr.attrs['id'])
                screen('\tDeleted ACR: {}'.format(acr.attrs['id']), noisy)
                client.initiator_groups.delete(id=acr.attrs['initiator_group_id'])
                screen('\tDeleted initiator group: {}'.format(acr.attrs['initiator_group_name']), noisy)
    if 'snap_id_list' in target_dict.keys():
        for item in target_dict['snap_id_list']:
            client.snapshots.delete(id=item)
            screen('\tDeleted snapshot: {}'.format(item), noisy)
    if 'vol_id_list' in target_dict.keys():
        for item in target_dict['vol_id_list']:
            client.volumes.offline(id=item)
            client.volumes.delete(id=item)
            screen('\tDeleted volume: {}'.format(item), noisy)
