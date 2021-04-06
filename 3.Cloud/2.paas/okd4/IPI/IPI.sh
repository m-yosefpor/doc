different interfaces # done
external network # probably done
more customizable?? what do we want? #day2 add interface?
##
super easy, super fast
more reliable
machineSet + clusterautoscaler
cinde-csi out of the box
kuryr (upi?)



### Download openshift-installer
wget https://github.com/openshift/okd/releases/download/4.5.0-0.okd-2020-09-18-202631/openshift-install-linux-4.5.0-0.okd-2020-09-18-202631.tar.gz
tar xvf openshift-install-linux-4.5.0-0.okd-2020-09-18-202631.tar.gz

### vars
INSTALLATION_DIR=/home/stack/okd4/install

###
sudo cp ca.crt.pem /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust extract
## create two floating ips
openstack network create test --external
openstack subnet create test --network test --subnet-range 10.168.52.0/24 --no-dhcp --allocation-pool start=10.168.52.2,end=10.168.52.22 --gateway 10.168.51.254 192.168.52.254
openstack floating ip create test
openstack floating ip create test


### install-config
./openshift-install create install-config


##### installl IPI
mkdir install
cp install-config.yaml install
./openshift-install create cluster --dir=install --log-level=debug

######## login into cluster
export KUBECONFIG=$INSTALLATION_DIR/auth/kubeconfig
##
oc whoami

### Approving the CSRs for your machines
oc get no
oc get csr
oc adm certificate approve <csr_name>
oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve

#### verify
openshift-install --log-level debug wait-for install-complete

### Configuring application access with floating IP addresses
openstack port show <cluster name>-<clusterID>-ingress-port
openstack floating ip set --port <ingress port ID> <apps FIP>
*.apps.<cluster name>.<base domain>  IN  A  <apps FIP>
