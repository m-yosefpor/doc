coreos-installer install /dev/sda \
    --ignition-url https://api.okd4.office-1.staging-snappcloud.io:22623/config/worker \
    --insecure \
    --insecure-ignition \

    --append-karg ip=10.168.48.7::10.168.51.254:255.255.252.0:okd4-bm-0:bond0.226:none \
    --append-karg bond=bond0:enp3s0f1,enp4s0f0:mode=4,miimon=100,lacp_rate=1 \
    --append-karg vlan=bond0.226:bond0 \

    --append-karg nameserver=8.8.8.8 \
    --append-karg nameserver=1.1.1.1 \
    --append-karg ip=::10.168.51.254:::: \
    --append-karg ip=10.10.10.2::10.10.10.254:255.255.255.0:okd4-bm-0:bond1.100:none
    --append-karg bond=bond1:em1,em2:mode=active-backup \
    --append-karg vlan=bond1.100:bond1 \

10.168.48.7


https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/33.20210117.3.2/x86_64/fedora-coreos-33.20210117.3.2-live.x86_64.iso



34.202109181327



      monitored_network_devices:
        - enp3s0f0 # not-bond 1g provisioning (ctlpane, management)
        - enp3s0f1 # bond0    1g external (WAN)
        - enp4s0f0 # bond0    1g external (WAN)
      unused_network_devices:
        - enp4s0f1



      networks:
        internal_api:
          vlan_id: 222
          cidr: 10.168.33.0/24
          allocation_pools: "[{'start': '10.168.33.2', 'end': '10.168.33.200'}]"
        storage:
          vlan_id: 223
          cidr: 10.168.36.0/22
          allocation_pools: "[{'start': '10.168.36.2', 'end': '10.168.39.200'}]"
        storage_mgmt:
          vlan_id: 225
          cidr: 10.168.44.0/22
          allocation_pools: "[{'start': '10.168.44.2', 'end': '10.168.47.200'}]"
        tenant:
          vlan_id: 224
          cidr: 10.168.40.0/22
          allocation_pools: "[{'start': '10.168.40.2', 'end': '10.168.40.200'}]"
        external:
          vlan_id: 226
          cidr: 10.168.48.0/22
          allocation_pools: "[{'start': '10.168.48.2', 'end': '10.168.48.61'}]" # This gives 60 IPs allocatable for baremetals. We can add other allocation pools if needed.
      external_interface: bond0
      external_interface_default_route: 10.168.51.254
      control_plane_subnet_cidr: 24
      control_plane_default_route: 10.168.32.254
      ec2_metadata_ip: 10.168.32.3
      fixed_ip: 10.168.48.201
