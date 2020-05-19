# Overview

These example workflows constitutes an introduction to the HPE Nimble Storage SDK for Python. It may be used to get familiar both HPE Nimble Storage and NimbleOS as a product as well as getting familiar with the SDK.

The examples are available to [browse on GitHub](https://github.com/hpe-storage/nimble-python-sdk/tree/master/workflows).

[TOC]

## Setup

Ensure Python 3.6+, `pip` and `git` is installed on your workstation. 

```markdown
pip install nimble-sdk
git clone https://github.com/hpe-storage/nimble-python-sdk
cd nimble-python-sdk/workflows
```

It's possible to run the example scripts interactively, but it's more convenient to configure the accompanied `workflow_config.json`:

```json
{
  "hostname":"192.168.1.100",  # Set these to point to the array being used
  "username":"admin",
  "password":"admin",
  "vol_name":"wfvol",
  "ig_name":"wfig",
  "mk_name":"default",
  "mk_phrase":"test-phrase11",
  "protection_sched":"ps1"
}
```

Scripts can be run with the `--query_login` paramater to interactively login to the Nimble array (credentials are not stored anywhere).

!!! tip
    All examples below assumes current working directory `nimble-python-sdk/workflows`

##  Interactive explorer

As a starting point, running the interactive explorer allows a user to interact with a Nimble array using the SDK.

```markdown
python nimble_sdk_helper.py
```

Source code: [nimble_sdk_helper.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/nimble_sdk_helper.py)

## Individual workflows

Each workflow creates objects to manipulate. If it's not desirable to have objects lingering around on the array, run the scripts with the `--cleanup` parameter.

!!! note "Good to know"
    The example outputs below is run in sequence running from the top on a clean array.

### Create a volume

Creates a volume on the array.

```markdown
python create_volume.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Create Volume

Running:
    Create Volume "wfvol": Created Id: 0649686580b78e0b16000000000000000000000017
```

Source code: [create_volume.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/create_volume.py)

### List objects

List objects on the array.

```markdown
python list_objects.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: List Objects

Generating Objects...
    Create Volume "wfvol0": Created Id: 0649686580b78e0b16000000000000000000000018
    Create Snapshot "wfvolsnap0.0": Created Id: 0449686580b78e0b1600000000000000210000004f
    Create Snapshot "wfvolsnap0.1": Created Id: 0449686580b78e0b16000000000000002100000050
    Create Snapshot "wfvolsnap0.2": Created Id: 0449686580b78e0b16000000000000002100000051
    Create Volume "wfvol1": Created Id: 0649686580b78e0b16000000000000000000000019
    Create Snapshot "wfvolsnap1.0": Created Id: 0449686580b78e0b16000000000000002200000052
    Create Snapshot "wfvolsnap1.1": Created Id: 0449686580b78e0b16000000000000002200000053
    Create Snapshot "wfvolsnap1.2": Created Id: 0449686580b78e0b16000000000000002200000054

Running:

    Objects on Array:
        VOLUME: wfvol0, Id: 0649686580b78e0b16000000000000000000000018
            SNAPSHOT: wfvolsnap0.0, Id: 0449686580b78e0b1600000000000000210000004f
            SNAPSHOT: wfvolsnap0.1, Id: 0449686580b78e0b16000000000000002100000050
            SNAPSHOT: wfvolsnap0.2, Id: 0449686580b78e0b16000000000000002100000051
        VOLUME: wfvol, Id: 0649686580b78e0b16000000000000000000000017
        VOLUME: wfvol1, Id: 0649686580b78e0b16000000000000000000000019
            SNAPSHOT: wfvolsnap1.0, Id: 0449686580b78e0b16000000000000002200000052
            SNAPSHOT: wfvolsnap1.1, Id: 0449686580b78e0b16000000000000002200000053
            SNAPSHOT: wfvolsnap1.2, Id: 0449686580b78e0b16000000000000002200000054
```

Source code: [list_objects.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/list_objects.py)

### Create a snapshot

Creates a snapshot on an example volume.

```markdown
python create_snapshot.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Create Snapshot

Running:
    Create Volume "wfvol": Already exists. Continuing.
    Create Snapshot "wfvolsnap": Created Id: 0449686580b78e0b16000000000000002000000055
```

Source code: [create_snapshot.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/create_snapshot.py)

### Create initiator group

Create an initiator group.

```markdown
python create_and_update_initiator_group.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Create And Update Initiator Group

Running:
    Create Initiator Group "wfig": Created Id: 0249686580b78e0b16000000000000000000000005
    Current initiator count: 0
    Added initiator "wftest-itor1": {'label': 'wftest-itor1', 'ip_address': '1.1.1.1', 'iqn': 'iqn.1992-01.com.example:storage.tape1.sys1.xyz'}
    Current initiator count: 1
```

Source code: [create_and_update_initiator_group.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/create_and_update_initiator_group.py)

### Publish volume

Publishes a volume to a host.

```markdown
python publish_volume.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Publish Volume

Running:
    Create Volume "wfvol": Already exists. Continuing.
    Create Initiator Group "wfig": Already exists. Continuing.
    Create Access Control Record: Created Id: 0d49686580b78e0b16000000000000000000000004
```

Source code: [publish_volume.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/publish_volume.py)

### Detach volume

Detach volume from a host.

```markdown
python detach_volume.py 

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Detach Volume

Running:
    Create Volume "wfvol": Already exists. Continuing.
    Create Initiator Group "wfig": Already exists. Continuing.
    Create Access Control Record: Already exists. Continuing.
    Cleanup Acccess Control Record: Deleted Id: 0d49686580b78e0b16000000000000000000000004
    Cleanup Initiator Group "wfig": Deleted Id: 0249686580b78e0b16000000000000000000000005
    Cleanup Vol "wfvol": Offlined and deleted Id: 0649686580b78e0b16000000000000000000000017
```

Source code: [detach_volume.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/detach_volume.py)

### Create a clone

Create a clone from a snapshot.

```markdown
python create_clone.py 

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Create Clone

Running:
    Create Volume "wfvol": Created Id: 0649686580b78e0b1600000000000000000000001a
    Create Snapshot "wfvolsnap": Created Id: 0449686580b78e0b16000000000000002300000056
    Create Clone "wfvolclone": Created Id: 0649686580b78e0b1600000000000000000000001b
```

Source code: [create_clone.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/create_clone.py)

### Create access control record

Create an access control record (ACR) for a volume.

```markdown
python create_access_control_record.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Create Access control Record

Running:
    Create Volume "wfvol": Already exists. Continuing.
    Create Initiator Group "wfig": Created Id: 0249686580b78e0b16000000000000000000000006
    Create Access Control Record: Created Id: 0d49686580b78e0b16000000000000000000000005
```

Source code: [create_access_control_record.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/create_access_control_record.py)

### Create a clone and publish

Create a clone from a snapshot and publish to a host.

```markdown
python clone_and_publish_volume.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Clone And Publish Volume

Running:
    Create Volume "wfvol": Already exists. Continuing.
    Create Snapshot "wfvolsnap": Already exists. Continuing.
    Create Clone "wfvolclone": Already exists. Continuing.
    Create Initiator Group "wfvolcloneig": Created Id: 0249686580b78e0b16000000000000000000000007
    Create Access Control Record: Created Id: 0d49686580b78e0b16000000000000000000000006
```

Source code: [clone_and_publish_volume.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/clone_and_publish_volume.py)

### Protect volume

Protect a volume with a volume collection and protection schedule.

```markdown
python protect_volume.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Protect Volume

Running:
    Create Volume "wfvol": Already exists. Continuing.
    Create Volume Collection "wfvolvolcoll": Created Id: 0749686580b78e0b16000000000000000000000006
    Associate Volume: Volume "wfvol" associated with volume vollection "wfvolvolcoll"
    Create Protection Schedule "ps1": Created Id: 0c49686580b78e0b1600000000000000000000000a
```

Source code: [protect_volume.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/protect_volume.py)

### Configures encryption

Setup encryption on the Nimble array.

```markdown
python configure_encryption.py

Attempting to establish connection to array:
    Hostname: 192.168.59.128
    Username: admin
    Connection successful!

WORKFLOW: Configure Encryption

Running:
    Got group: "nva-test-grp", Id: 0049686580b78e0b16000000000000000000000001
    Current encryption:  {'master_key_set': False, 'mode': 'none', 'scope': 'none', 'cipher': 'none', 'encryption_active': False}
    Create Master Key "default": Created Id: 2449686580b78e0b16000000000000000000000001
    Create Encrypted Volume "wfvolencrypted": Created Id: 0649686580b78e0b16000000000000000000000013
    Updated encryption:  {'master_key_set': True, 'mode': 'available', 'scope': 'group', 'cipher': 'aes_256_xts', 'encryption_active': True}
    Modified encryption: {'master_key_set': True, 'mode': 'secure', 'scope': 'group', 'cipher': 'aes_256_xts', 'encryption_active': True}
```

Source code: [configure_encryption.py](https://github.com/hpe-storage/nimble-python-sdk/blob/master/workflows/configure_encryption.py)
