# provision
ansible-playbook -s kube-playbook -i hosts
ansible -b -K -m ping all -i hosts 
