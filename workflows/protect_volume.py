import os
import sys
import traceback
from workflow_common import screen, get_config_vol_name, handle_params, login, cleanup
from nimbleclient.v1 import NimOSAPIError
from create_volume import create_volume


def protect_volume(client, vol_id, noisy):
    try:
        screen('\nWORKFLOW: Protect Volume - {}'.format(vol_id), noisy)
        # Get the volume
        vol = client.volumes.get(vol_id)
        # Create a volume collection
        volcoll_name = vol.attrs['name'] + 'coll'
        volcoll1 = client.volume_collections.create(name=volcoll_name, description="created by workflow")
        screen('\tCreated volume collection: {}, Id: {}'.format(volcoll1.attrs['name'], volcoll1.id), noisy)
        # Associate a volume with the volume collection
        asoc = client.volumes.associate(id=vol.attrs['id'], volcoll=volcoll1)
        screen('\tAssociated volume: {}, with volume vollection: {}'.format(
               asoc['id'], asoc['volcoll_name']), noisy)
        # Create a protection schedule
        ps_name = "ps1"
        ps_days = "monday,tuesday,wednesday,thursday,friday"
        ps_info = "just a schedule"
        ps = client.protection_schedules.create(name=ps_name, period=60, period_unit="minutes",
                                                days=ps_days, description=ps_info,
                                                volcoll_or_prottmpl_id=volcoll1.id,
                                                volcoll_or_prottmpl_type='volume_collection',
                                                num_retain=2)
        screen('\tCreated protection schedule: {}, Id: {}'.format(ps.attrs['name'], ps.id), noisy)
        client.protection_schedules.delete(id=ps.attrs['id'])
        screen('\tDeleted protection schedule: {}'.format(ps.attrs['name']), noisy)
        # Disassociate a volume with the volume collection and delete the volume collection
        client.volumes.dissociate(id=vol.attrs['id'])
        screen('\tDisassociated volume: {}, with volume vollection: {}'.
               format(vol.attrs['name'], volcoll1.attrs['name']), noisy)
        client.volume_collections.delete(id=volcoll1.id)
        screen('\tDeleted volume collection: {}'.format(volcoll1.attrs['name']), noisy)
    except NimOSAPIError:
        traceback.print_stack()
        traceback.print_exc()


if __name__ == '__main__':
    noisy = True
    filename = os.path.basename(__file__)
    client = login(handle_params(filename, sys.argv), noisy)
    vol_id = create_volume(client, get_config_vol_name(), noisy=False)
    screen('\nCreated volume {} to protect.'.format(vol_id), noisy)
    protect_volume(client, vol_id, noisy)
    cleanup(client, {'vol_id_list': [vol_id]}, noisy)
