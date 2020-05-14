# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login, read_config, KEY_VOL, KEY_IG,\
    cleanup_access_control_rec, cleanup_initiator_group, cleanup_vol,\
    create_vol, create_initiator_group, create_access_control_rec
from nimbleclient.v1 import NimOSAPIError


class create_access_control_record:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Create Access control Record'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, acr_id, ig_name, vol_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_access_control_rec(self.client, acr_id, noisy)
        cleanup_initiator_group(self.client, ig_name, noisy)
        cleanup_vol(self.client, vol_name, noisy)

    def do_cleanup(self, ig_name, vol_name, noisy_cleanup=False):
        res = self.client.access_control_records.list()
        for item in res:
            acr = self.client.access_control_records.get(id=item.attrs['id'])
            if acr.attrs['vol_name'] == vol_name:
                self._do_cleanup(acr.attrs['id'], ig_name, vol_name, noisy_cleanup)
                break

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            # Create a volume
            vol = create_vol(self.client, self.config[KEY_VOL], self.noisy)
            # Create an initiator group
            ig = create_initiator_group(self.client, self.config[KEY_IG], self.noisy)
            # Create the ACR
            acr = create_access_control_rec(self.client, ig.attrs['id'], vol.attrs['id'], self.noisy)
            if self.cleanup:
                self._do_cleanup(acr.attrs['id'], self.config[KEY_IG], self.config[KEY_VOL], self.noisy)
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
    wf = create_access_control_record(client, cur_noisy, cleanup)
    wf.run()
