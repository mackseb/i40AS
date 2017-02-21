# i40VS

####################################################################
Server Installation (Linux)

Required package
$ sudo apt-get update
$ sudo apt-get install git python-pip python-virtualenv python-dev python3-dev nginx


Create a new virtualenvironment
$ virtualenv -p /usr/bin/python3.5 project_env

Activate the environment
$ . project_env/bin/activate

Install the requirements
$ (project_env/bin/)pip install -r requirements.txt

(If needed) change the folder owner properties
$ chmod -R 777 *

####################################################################
Server commands

sudo systemctl [start/stop/restart] nginx/i40VS
