#!/bin/bash
sudo cp /var/lib/jenkins/workspace/pipeline1/script/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service


sudo systemctl stop flask.service
sudo systemctl start flask.service
sleep 10

source  ~/.bashrc
/var/jenkins_home/workspace/pipelinedockervenv/bin/coverage run -m pytest /var/jenkins_home/workspace/pipelinedocker/testing.py
/var/jenkins_home/workspace/pipelinedocker/venv/bin/coverage report
