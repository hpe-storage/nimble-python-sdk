# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, KEY_IG, cleanup_vol,\
    cleanup_access_control_rec, cleanup_initiator_group, create_vol, create_initiator_group, create_access_control_rec
from nimbleclient.exceptions import NimOSAPIError


class publish_volume:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Publish Volume'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()
        self.acr_id = None

    def _do_cleanup(self, acr_id, noisy):
        screen('\nDoing Cleanup:', noisy)
        acr = self.client.access_control_records.get(acr_id)
        cleanup_access_control_rec(self.client, acr.attrs['id'], noisy)
        self.acr_id = None
        cleanup_initiator_group(self.client, acr.attrs['initiator_group_name'], noisy)
        cleanup_vol(self.client, acr.attrs['vol_name'], noisy)   # Cleanup clone vol

    def do_cleanup(self, noisy_cleanup=False):
        res = self.client.access_control_records.list()
        for item in res:
            acr = self.client.access_control_records.get(id=item.attrs['id'])
            if acr.attrs['vol_name'] == self.config[KEY_VOL]:
                self._do_cleanup(acr.attrs['id'], noisy_cleanup)
                break

    def run(self, show_header=True):
        if show_header:
            screen('WORKFLOW: {}'.format(self.title), self.noisy)
            screen('\nRunning:', self.noisy)
        try:
            vol = create_vol(self.client, self.config[KEY_VOL], self.noisy)
            ig = create_initiator_group(self.client, self.config[KEY_IG], self.noisy)
            acr = create_access_control_rec(self.client, ig.attrs['id'], vol.attrs['id'], self.noisy)
            self.acr_id = acr.attrs['id']
            if self.cleanup:
                self._do_cleanup(acr.attrs['id'], self.noisy)
        except NimOSAPIError:
            traceback.print_exc()
            return False
        return True

    def get_acr_id(self):
        return self.acr_id


if __name__ == '__main__':
    cur_noisy = True
    filename = os.path.basename(__file__)
    query_login, cleanup = handle_params(filename, sys.argv)
    client = login(query_login, cur_noisy)
    screen(' ', cur_noisy)
    wf = publish_volume(client, cur_noisy, cleanup)
    wf.run()
