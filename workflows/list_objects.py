# (c) Copyright 2020 Hewlett Packard Enterprise Development LP
# @author bsorge

import os
import sys
import traceback
from workflow_common import screen, handle_params, login, read_config, KEY_VOL, KEY_SNAP,\
    cleanup_snapshot, cleanup_vol, create_vol, create_snap
from nimbleclient.exceptions import NimOSAPIError


class list_objects:
    def __init__(self, client, noisy, cleanup):
        self.title = 'List Objects'
        self.client = client
        self.noisy = noisy
        self.cleanup = cleanup
        self.config = read_config()
        self.obj_list = []

    def _do_cleanup(self, noisy):
        screen('\nDoing Cleanup:', noisy)
        for item in self.obj_list:
            if item[0] == 'snap_id':
                cleanup_snapshot(self.client, item[1], noisy)
            if item[0] == 'vol_name':
                cleanup_vol(self.client, item[1], noisy)

    def do_cleanup(self, noisy_cleanup=False):
        self._do_cleanup(noisy_cleanup)

    def _do_generate_objects(self):
        screen('\nGenerating Objects...', self.noisy)
        vol_count = 2
        snap_count = 3
        temp_noisy = True
        vol_base_name = self.config[KEY_VOL]
        snap_base_name = self.config[KEY_SNAP]
        for i in range(vol_count):
            vol = create_vol(self.client, vol_base_name + str(i), temp_noisy)
            for j in range(snap_count):
                snap = create_snap(self.client, snap_base_name + str(i) + '.' + str(j), vol.attrs['id'], temp_noisy)
                self.obj_list.append(('snap_id', snap.attrs['id']))
            self.obj_list.append(('vol_name', vol.attrs['name']))

    def run(self):
        screen('WORKFLOW: {}'.format(self.title), self.noisy)
        self._do_generate_objects()
        screen('\nRunning:', self.noisy)
        try:
            vol_list = self.client.volumes.list()
            screen('\n\tObjects on Array:', self.noisy)
            for vol in vol_list:
                screen('\t\tVOLUME: {}, Id: {}'.format(vol.attrs['name'], vol.attrs['id']), self.noisy)
                snap_list = self.client.snapshots.list(vol_name=vol.attrs['name'])
                for snap in snap_list:
                    screen('\t\t\tSNAPSHOT: {}, Id: {}'.format(snap.attrs['name'], snap.attrs['id']), self.noisy)
            if self.cleanup:
                self._do_cleanup(self.noisy)
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
    wf = list_objects(client, cur_noisy, cleanup)
    wf.run()
