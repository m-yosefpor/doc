########################### install podman
sudo yum install podman
sudo bash -c 'echo 10000 > /proc/sys/user/max_user_namespaces'
sudo bash -c "echo $(whoami):110000:65536 > /etc/subuid"
sudo bash -c "echo $(whoami):110000:65536 > /etc/subgid"

###############
wget https://github.com/openshift/okd/releases/download/4.5.0-0.okd-2020-09-18-202631/openshift-install-linux-4.5.0-0.okd-2020-09-18-202631.tar.gz
tar xvf openshift-install-linux-4.5.0-0.okd-2020-09-18-202631.tar.gz

###
INSTALLATION_DIR=/home/stack/okd4
CLUSTER_NAME=teh-3
BASE_DOMAIN=snappcloud.io

###
wget $FCOS_IMAGE_URL
openstack image create --container-format=bare --disk-format=qcow2 --file rhcos-${RHCOS_VERSION}-openstack.qcow2 rhcos

# create external network
 openstack network list --long -c ID -c Name -c "Router Type"
 openstack floating ip create --description "API <cluster_name>.<base_domain>" <external network>
 openstack floating ip create --description "Ingress <cluster_name>.<base_domain>" <external network>

### install-config
openshift-install create install-config


## manifests
./openshift-install create manifests --dir=$INSTALLATION_DIR

vi <installation_directory>/manifests/cluster-scheduler-02-config.yml #mastersSchedulable: False

./openshift-install create ignition-configs --dir=<installation_directory>

### ignition files
./openshift-install create install-config --dir=$INSTALLATION_DIR

export INFRA_ID=$(jq -r .infraID metadata.json)

####
openstack image create --disk-format=raw --container-format=bare --file bootstrap.ign okd-fcos

###
cat > $INFRA_ID-bootstrap-ignition.json <<EOF
{
  "ignition": {
    "config": {
      "merge": [{
        "source": "<storage_url>",
        "httpHeaders": [{
          "name": "X-Auth-Token",
          "value": "<token_ID>"
        }]
      }]
    },
    "security": {
      "tls": {
        "certificateAuthorities": [{
          "source": "data:text/plain;charset=utf-8;base64,<base64_encoded_certificate>"
        }]
      }
    },
    "version": "3.1.0"
  }
}
EOF
##### master ign
for index in $(seq 0 2); do
    MASTER_HOSTNAME="$INFRA_ID-master-$index\n"
    python -c "import base64, json, sys;
ignition = json.load(sys.stdin);
files = ignition['storage'].get('files', []);
files.append({'path': '/etc/hostname', 'mode': 420, 'contents': {'source': 'data:text/plain;charset=utf-8;base64,' + base64.standard_b64encode(b'$MASTER_HOSTNAME').decode().strip()}});
ignition['storage']['files'] = files;
json.dump(ignition, sys.stdout)" <master.ign >"$INFRA_ID-master-$index-ignition.json"
done

##### 01_security groups
ansible-playbook -i inventory.yaml 01_security-groups.yaml

#### 02_network configs
ansible-playbook -i inventory.yaml 02_network.yaml

openstack subnet set --dns-nameserver <server_1> --dns-nameserver <server_2> "$INFRA_ID-nodes" #optional
### 03_bootstap
ansible-playbook -i inventory.yaml 03_bootstrap.yaml
openstack console log show "$INFRA_ID-bootstrap" ##verify

### 04_control plane
ansible-playbook -i inventory.yaml 04_control-plane.yaml
openshift-install wait-for bootstrap-complete




##### installl IPI ###### this should move to other place
./openshift-install create cluster --dir=$INSTALLATION_DIR --log-level=info






######## login into cluster
export KUBECONFIG=$INSTALLATION_DIR/auth/kubeconfig
##
oc whoami

#### destroy bootstrap machine
ansible-playbook -i inventory.yaml down-03_bootstrap.yaml


### Creating compute machines
ansible-playbook -i inventory.yaml 05_compute-nodes.yaml

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
