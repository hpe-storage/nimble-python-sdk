# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, cleanup_access_control_rec,\
    KEY_VOL, KEY_SNAP, KEY_CLONE, cleanup_initiator_group, create_vol, cleanup_vol, clone_vol,\
    cleanup_snapshots, create_snap, create_initiator_group, create_access_control_rec
from nimbleclient.v1 import NimOSAPIError


class clone_and_publish_volume:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Clone And Publish Volume'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, clone_acr_id, snap_name, vol_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        acr = self.client.access_control_records.get(clone_acr_id)
        cleanup_access_control_rec(self.client, acr.attrs['id'], noisy)
        cleanup_initiator_group(self.client, acr.attrs['initiator_group_name'], noisy)
        cleanup_vol(self.client, acr.attrs['vol_name'], noisy)   # Cleanup clone vol
        cleanup_snapshots(self.client, vol_name, noisy)
        cleanup_vol(self.client, vol_name, noisy)    # Cleanup orig vol

    def do_cleanup(self, noisy_cleanup=False):
        res = self.client.access_control_records.list()
        for item in res:
            acr = self.client.access_control_records.get(id=item.attrs['id'])
            if acr.attrs['vol_name'] == self.config[KEY_CLONE]:
                self._do_cleanup(acr.attrs['id'], self.config[KEY_SNAP], self.config[KEY_VOL], noisy_cleanup)
                break

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            vol = create_vol(self.client, self.config[KEY_VOL], self.noisy)
            vol_id = vol.id
            vol_name = vol.attrs['name']
            snap = create_snap(self.client, self.config[KEY_SNAP], vol_id, self.noisy)
            clone = clone_vol(self.client, self.config[KEY_CLONE], snap.attrs['id'], self.noisy)
            ig = create_initiator_group(self.client, self.config[KEY_CLONE] + 'ig', self.noisy)
            acr = create_access_control_rec(self.client, ig.attrs['id'], clone.attrs['id'], self.noisy)
            if self.cleanup:
                self._do_cleanup(acr.attrs['id'], snap.attrs['name'], vol_name, self.noisy)
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
    wf = clone_and_publish_volume(client, cur_noisy, cleanup)
    wf.run()
