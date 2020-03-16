#!/bin/bash
source venv/bin/activate
cd venv/bin
pip3 install flask
pip3 install flask_mysqldb
source  ~/.bashrc
cd /var/lib/jenkins/workspace/pipeline1
python3 app.py