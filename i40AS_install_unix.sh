#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install python3-pip python3-dev nginx -y


pip3 install virtualenv

virtualenv projectenv

source projectenv/bin/activate

pip install -r requirements.txt

deactivate

sed -i -e "s/USR/$SUDO_USER/g" control.service
sed -i -e "s/USR/$SUDO_USER/g" frontend.service
sed -i -e "s/USR/$SUDO_USER/g" backend.service
sed -i -e "s/USR/$SUDO_USER/g" nginx
address=`ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'`
sed -i -e "s/ADD/$address/g" nginx

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

systemctl restart nginx

systemctl daemon-reload
