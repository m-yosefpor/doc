1. Download the FCOS  iso from https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/33.20210117.3.2/x86_64/fedora-coreos-33.20210117.3.2-live.x86_64.iso

1. Verify shasum -a 256 CentOS-7-x86_64-DVD-1808.iso matches what CentOS.org shows.

1. Ask DC team to put it on a webserver and note the URL

1. Download java 8 from oracle archive (you can create an account and use VPN)

1. Go to ilo page login with creds from gopass

1. Go to start java-based ILO, download applet and start the program



1. Start the Java-based ILO console:

    Go to Virtual Drives > Image File from CD/DVD-ROM and select the Minimal ISO file.

    Go to Power Switch > Reset.

    When you see the HP logo and the option to pick a F* options, use F9 to change the boot order so the baremetal boots from the ILO-mounted CD/DVD from your machine.

    Reboot the machine from the boot menu options.

    Start coreos live



1. config eno3
    nmcli con mod eno3 ipv4.addresses 192.168.2.20/24
    nmcli con mod eno3 ipv4.dns "8.8.8.8"
    nmcli con mod eno3 ipv4.method manual
    nmcli con up eno3

1. from utility node copy the ignition file ` ~/ignition-configs/worker.ign` and create file named worker.ign

1. install coreos on sda using


    coreos-installer install /dev/sda  \
        --ignition-file worker.ign --insecure --insecure-ignition \
        #--ignition-url https://api.okd4.ts-2.staging-snappcloud.io:22623/config/worker \
        --append-karg ip=172.21.32.100:::255.255.255.0:okd4-bm-0:eno1:none \
        --append-karg ip=172.21.48.100:::255.255.252.0:okd4-bm-0:bond0.226:none \
        --append-karg vlan=bond0.226:bond0 \
        --append-karg ip=172.21.40.100::172.21.43.254:255.255.252.0:okd4-bm-0:bond1.224:none \
        --append-karg vlan=bond1.224:bond1 \
        --append-karg nameserver=8.8.8.8 \
        --append-karg nameserver=1.1.1.1 \
        --append-karg bond=bond1:eno49,ens3f1:mode=balance-xor,miimon=100 \
        --append-karg bond=bond0:eno2,ens2f3:mode=balance-xor,miimon=100 \
        --delete-karg 'console=ttyS0,115200n8'

1. after finish installation you need to manual reboot `sudo reboot` and wait for BM to boot from sda and load ignition config
1. ??? ssh to BM using `enp3s0f0`(whatever?) ip address xxx.xxx.32.xx and set hostname in /etc/hostname and chmod 0644
