#!/bin/bash

#source /var/lib/jenkins/workspace/pipeline/venv/bin/activate
source /var/jenkins_home/workspace/pipelinedocker/venv/bin/activate

pip3 install flask
pip3 install flask_mysqldb
pip3 install -U pytest
pip3 install urllib3
pip3 install coverage
#s
source  ~/.bashrc

python3 /var/jenkins_home/workspace/pipelinedocker/app.py