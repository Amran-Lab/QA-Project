#!/bin/bash
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt-get install libmysqlclient-dev -y

rm -r /var/lib/jenkins/workspace/pipeline1/venv
python3 -m venv venv
