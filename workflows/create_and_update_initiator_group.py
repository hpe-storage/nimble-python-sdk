# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, read_config, handle_params, login, cleanup_initiator_group, KEY_IG,\
     create_initiator_group
from nimbleclient.exceptions import NimOSAPIError


class create_and_update_initiator_group:
    def __init__(self, client, noisy, cleanup):
        self.title = 'Create And Update Initiator Group'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()

    def _do_cleanup(self, ig_name, noisy):
        screen('\nDoing Cleanup:', noisy)
        cleanup_initiator_group(self.client, ig_name, noisy)

    def do_cleanup(self, ig_name, noisy_cleanup=False):
        self._do_cleanup(ig_name, noisy_cleanup)

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        screen('\nRunning:', self.noisy)
        try:
            initiator_count = 0
            ig = create_initiator_group(self.client, self.config[KEY_IG], self.noisy)
            if ig.attrs['iscsi_initiators'] is not None:
                initiator_count = len(ig.attrs['iscsi_initiators'])
                screen('\tCurrent initiator count: {}'.format(initiator_count), self.noisy)
                initiators = ig.attrs['iscsi_initiators']
            else:
                screen('\tCurrent initiator count: 0', self.noisy)
                initiators = []
            initiator_count += 1
            # Add an initiator to the list
            new_initiator = {"label": "wftest-itor" + str(initiator_count),
                             "ip_address": "1.1.1." + str(initiator_count),
                             "iqn": "iqn.1992-0" + str(initiator_count) + ".com.example:storage.tape1.sys1.xyz"}
            initiators.append(new_initiator)
            # Note that we re-assign ig so as to capture the update
            ig = self.client.initiator_groups.update(id=ig.attrs['id'], description='add initiators',
                                                     iscsi_initiators=initiators)
            screen('\tAdded initiator "{}": {}'.
                   format(ig.attrs['iscsi_initiators'][-1]['label'], initiators[-1]), self.noisy)
            screen('\tCurrent initiator count: {}'.format(len(ig.attrs['iscsi_initiators'])), self.noisy)
            if self.cleanup:
                self._do_cleanup(self.config[KEY_IG], self.noisy)
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
    wf = create_and_update_initiator_group(client, cur_noisy, cleanup)
    wf.run()
