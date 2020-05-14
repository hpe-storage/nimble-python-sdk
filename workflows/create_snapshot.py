# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login, read_config, KEY_VOL, KEY_SNAP,\
    cleanup_snapshots, cleanup_snapshot, cleanup_vol, create_vol, create_snap
from nimbleclient.v1 import NimOSAPIError


class create_snapshot:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Create Snapshot'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, snap_id, vol_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_snapshot(self.client, snap_id, noisy)
        cleanup_vol(self.client, vol_name, noisy)

    def do_cleanup(self, vol_name, noisy_cleanup=False):
        cleanup_snapshots(client, vol_name, noisy=False)
        cleanup_vol(client, vol_name, noisy=False)

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            # Create a volume
            vol = create_vol(self.client, self.config[KEY_VOL], self.noisy)
            # Create a snapshot
            snap = create_snap(self.client, self.config[KEY_SNAP], vol.attrs['id'], self.noisy)
            if self.cleanup:
                self._do_cleanup(snap.id, vol.attrs['name'], self.noisy)
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
    wf = create_snapshot(client, cur_noisy, cleanup)
    wf.run()
