
data_windows = {
'client': {'identity': b'client','url':'tcp://127.0.0.1:5555'},
'database': {'identity': b'database','url': 'tcp://127.0.0.1:5556'},
'io_asset': {'identity': b'io_asset','url': 'tcp://127.0.0.1:5557'},
'communication': {'identity': b'communication','url': 'tcp://127.0.0.1:5558'},
'remote_maintenance': {'identity': b'remote_maintenance','url': 'tcp://127.0.0.1:5559'},
'worker': {'identity': b'worker','url': 'tcp://127.0.0.1:6000'}
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
