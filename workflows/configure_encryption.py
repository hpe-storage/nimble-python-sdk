# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, cleanup_vol, cleanup_master_key,\
    KEY_ENCRYPT_VOL, KEY_MK, KEY_MK_PHRASE, create_master_key, create_encrypted_vol
from nimbleclient.v1 import NimOSAPIError


class configure_encryption:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Configure Encryption'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, encrypt_vol_name, master_key_name, grp_id, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_vol(self.client, encrypt_vol_name, noisy)
        cleanup_master_key(self.client, master_key_name, noisy)
        grp = self.client.groups.get(grp_id)
        screen('\tCurrent encryption: {}'.format(grp.attrs['encryption_config']), noisy)

    def do_cleanup(self, encrypt_vol_name, mk_name, grp_id, noisy_cleanup=False):
        self._do_cleanup(encrypt_vol_name, mk_name, grp_id, noisy_cleanup)

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            # Get a group and default encryption
            grp_list = self.client.groups.list()
            if len(grp_list) == 0:
                screen('\tERROR: No groups configured on this system.')
                screen('\t       A group must be configured in order to configure encryption.')
                return
            grp_id = grp_list[0].attrs['id']
            grp = self.client.groups.get(grp_id)
            screen('\tGot group: "{}", Id: {}'.format(grp.attrs['name'], grp.id), self.noisy)
            orig_encryption = grp.attrs['encryption_config']
            screen('\tCurrent encryption:  {}'.format(orig_encryption), self.noisy)
            # Create a master key and create an encrypted volume
            create_master_key(self.client, self.config[KEY_MK], self.config[KEY_MK_PHRASE], self.noisy)
            create_encrypted_vol(self.client, self.config[KEY_ENCRYPT_VOL], self.noisy)
            grp = self.client.groups.get(grp_id)
            updated_encryption = grp.attrs['encryption_config']
            if updated_encryption != orig_encryption:
                screen('\tUpdated encryption:  {}'.format(updated_encryption), self.noisy)
            # Modify the encryption (for test)
            mod_encryption = grp.attrs['encryption_config']
            mod_encryption.pop('master_key_set')
            mod_encryption.pop('encryption_active')
            if mod_encryption['mode'] == 'available':
                mod_encryption['mode'] = 'secure'
            elif mod_encryption['mode'] == 'secure':
                mod_encryption['mode'] = 'available'
            ue = self.client.groups.update(id=grp.id, encryption_config=mod_encryption)
            screen('\tModified encryption: {}'.format(ue.attrs['encryption_config']), self.noisy)
            if self.cleanup:
                self._do_cleanup(self.config[KEY_ENCRYPT_VOL], self.config[KEY_MK], grp_id, self.noisy)
        except NimOSAPIError:
            traceback.print_exc()
            return False
        return True


if __name__ == '__main__':
    cur_noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, cur_noisy)
    screen(' ', cur_noisy)
    wf = configure_encryption(client, cur_noisy, cleanup)
    wf.run()
