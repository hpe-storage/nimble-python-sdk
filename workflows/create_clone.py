# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, KEY_SNAP, KEY_CLONE,\
    cleanup_vol, cleanup_snapshots, create_vol, create_snap, clone_vol
from nimbleclient.exceptions import NimOSAPIError


class create_clone:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Create Clone'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, clone_name, vol_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_vol(self.client, clone_name, noisy)
        cleanup_snapshots(self.client, vol_name, noisy)
        cleanup_vol(self.client, vol_name, noisy)

    def do_cleanup(self, clone_name, vol_name, noisy_cleanup=False):
        self._do_cleanup(clone_name, vol_name, noisy_cleanup)

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            # Create a volume
            vol = create_vol(self.client, self.config[KEY_VOL], self.noisy)
            # Create a snapshot
            snap = create_snap(self.client, self.config[KEY_SNAP], vol.attrs['id'], self.noisy)
            # Create a clone from a snapshot
            clone = clone_vol(self.client, self.config[KEY_CLONE], snap.attrs['id'], self.noisy)
            if self.cleanup:
                self._do_cleanup(clone.attrs['name'], self.config[KEY_VOL], self.noisy)
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
    wf = create_clone(client, cur_noisy, cleanup)
    wf.run()
