#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install python3-pip python3-dev nginx -y


pip3 install virtualenv

virtualenv projectenv

source projectenv/bin/activate

pip install -r install/requirements.txt

deactivate

CURRENTUSER= who am i | awk '{print $1}'
echo $CURRENTUSER

sed -i -e "s/USR/$CURRENTUSER/g" install/control.service
sed -i -e "s/USR/$CURRENTUSER/g" install/frontend.service
sed -i -e "s/USR/$CURRENTUSER/g" install/backend.service
sed -i -e "s/USR/$CURRENTUSER/g" install/nginx
ADDRESS=`ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'`
sed -i -e "s/ADD/$ADDRESS/g" install/nginx

cp install/control.service /etc/systemd/system

cp install/backend.service /etc/systemd/system

cp install/frontend.service /etc/systemd/system

cp install/nginx /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/nginx /etc/nginx/sites-enabled

systemctl start control
systemctl enable control

systemctl start backend

systemctl start frontend
systemctl enable frontend

systemctl restart nginx

systemctl daemon-reload
