from nimbleclient import NimOSClient
import pprint
import random
import string

ACCESS_PROTOCOL = 'iscsi'
IP = "1.1.1.1"
tenant_api = NimOSClient(IP, "xxx", "xxx", tenant_aware=True)
admin_api = NimOSClient(IP, "xxx", "xxx")
failed_test = {
    "count": 0,
    "methodnames": []
}

TENANT_FUNCTIONS = {
    'application_server': tenant_api.application_servers,
    'chap_user': tenant_api.chap_users,
    'volume': tenant_api.volumes,
    'volume_collection': tenant_api.volume_collections,
    'initiator_group': tenant_api.initiator_groups,
    'initiator': tenant_api.initiators,
    'token': tenant_api.tokens,
    'access_control_record': tenant_api.access_control_records,
    'snapshot': tenant_api.snapshots,
    'snapshot_collection': tenant_api.snapshot_collections,
    'folder': tenant_api.folders,
    'group': tenant_api.groups,
    'performance_policy': tenant_api.performance_policies,
    'pool': tenant_api.pools,
    'network_config': tenant_api.network_configs,
    'protection_template': tenant_api.protection_templates,
    'replication_partner': tenant_api.replication_partners,
    'subnet': tenant_api.subnets
}

ADMIN_FUNCTIONS = {
    'application_server': admin_api.application_servers,
    'chap_user': admin_api.chap_users,
    'volume': admin_api.volumes,
    'volume_collection': admin_api.volume_collections,
    'initiator_group': admin_api.initiator_groups,
    'initiator': admin_api.initiators,
    'token': admin_api.tokens,
    'access_control_record': admin_api.access_control_records,
    'snapshot': admin_api.snapshots,
    'snapshot_collection': admin_api.snapshot_collections,
    'folder': admin_api.folders,
    'group': admin_api.groups,
    'performance_policy': admin_api.performance_policies,
    'pool': admin_api.pools,
    'network_config': admin_api.network_configs,
    'protection_template': admin_api.protection_templates,
    'replication_partner': admin_api.replication_partners,
    'subnet': admin_api.subnets
}

''' Helper Functions '''


def generate_random_str(length: int) -> str:
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))


def print_summary():
    print(f"Total failed test: {failed_test['count']}")
    print(
        f"Failed methods: {failed_test['methodnames'] if failed_test['methodnames'] != [] else 'None'}")


def get_vol_by_id(object_id):
    return admin_api.volumes.get(id=object_id)


'''
Create
'''


def test_create(test_object: str, uid_set: set, user: str, **kwargs):
    '''
    user can only be "tenant" or "admin"
    '''
    print(f"TEST: {user.capitalize()} should be able to see {uid_set}")

    if kwargs == {}:
        retrieved_objects = TENANT_FUNCTIONS[test_object].list(
        ) if user.lower() == "tenant" else ADMIN_FUNCTIONS[test_object].list()
    else:
        for key in kwargs:
            if key == 'vol_id':
                retrieved_objects = TENANT_FUNCTIONS[test_object].list(vol_id=kwargs[key]) if user.lower(
                ) == "tenant" else ADMIN_FUNCTIONS[test_object].list(vol_id=kwargs[key])

    objects_ids = set()
    for obj in retrieved_objects:
        objects_ids.add(obj.attrs['id'])

    if uid_set - objects_ids == set():
        print(f"TEST PASSED")
    else:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"{user.capitalize()} create {test_object}")
        print(
            f"TEST FAILED: {user.capitalize()} sees {objects_ids} while the user it created is {uid_set}")


# Tenant creates an application server. Admin should be able to see.


def create_server_test(server_name: str = "servername") -> str:
    print("------- Starting create_server_test ---------")
    print(f"Creating a server with name {server_name}")
    try:
        server = tenant_api.application_servers.get(name=server_name)
        if server == None:
            server = tenant_api.application_servers.create(
                name=server_name, hostname=IP)
        else:
            print("Server has already been created.")
    except Exception as e:
        print(
            f"Failed to create a server with name {server_name}. Message: {e}")
        return None

    tenant_server_sid = server.attrs['id']
    print("TEST: Admin should be able to see the server")
    admin_server = admin_api.application_servers.get(name=server_name)
    if admin_server == None:
        failed_test["count"] += 1
        failed_test["methodnames"].append(f"Admin create application_server")
        print("TEST FAILED: Admin could not find the server.")
    elif admin_server.attrs['id'] != tenant_server_sid:
        failed_test["count"] += 1
        failed_test["methodnames"].append(f"Admin create application_server")
        print(
            f"TEST FAILED: Server id found by admin is {admin_server.attrs['id']} while server id created by tenant is {tenant_server_sid}.")
    else:
        print("TEST PASSED: Admin found the server")

    return tenant_server_sid


def create_chap_user_test(name1: str = "name1", name2: str = "name2") -> str:
    '''
    Tenant and admin eachcreate a chap user.
    Admin should be able to see both users
    Tenant should only see the user it created
    '''

    print("------- Starting create_chap_user_test ---------")
    print(f"Tenant is creating a chap user with name {name1}")
    try:
        tenant_chap_user = tenant_api.chap_users.get(name=name1)
        if tenant_chap_user == None:
            password = generate_random_str(12)
            tenant_chap_user = tenant_api.chap_users.create(
                name=name1, password=password)
        else:
            print(f"A chap user with name {name1} already exists")
    except Exception as e:
        print(f"Failed to create a chap user with name {name1}. Message: {e}")
        return None
    tenant_chap_uid = tenant_chap_user.attrs['id']
    print(f"User created by tenant = {tenant_chap_uid}")

    try:
        print(f"Admin is creating a chap user with name {name2}")
        chap_user = admin_api.chap_users.get(name=name2)
        if chap_user == None:
            password = generate_random_str(12)
            chap_user = admin_api.chap_users.create(
                name=name2, password=password)
        else:
            print(f"A chap user with name {name2} already exists")
    except Exception as e:
        print(f"Failed to create a chap user with name {name2}. Message: {e}")
        return None
    admin_chap_uid = chap_user.attrs['id']
    print(f"User created by admin = {admin_chap_uid}")

    test_create("chap_user", {tenant_chap_uid, admin_chap_uid}, "admin")
    test_create("chap_user", {tenant_chap_uid}, "tenant")

    return [tenant_chap_uid, admin_chap_uid]


def create_volume_test(name1: str = "vol1", name2: str = "vol2") -> str:
    '''
    Admin and tenant each creates a volume
    Admin should be able to see both volume
    Tenant should only see the volume it created
    '''
    print("------- Starting create_volume_test ---------")
    print(f"Tenant is creating a volume with name {name1}")
    try:
        tenant_volume = tenant_api.volumes.get(name=name1)
        if tenant_volume == None:
            # TODO: replace folder id
            tenant_volume = tenant_api.volumes.create(
                name=name1, size=1024, folder_id="<folderid>")
        else:
            print(f"A volume with name {name1} already exists")
    except Exception as e:
        print(f"Failed to create a volume with name {name1}. Message: {e}")
        return None
    tenant_vol_id = tenant_volume.attrs['id']
    print(f"Volume created by tenant = {tenant_vol_id}")

    try:
        print(f"Admin is creating a volume with name {name2}")
        admin_volume = admin_api.volumes.get(name=name2)
        if admin_volume == None:
            admin_volume = admin_api.volumes.create(name=name2, size=1024)
        else:
            print(f"A volume with name {name2} already exists")
    except Exception as e:
        print(f"Failed to create a volume with name {name2}. Message: {e}")
        return None
    admin_vol_id = admin_volume.attrs['id']
    print(f"Volume created by admin = {admin_vol_id}")

    test_create("volume", {tenant_vol_id, admin_vol_id}, "admin")
    test_create("volume", {tenant_vol_id}, "tenant")

    return [tenant_vol_id, admin_vol_id]


def create_volume_collection_test(name1: str = "volcoll1", name2: str = "volcoll2") -> str:
    '''
    Admin and tenant each creates a volume collection
    Admin should be able to see both volume collections
    Tenant should only see the volume collection it created
    '''
    print("------- Starting create_volume_collection_test ---------")
    print(f"Tenant is creating a volume collection with name {name1}")
    try:
        tenant_volume = tenant_api.volume_collections.get(name=name1)
        if tenant_volume == None:
            tenant_volume = tenant_api.volume_collections.create(name=name1)
        else:
            print(f"A volume collection with name {name1} already exists")
    except Exception as e:
        print(
            f"Failed to create a volume collection with name {name1}. Message: {e}")
        return None
    tenant_vol_id = tenant_volume.attrs['id']
    print(f"Volume collection created by tenant = {tenant_vol_id}")

    try:
        print(f"Admin is creating a volume collection with name {name2}")
        admin_volume = admin_api.volume_collections.get(name=name2)
        if admin_volume == None:
            admin_volume = admin_api.volume_collections.create(name=name2)
        else:
            print(f"A volume collection with name {name2} already exists")
    except Exception as e:
        print(
            f"Failed to create a volume collection with name {name2}. Message: {e}")
        return None
    admin_vol_id = admin_volume.attrs['id']
    print(f"Volume collection created by admin = {admin_vol_id}")

    test_create("volume_collection", {tenant_vol_id, admin_vol_id}, "admin")
    test_create("volume_collection", {tenant_vol_id}, "tenant")

    return [tenant_vol_id, admin_vol_id]


def create_initiator_group_test(name1: str = "ig1", name2: str = "ig2") -> str:
    '''
    Admin and tenant each creates an initiator group
    Admin should be able to see both initiator groups
    Tenant should only see the initiator group it created
    '''
    print("------- Starting create_initiator_group_test ---------")
    print(f"Tenant is creating an initiator group with name {name1}")
    try:
        tenant_initator = tenant_api.initiator_groups.get(name=name1)
        if tenant_initator == None:
            tenant_initator = tenant_api.initiator_groups.create(
                name=name1, access_protocol=ACCESS_PROTOCOL)
        else:
            print(f"An initiator group with name {name1} already exists")
    except Exception as e:
        print(
            f"Failed to create an initiator group with name {name1}. Message: {e}")
        return None
    tenant_init_id = tenant_initator.attrs['id']
    print(f"Initiator group created by tenant = {tenant_init_id}")

    try:
        print(f"Admin is creating an initiator group with name {name2}")
        admin_initiator = admin_api.initiator_groups.get(name=name2)
        if admin_initiator == None:
            admin_initiator = admin_api.initiator_groups.create(
                name=name2, access_protocol=ACCESS_PROTOCOL)
        else:
            print(f"An initiator group with name {name2} already exists")
    except Exception as e:
        print(
            f"Failed to create an initiator group with name {name2}. Message: {e}")
        return None
    admin_init_id = admin_initiator.attrs['id']
    print(f"Initiator group created by admin = {admin_init_id}")

    test_create("initiator_group", {tenant_init_id, admin_init_id}, "admin")
    test_create("initiator_group", {tenant_init_id}, "tenant")

    return [tenant_init_id, admin_init_id]


def create_initiator_test(initiator_group_id: str, lbl1: str = "vol1", lbl2: str = "vol2", iqn1="iqn.1992-01.com.example:storage.tape1.sys1.xyz", iqn2="iqn.1992-01.com.example:storage.tape1.sys1.xyx") -> str:
    '''
    Admin and tenant each creates an initiator
    Admin should be able to see both initiators
    Tenant should only see the initiator it created
    '''
    print("------- Starting create_initiator_test ---------")
    print(f"Tenant is creating an initiator with label {lbl1}")
    try:
        tenant_initator = tenant_api.initiators.get(label=lbl1)
        if tenant_initator == None:
            tenant_initator = tenant_api.initiators.create(
                label=lbl1, iqn=iqn1, ip_address=IP, initiator_group_id=initiator_group_id, access_protocol=ACCESS_PROTOCOL)
        else:
            print(f"An initiator with label {lbl1} already exists")
    except Exception as e:
        print(f"Failed to create an initiator with label {lbl1}. Message: {e}")
        return None
    tenant_init_id = tenant_initator.attrs['id']
    print(f"Initiator created by tenant = {tenant_init_id}")

    try:
        print(f"Admin is creating an initiator with label {lbl2}")
        admin_initiator = admin_api.initiators.get(label=lbl2)
        if admin_initiator == None:
            admin_initiator = admin_api.initiators.create(
                label=lbl2, iqn=iqn2, ip_address=IP, initiator_group_id=initiator_group_id, access_protocol=ACCESS_PROTOCOL)
        else:
            print(f"An initiator with label {lbl2} already exists")
    except Exception as e:
        print(f"Failed to create an initiator with label {lbl2}. Message: {e}")
        return None
    admin_init_id = admin_initiator.attrs['id']
    print(f"Initiator created by admin = {admin_init_id}")

    test_create("initiator", {tenant_init_id, admin_init_id}, "admin")
    test_create("initiator", {tenant_init_id}, "tenant")

    return [tenant_init_id, admin_init_id]


def create_token_test(name1: str = "name1", name2: str = "admin") -> str:
    '''
    Admin and tenant each creates a token
    Admin should be able to see both tokens
    Tenant should only see the token it created
    '''
    print("------- Starting create_token_test ---------")
    print(f"Tenant is creating a token with username {name1}")
    try:
        tenant_token = tenant_api.tokens.get(username=name1)
        if tenant_token == None:
            password = generate_random_str(10)
            tenant_token = tenant_api.tokens.create(
                username=name1, password=password)
        else:
            print(f"A token with username {name1} already exists")
    except Exception as e:
        print(f"Failed to create a token with username {name1}. Message: {e}")
        return None
    tenant_token_id = tenant_token.attrs['id']
    print(f"Token created by tenant = {tenant_token_id}")

    try:
        print(f"Admin is creating a token with username {name2}")
        admin_token = admin_api.tokens.get(username=name2)
        if admin_token == None:
            password = "admin"
            admin_token = admin_api.tokens.create(
                username=name2, password=password)
        else:
            print(f"A token with username {name2} already exists")
    except Exception as e:
        print(f"Failed to create a token with username {name2}. Message: {e}")
        return None
    admin_token_id = admin_token.attrs['id']
    print(f"Token created by admin = {admin_token_id}")

    test_create("token", {tenant_token_id, admin_token_id}, "admin")
    test_create("token", {tenant_token_id}, "tenant")

    return [tenant_token_id, admin_token_id]


def create_access_control_records_test(initiator_group_id1: str, vol_id1: str, initiator_group_id2: str, vol_id2: str) -> str:
    '''
    Admin and tenant each creates a token
    Admin should be able to see both tokens
    Tenant should only see the token it created
    '''
    print("------- Starting create_access_control_records_test ---------")
    print(
        f"Tenant is creating an ACR with for initiator group id {initiator_group_id1} and volume id {vol_id1}")
    try:
        tenant_acr = tenant_api.access_control_records.get(
            initiator_group_id=initiator_group_id1, vol_id=vol_id1)
        if tenant_acr == None:
            tenant_acr = tenant_api.access_control_records.create(
                initiator_group_id=initiator_group_id1, vol_id=vol_id1)
        else:
            print(
                f"ACR for initiator group id {initiator_group_id1} and volume id {vol_id1} already exists")
    except Exception as e:
        print(
            f"Failed to create an ACR for initiator group id {initiator_group_id1} and volume id {vol_id1}. Message: {e}")
        return None
    tenant_acr_id = tenant_acr.attrs['id']
    print(f"ACR created by tenant = {tenant_acr_id}")

    try:
        print(
            f"Admin is creating an ACR for initiator group id {initiator_group_id2} and volume id {vol_id2}")
        admin_acr = admin_api.access_control_records.get(
            initiator_group_id=initiator_group_id2, vol_id=vol_id2)
        if admin_acr == None:
            admin_acr = admin_api.access_control_records.create(
                initiator_group_id=initiator_group_id2, vol_id=vol_id2)
        else:
            print(
                f"ACR for initiator group id {initiator_group_id2} and volume id {vol_id2}")
    except Exception as e:
        print(
            f"Failed to create an ACR for initiator group id {initiator_group_id2} and volume id {vol_id2}. Message: {e}")
        return None
    admin_acr_id = admin_acr.attrs['id']
    print(f"ACR created by admin = {admin_acr_id}")

    test_create("access_control_record", {
                tenant_acr_id, admin_acr_id}, "admin")
    test_create("access_control_record", {tenant_acr_id}, "tenant")

    return [tenant_acr_id, admin_acr_id]


def create_snapshot_test(vol_id1, vol_id2, name1: str = "snap1", name2: str = "snap2") -> str:
    '''
    Admin and tenant each creates a snapshot
    Admin should be able to see tenant's snapshot
    Tenant should only see the snapshot it created
    '''
    print("------- Starting create_snapshot_test ---------")
    print(f"Tenant is creating a snapshot with name {name1}")
    try:
        tenant_snapshot = tenant_api.snapshots.get(name=name1)
        if tenant_snapshot == None:
            tenant_snapshot = tenant_api.snapshots.create(
                name=name1, vol_id=vol_id1)
        else:
            print(f"A snapshot with name {name1} already exists")
    except Exception as e:
        print(f"Failed to create a snapshot with name {name1}. Message: {e}")
        return None
    tenant_ss_id = tenant_snapshot.attrs['id']
    print(f"Snapshot created by tenant = {tenant_ss_id}")

    try:
        print(f"Admin is creating a snapshot with name {name2}")
        admin_snapshot = admin_api.snapshots.get(name=name2, vol_id=vol_id2)
        if admin_snapshot == None:
            admin_snapshot = admin_api.snapshots.create(
                name=name2, vol_id=vol_id2)
        else:
            print(f"A snapshot with name {name2} already exists")
    except Exception as e:
        print(f"Failed to create a snapshot with name {name2}. Message: {e}")
        return None
    admin_ss_id = admin_snapshot.attrs['id']
    print(f"Snapshot created by admin = {admin_ss_id}")

    # test admin can see tenant's snapshot
    test_create("snapshot", {tenant_ss_id},
                "admin", vol_id=vol_id1)
    # test admin can see their snapshot
    test_create("snapshot", {admin_ss_id},
                "admin", vol_id=vol_id2)
    test_create("snapshot", {tenant_ss_id}, "tenant")

    return [tenant_ss_id, admin_ss_id]


def create_snapshot_collection_test(volcol_id1, volcol_id2, name1: str = "volcoll1", name2: str = "volcoll2") -> str:
    '''
    Admin creates a snapshot collection
    Admin should be able to see its snapshot collections
    '''
    try:
        print(f"Admin is creating a snapshot collection with name {name2}")
        admin_ssc = admin_api.snapshot_collections.get(name=name2)
        if admin_ssc == None:
            admin_ssc = admin_api.snapshot_collections.create(
                name=name2, volcoll_id=volcol_id2)
        else:
            print(f"A snapshot collection with name {name2} already exists")
    except Exception as e:
        print(
            f"Failed to create a snapshot collection with name {name2}. Message: {e}")
        return None
    admin_ssc_id = admin_ssc.attrs['id']
    print(f"snapshot collection created by admin = {admin_ssc_id}")

    test_create("snapshot_collection", {admin_ssc_id}, "admin")

    return [admin_ssc_id]


'''
Update
'''


def test_update_description(test_object: str, object_id_tenant: str, object_id_admin: str, description_tenant="tenant-new-description", description_admin="admin-new-description"):
    print(
        f"------- Starting test_update_description on {test_object}---------")
    print(
        f"TEST: Tenant try to update {test_object} with id {object_id_tenant}")
    try:
        TENANT_FUNCTIONS[test_object].update(
            id=object_id_tenant, description=description_tenant)
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"Tenant updates {test_object}")
        print(
            f"TEST FAILED: Tenant fails to update {test_object} with id {object_id_tenant}")
        print(f"Error message: {e}")
        return
    print(f"TEST PASSED")

    print(
        f"TEST: Admn try to update {test_object} with id {object_id_admin}")

    try:
        ADMIN_FUNCTIONS[test_object].update(
            id=object_id_admin, description=description_admin)
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"Admin updates {test_object}")
        print(
            f"TEST FAILED: Admin fails to update {test_object} with id {object_id_admin}")
        print(f"Error message: {e}")
        return
    print(f"TEST PASSED")

    print(
        f"TEST: Tenant should be able to see the new desctiption")
    try:
        obj_tenant = TENANT_FUNCTIONS[test_object].get(id=object_id_tenant)
        if obj_tenant.attrs['description'] != description_tenant:
            failed_test["count"] += 1
            failed_test["methodnames"].append(
                f"Tenant reads new update from tenant: {test_object}")
            print(
                f"TEST FAILED: Description doesn't match.")
            return
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"Tenant reads update {test_object}")
        print(
            f"TEST FAILED: {e}")
        return
    print(f"TEST PASSED")

    print(
        f"TEST: Admin should be able to see the tenant's new description and its new description")
    try:
        obj_tenant = ADMIN_FUNCTIONS[test_object].get(id=object_id_tenant)
        obj_admin = ADMIN_FUNCTIONS[test_object].get(id=object_id_admin)
        if obj_tenant.attrs['description'] != description_tenant:
            failed_test["count"] += 1
            failed_test["methodnames"].append(
                f"Admin read new update from tenant: {test_object}")
            print(
                f"TEST FAILED: Description doesn't match.")
            return

        if obj_admin.attrs['description'] != description_admin:
            failed_test["count"] += 1
            failed_test["methodnames"].append(
                f"Admin read new update from admin: {test_object}")
            print(
                f"TEST FAILED: Description doesn't match.")
            return
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"Admin reads updates{test_object}")
        print(
            f"TEST FAILED: {e}")
        return
    print(f"TEST PASSED")


'''
READ
'''


def read_test(test_object, user, object_id=None):
    print(
        f"------- Starting read_test on {test_object}---------")
    print(
        f"TEST: {user.capitalize()} try to read {test_object}")

    api = TENANT_FUNCTIONS[test_object] if user.lower(
    ) == "tenant" else ADMIN_FUNCTIONS[test_object]

    data = None
    try:
        if object_id == None:
            data = api.get()
        else:
            data = api.get(id=object_id)

        if data == None or data.attrs["id"] == None:
            failed_test["count"] += 1
            failed_test["methodnames"].append(
                f"{user.capitalize()} reads {test_object}")
            print(
                f"TEST FAILED: {test_object} unable to retrieve data")
            return
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"{user.capitalize()} reads {test_object}")
        print(
            f"TEST FAILED: {e}")
        return
    print("TEST PASSED")


'''
Delete
'''


def test_delete(test_object: str, object_id, user):
    '''
    user can only be "tenant" or "admin"
    '''
    print(
        f"TEST: {user.capitalize()} try to delete {test_object} with id {object_id}")
    try:
        if user.lower() == "tenant":
            TENANT_FUNCTIONS[test_object].delete(id=object_id)
        else:
            ADMIN_FUNCTIONS[test_object].delete(id=object_id)
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"{user.capitalize()} delete {test_object}")
        print(
            f"TEST FAILED: {user.capitalize()} fails to delete {test_object} with id {object_id}")
        print(f"Error message: {e}")
        return
    print(f"TEST PASSED")


def test_delete_volume(object_id: str, user):
    '''
    user can only be "tenant" or "admin"
    '''
    print(
        f"TEST: {user.capitalize()} try to delete volume with id {object_id}")
    try:
        if user.lower() == "tenant":
            vol = tenant_api.volumes.get(id=object_id)
            vol.offline()
            vol.delete()
        else:
            vol = admin_api.volumes.get(id=object_id)
            vol.offline()
            vol.delete()
    except Exception as e:
        failed_test["count"] += 1
        failed_test["methodnames"].append(
            f"{user.capitalize()} delete volume")
        print(
            f"TEST FAILED: {user.capitalize()} fails to delete volume with id {object_id}")
        print(f"Error message: {e}")
        return
    print(f"TEST PASSED")
