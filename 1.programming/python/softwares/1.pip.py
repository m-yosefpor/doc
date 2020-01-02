never use:
    sudo pip install

use:
    1) sudo apt install python3-package1
    2) pip install --user sth # add user installation to PATH env
    3) virtual env #for pip install where it's not in linux repos
    4) conda



#3
p -m venv env1
. ./env1/bin/activate
pip install black
which black
deactivate
