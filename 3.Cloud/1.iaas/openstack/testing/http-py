import requests #http://docs.python-requests.org/en/latest
import json
KEYSTONE_URL= 'http://controller:5000/v2.0/'
TENANT='demo'
USERNAME= 'demo'
PASSWORD= 'secret'
r = requests.post("%s/tokens"% (KEYSTONE_URL,), 
	json={
		"auth": {
			"tenantName": TENANT,
			"passwordCredentials": {
				"username": USERNAME,
				"password": PASSWORD,
			}
		}
	})

if r.ok:
token = r.json()['access']['token']['id']
else:
raise Exception(r.text)


# Place the token in the X-Auth-Token header
headers = {'X-Auth-Token': token}


# Find the link to the Nova API in the service catalog:
for service in r.json()['access']['serviceCatalog']:
	if service['type'] == 'compute':
		nova_endpoint = service['endpoints'][0]['publicURL']
	if service['type'] == 'network':
		neutron_endpoint = service['endpoints'][0]['publicURL']

# For example, if our tenant ID is 8ce08c9fa6c54ba094be743a55dc5b9a , our Nova endpoint will be
# http://10.3.71.50:8774/v2/8ce08c9fa6c54ba094be743a55dc5b9
# As such, the only endpoint that shouldn't be dynamically determined is the Keystone endpoint. All other endpoints that need to be interacted with should be pulled from the service catalog


keypair_ref = None
# Get the list of available keypairs:
keypairs = requests.get("%s/os-keypairs"% nova_endpoint,
headers=headers)
# take the first one

keypair_ref = None
# Get the list of available keypairs:
keypairs = requests.get("%s/os-keypairs"% nova_endpoint,
headers=headers)
# take the first one

keypair_ref = keypairs.json()['keypairs'][0]['keypair']['name']
image_ref = None
# Get the list of available images:
images = requests.get("%s/images"% nova_endpoint,
headers=headers)
# Select the "cirros" image:
for image in images.json()['images']:
if image['name'] == 'cirros':
image_ref = image['id']
flavor_ref = None
# Get the list of available flavors:
flavors = requests.get("%s/flavors"% nova_endpoint,
headers=headers)
# Select the "m1.small" flavor
for flavor in flavors.json()['flavors']:
if flavor['name'] == 'm1.small':
flavor_ref = flavor['id']
network_ref = None
# Get the list of available networks:
networks = requests.get("%s/v2.0/networks"% neutron_endpoint,
headers=headers)
# Select the "private" network
for network in networks.json()['networks']:
if network['name'] == 'private':
network_ref = network['id']

'''Nova endpoint includes a version string (v2), the
Neutron endpoint does not. Also, note that the Neutron endpoint does not
include the tenant ID'''

# Launch the instance:
server = requests.post("%s/servers"% (nova_endpoint,), json={

"server": {
"name": "new_server",
"imageRef": image_ref,
"flavorRef": flavor_ref,
"key_name": keypair_ref,
"networks": [{
"uuid": network_ref
}]
}
},
headers=headers)
#status of the instance:
server_ref = server.json()['server']['id']
requests.get(server.json()['server']['links'][0]['href'],
headers=headers)
#action	
server_url = server.json()['server']['links'][0]['href']
stop = requests.post("%s/action"% (server_url,), json={
"os-stop": None
}, headers=headers)
#delete an instance
delete = requests.delete(server_url, headers=headers)


#### READ PAG# 139 (OPENSTACK FOR ARCHITECTS), PROGRAM HEAT IS EASIER
Heat performs the name-to-ID translations for us, so we don't need to look up the reference for the flavor, image, key, or network

Perhaps the most important feature of the Heat API, though, is the ability to reference an
external template

