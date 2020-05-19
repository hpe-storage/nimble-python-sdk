# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, KEY_VOL, create_vol, cleanup_vol
from nimbleclient.exceptions import NimOSAPIError


class create_volume:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Create Volume'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, vol_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_vol(self.client, vol_name, noisy)

    def do_cleanup(self, vol_name, noisy_cleanup=False):
        self._do_cleanup(vol_name, noisy_cleanup)

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            create_vol(self.client, self.config[KEY_VOL], self.noisy)
            if self.cleanup:
                self._do_cleanup(self.config[KEY_VOL], self.noisy)
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
    wf = create_volume(client, cur_noisy, cleanup)
    wf.run()
