import test_admin_tenant

'''
Create
'''
server_id = test_admin_tenant.create_server_test()
tenant_uid, admin_uid = test_admin_tenant.create_chap_user_test()
tenant_vol_id, admin_vol_id = test_admin_tenant.create_volume_test()
tenant_volcol_id, admin_volcol_id = test_admin_tenant.create_volume_collection_test()
tenant_ig_id, admin_ig_id = test_admin_tenant.create_initiator_group_test()
tenant_iid, admin_iid = test_admin_tenant.create_initiator_test(tenant_ig_id)
tenant_token_id, admin_token_id = test_admin_tenant.create_token_test()
tenant_acr_id, admin_acr_id = test_admin_tenant.create_access_control_records_test(
    tenant_ig_id, tenant_vol_id, admin_ig_id, admin_vol_id)
tenant_ss_id, admin_ss_id = test_admin_tenant.create_snapshot_test(
    tenant_vol_id, admin_vol_id)
admin_ssc_id = test_admin_tenant.create_snapshot_collection_test(
    tenant_volcol_id, tenant_volcol_id)

'''
Update
'''
test_admin_tenant.test_update_description("chap_user", tenant_uid, admin_uid)
test_admin_tenant.test_update_description(
    "volume", tenant_vol_id, admin_vol_id)
test_admin_tenant.test_update_description(
    "volume_collection", tenant_volcol_id, admin_volcol_id)
test_admin_tenant.test_update_description(
    "snapshot", tenant_ss_id, admin_ss_id)
test_admin_tenant.test_update_description(
    "initiator_group", tenant_ig_id, admin_ig_id)


'''
READ
# '''
vol = test_admin_tenant.get_vol_by_id(admin_vol_id)
folder_id = vol.attrs['folder_id']
test_admin_tenant.read_test('folder', 'tenant', folder_id)
test_admin_tenant.read_test('folder', 'admin', folder_id)

group_id = vol.attrs['owned_by_group_id']
test_admin_tenant.read_test('group', 'tenant', group_id)
test_admin_tenant.read_test('group', 'admin', group_id)

perpolicy_id = vol.attrs['perfpolicy_id']
test_admin_tenant.read_test('performance_policy', 'tenant', perpolicy_id)
test_admin_tenant.read_test('performance_policy', 'admin', perpolicy_id)

pool_id = vol.attrs['pool_id']
test_admin_tenant.read_test('pool', 'tenant', pool_id)
test_admin_tenant.read_test('pool', 'admin', pool_id)

test_admin_tenant.read_test('network_config', 'tenant')
test_admin_tenant.read_test('network_config', 'admin')
test_admin_tenant.read_test('protection_template', 'tenant')
test_admin_tenant.read_test('protection_template', 'admin')
test_admin_tenant.read_test('replication_partner', 'tenant')
test_admin_tenant.read_test('replication_partner', 'admin')

test_admin_tenant.read_test('snapshot_collection', 'tenant')
test_admin_tenant.read_test('snapshot_collection', 'admin')

test_admin_tenant.read_test('subnet', 'tenant')
test_admin_tenant.read_test('subnet', 'admin')


'''
Delete
'''
test_admin_tenant.test_delete("snapshot", tenant_ss_id, "tenant")
test_admin_tenant.test_delete("snapshot", admin_ss_id, "admin")
test_admin_tenant.test_delete("access_control_record", tenant_acr_id, "tenant")
test_admin_tenant.test_delete("access_control_record", admin_acr_id, "admin")
test_admin_tenant.test_delete("initiator", tenant_iid, "tenant")
test_admin_tenant.test_delete("initiator", admin_iid, "admin")
test_admin_tenant.test_delete("initiator_group", tenant_ig_id, "tenant")
test_admin_tenant.test_delete("initiator_group", admin_ig_id, "admin")
test_admin_tenant.test_delete("volume_collection", admin_volcol_id, "admin")
test_admin_tenant.test_delete_volume(tenant_vol_id, "tenant")
test_admin_tenant.test_delete_volume(admin_vol_id, "admin")
test_admin_tenant.test_delete("chap_user", tenant_uid, "tenant")
test_admin_tenant.test_delete("chap_user", admin_uid, "admin")
test_admin_tenant.test_delete("application_server", server_id, "admin")

test_admin_tenant.print_summary()
