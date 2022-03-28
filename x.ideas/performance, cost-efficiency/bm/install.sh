#!/bin/bash
sudo coreos-installer install /dev/sda  \
    --ignition-file worker.ign --insecure --insecure-ignition \
    --append-karg ip=172.16.40.100::172.16.43.254:255.255.252.0:okd4-bm-0:bond1.224:none:8.8.8.8 \
    --append-karg vlan=bond1.224:bond1 \
    --append-karg bond=bond1:eno49np0,ens3f1:mode=balance-xor,miimon=100 \
    --delete-karg console=ttyS0,115200n8
