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
    ip addr add 172.16.30.100/24 dev eno3
    ip r a default via 172.16.30.254


1. install coreos on sda using

```sh
curl 172.16.51.122:8000/worker.ign > worker.ign
curl 172.16.51.122:8000/install.sh > install.sh
chmod +x install.sh
./install.sh
```

1. after finish installation you need to manual reboot `sudo reboot` and wait for BM to boot from sda and load ignition config
1. ??? ssh to BM using `enp3s0f0`(whatever?) ip address xxx.xxx.32.xx and set hostname in /etc/hostname and chmod 0644
