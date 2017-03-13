#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install python3-pip python3-dev nginx -y


pip3 install virtualenv

virtualenv projectenv

source projectenv/bin/activate

pip install -r requirements.txt
