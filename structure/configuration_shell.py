
data_windows = {
'HTTPIN': {'identity': b'httpin','url':'tcp://127.0.0.1:5555'},
'HTTPOUT': {'identity': b'httpout','url': 'tcp://127.0.0.1:5558'},
'DATABASE': {'identity': b'database','url': 'tcp://127.0.0.1:5556'},
'SYSTEM': {'identity': b'system','url': 'tcp://127.0.0.1:6000'},
'INTERFACE': {'identity': b'interface','url': 'tcp://127.0.0.1:5557'},
'API_MAINTENANCE': {'identity': b'api_maintenance','url': 'tcp://127.0.0.1:5559'},

}

data_unix = {
'client': {'identity': b'client','url':'ipc://client.ipc'},
'database': {'identity': b'database','url': 'ipc://database.ipc'},
'io_asset': {'identity': b'io_asset','url': 'ipc://io_asset.ipc'},
'communication': {'identity': b'communication','url': 'ipc://communication.ipc'},
'remote_maintenance': {'identity': b'remote_maintenance','url': 'ipc://remote_maintenance.ipc'},
'worker': {'identity': b'worker','url': 'ipc://worker.ipc'}
}

data=data_windows
