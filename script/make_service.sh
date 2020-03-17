#!/bin/bash
sudo cp /var/lib/jenkins/workspace/pipeline1/script/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service


sudo systemctl start flask.service
/var/lib/jenkins/workspace/pipeline1/venv/bin/pytest /var/lib/jenkins/workspace/pipeline1/testing.py
