# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login, read_config, cleanup_vol,\
     cleanup_access_control_rec, cleanup_initiator_group, cleanup_vol_prep
from nimbleclient.exceptions import NimOSAPIError
from publish_volume import publish_volume


class detach_volume:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Detach Volume'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def do_cleanup(self, noisy):
        screen('\nDoing Cleanup:', noisy)
        screen('\tNo cleanup required for detach_volume workflow', noisy)

    def run(self, show_header=True):
        if show_header:
            screen('WORKFLOW: {}'.format(self.title), self.noisy)
            screen('\nRunning:', self.noisy)
        pubvol_wf = publish_volume(self.client, self.noisy, cleanup=False)
        pubvol_wf.run(show_header=False)
        acr_id = pubvol_wf.get_acr_id()
        try:
            # Get the ACR, we will need this to cleanup the initiator group
            acr = self.client.access_control_records.get(acr_id)
            cleanup_access_control_rec(self.client, acr_id, self.noisy)
            cleanup_initiator_group(self.client, acr.attrs['initiator_group_name'], self.noisy)
            cleanup_vol_prep(self.client, acr.attrs['vol_name'], self.noisy)
            cleanup_vol(self.client, acr.attrs['vol_name'], self.noisy)
            if self.cleanup:
                self.do_cleanup(self.noisy)
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
    wf = detach_volume(client, cur_noisy, cleanup)
    wf.run()
