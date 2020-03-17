#!/bin/bash

source /var/lib/jenkins/workspace/pipeline1/venv/bin/activate

pip3 install flask
pip3 install flask_mysqldb
pip3 install -U pytest
pip3 install urllib3
pip3 install coverage
#s
source  ~/.bashrc

python3 /var/lib/jenkins/workspace/pipeline1/app.py