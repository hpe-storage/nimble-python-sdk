import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login
from nimbleclient.v1 import NimOSAPIError


def configure_encryption(client, noisy):
    try:
        screen('\nWorkflow: Configure Encryption', noisy)
        # Get the group
        grp_id = client.groups.list()[0].attrs['id']
        grp = client.groups.get(grp_id)
        screen('\tGot group: {}, Id: {}'.format(grp.attrs['name'], grp.id), noisy)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
        # Create a master key
        mk_name = 'default'
        mk_phrase = 'test-phrase11'
        mk = client.master_key.create(name=mk_name, passphrase=mk_phrase)
        screen('\tCreated a master key: {}, Id: {}'.format(mk.attrs['name'], mk.attrs['id']), noisy)
        # Create an encrypted volume
        vol_name = get_config_vol_name() + 'encrypted'
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000, encryption_cipher='aes_256_xts')
        screen('\tCreated an encrypted volume: {}, Id: {}'.format(vol.attrs['name'], vol.attrs['id']), noisy)
        # Get the group
        grp = client.groups.get(grp_id)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
        # Update encryption
        new_encryption = {"mode": "secure",   # Vals: none, available, secure
                          "scope": "volume",  # Vals: none, volume, pool, group
                          "cipher": "none"}   # Vals: none, aes_256_xts
        ue = client.groups.update(id=grp.id, encryption_config=new_encryption)
        screen('\tUpdated encryption: {}'.format(ue.attrs['encryption_config']), noisy)
        # Delete encrypted volume and master_key
        client.volumes.offline(id=vol.id)
        client.volumes.delete(id=vol.id)
        screen('\tDeleted volume: {}'.format(vol_name), noisy)
        client.master_key.delete(mk.attrs['id'])
        screen('\tDeleted master key: {}'.format(mk_name), noisy)
        grp = client.groups.get(grp_id)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    configure_encryption(client, noisy)
