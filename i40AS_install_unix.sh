#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install python3-pip python3-dev nginx -y


pip3 install virtualenv

virtualenv projectenv

source projectenv/bin/activate

pip install -r requirements.txt

deactivate

cp control.service /etc/systemd/system

cp backend.service /etc/systemd/system

cp frontend.service /etc/systemd/system

cp nginx /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/nginx /etc/nginx/sites-enabled

systemctl start control
systemctl enable control

systemctl start backend
systemctl enable backend

systemctl start frontend
systemctl enable frontend
