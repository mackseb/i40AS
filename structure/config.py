import os



data_windows ={
'HTTPIN': {'identity': b'httpin','url':'tcp://127.0.0.1:5555'},
'HTTPOUT': {'identity': b'httpout','url': 'tcp://127.0.0.1:5556'},
'DATABASE': {'identity': b'database','url': 'tcp://127.0.0.1:5557'},
'SYSTEM': {'identity': b'system','url': 'tcp://127.0.0.1:5558'},
'INTERFACE': {'identity': b'interface','url': 'tcp://127.0.0.1:5559'},
'API_MAINTENANCE': {'identity': b'api_maintenance','url': 'tcp://127.0.0.1:6000'},
}

data_linux ={
'HTTPIN': {'identity': b'httpin','url':'ipc://httpin.ipc'},
'HTTPOUT': {'identity': b'httpout','url': 'ipc://httpout.ipc'},
'DATABASE': {'identity': b'database','url': 'ipc://database.ipc'},
'SYSTEM': {'identity': b'system','url': 'ipc://system.ipc'},
'INTERFACE': {'identity': b'interface','url': 'ipc://interface.ipc'},
'API_MAINTENANCE': {'identity': b'api_maintenance','url': 'ipc://api_maintenance.ipc'},
}

data = {}

if os.name == 'nt':
    data=data_windows
else:
    data=data_linux
