import os
import sys
import traceback
from workflow_common import get_config_vol_name, get_config_ig_name, screen, handle_params, login
from nimbleclient.v1 import NimOSAPIError


def access_control_record_lifecycle(client, vol_name, ig_name, noisy):
    try:
        screen('\nWORKFLOW: Access Control Record Lifecycle:', noisy)
        # Create a volume
        vol = client.volumes.create(name=vol_name, size=50, limit_iops=12000)
        screen('\tCreated volume: {}, Id: {}'.format(vol.attrs['name'], vol.id), noisy)
        # Create an initiator group
        ig = client.initiator_groups.create(name=ig_name, description='workflow example', access_protocol='iscsi')
        screen('\tCreated initiator group: {}, Id: {}'.format(ig.attrs['name'], ig.id), noisy)
        # Create the ACR
        acr = client.access_control_records.create(apply_to='both', initiator_group_id=ig.attrs['id'],
                                                   vol_id=vol.attrs['id'])
        screen('\tCreated access control record: {}'.format(acr.attrs['id']), noisy)
        # Cleanup
        client.access_control_records.delete(id=acr.attrs['id'])
        screen('\tDeleted access control record: {}'.format(acr.attrs['id']), noisy)
        client.initiator_groups.delete(id=ig.attrs['id'])
        screen('\tDeleted initiator group: {}'.format(ig.attrs['name']), noisy)
        client.volumes.offline(id=vol.attrs['id'])
        client.volumes.delete(id=vol.attrs['id'])
        screen('\tDeleted volume: {}'.format(vol.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    access_control_record_lifecycle(client, get_config_vol_name(), get_config_ig_name(), noisy)
