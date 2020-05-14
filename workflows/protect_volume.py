# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, KEY_PS, KEY_VOLCOLL,\
    cleanup_protection_schedule, cleanup_volume_collection, cleanup_vol, create_vol, create_volume_collection,\
    associate_vol, create_protection_schedule
from nimbleclient.v1 import NimOSAPIError


class protect_volume:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Protect Volume'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, ps_name, vc_name, vol_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_protection_schedule(self.client, ps_name, noisy)
        cleanup_volume_collection(self.client, vc_name, noisy)
        cleanup_vol(self.client, vol_name, noisy)

    def do_cleanup(self, ps_name, vc_name, vol_name, noisy_cleanup=False):
        self._do_cleanup(ps_name, vc_name, vol_name, noisy_cleanup)

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            # Create Volume
            vol = create_vol(self.client, self.config[KEY_VOL], self.noisy)
            # Create a volume collection
            volcoll1 = create_volume_collection(self.client, self.config[KEY_VOLCOLL], self.noisy)
            # Associate a volume with the volume collection
            associate_vol(self.client, vol.id, volcoll1, self.noisy)
            # Create a protection schedule
            ps_name = self.config[KEY_PS]
            create_protection_schedule(self.client, ps_name, volcoll1.attrs['id'], self.noisy)
            if self.cleanup:
                self._do_cleanup(ps_name, self.config[KEY_VOLCOLL], vol.attrs['name'], self.noisy)
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
    wf = protect_volume(client, cur_noisy, cleanup)
    wf.run()
