#!/bin/bash
source venv/bin/activate
sudo pip3 install flask
sudo pip3 install flask_mysqldb
source  ~/.bashrc
python3 app.py