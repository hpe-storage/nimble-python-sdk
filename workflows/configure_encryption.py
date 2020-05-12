# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, cleanup_vol, cleanup_master_key,\
    KEY_ENCRYPT_VOL, KEY_MK, KEY_MK_PHRASE
from nimbleclient.v1 import NimOSAPIError


def do_cleanup(client, encrypt_vol_name, master_key_name, grp_id, noisy):
    screen('\nDoing Cleanup:', noisy)
    cleanup_vol(client, encrypt_vol_name, noisy)
    cleanup_master_key(client, master_key_name, noisy)
    grp = client.groups.get(grp_id)
    screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)


def force_cleanup(client, encrypt_vol_name, mk_name, grp_id, noisy):
    screen('\tCleaning up existing workflow objects...', noisy)
    do_cleanup(client, encrypt_vol_name, mk_name, grp_id, noisy=False)


def configure_encryption(client, noisy, cleanup):
    config = read_config()
    try:
        screen('\nWORKFLOW: Configure Encryption', noisy)
        # Get the group
        grp_id = client.groups.list()[0].attrs['id']
        grp = client.groups.get(grp_id)
        screen('\tGot group: {}, Id: {}'.format(grp.attrs['name'], grp.id), noisy)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
        # Create a master key
        mk_name = config[KEY_MK]
        mk_phrase = config[KEY_MK_PHRASE]
        encrypt_vol_name = config[KEY_ENCRYPT_VOL]
        # Cleanup any existing workflow objects (i.e. if cleanup was skipped on a previous execution)
        mk = client.master_key.get(name=mk_name)
        if mk is not None:
            force_cleanup(client, encrypt_vol_name, mk_name, grp_id, noisy)
        mk = client.master_key.create(name=mk_name, passphrase=mk_phrase)
        screen('\tCreated a master key: {}, Id: {}'.format(mk.attrs['name'], mk.attrs['id']), noisy)
        # Create an encrypted volume
        encrypt_vol = client.volumes.create(name=encrypt_vol_name, size=50, limit_iops=12000,
                                            encryption_cipher='aes_256_xts')
        screen('\tCreated an encrypted volume: {}, Id: {}'.format(encrypt_vol.attrs['name'], encrypt_vol.attrs['id']),
               noisy)
        # Get the group
        grp = client.groups.get(grp_id)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)
        # Update encryption
        new_encryption = {"mode": "secure",   # Vals: none, available, secure
                          "scope": "volume",  # Vals: none, volume, pool, group
                          "cipher": "none"}   # Vals: none, aes_256_xts
        ue = client.groups.update(id=grp.id, encryption_config=new_encryption)
        screen('\tUpdated encryption: {}'.format(ue.attrs['encryption_config']), noisy)
        if cleanup:
            do_cleanup(client, encrypt_vol_name, mk_name, grp_id, noisy)
    except NimOSAPIError:
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, noisy)
    configure_encryption(client, noisy, cleanup)
