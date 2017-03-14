from multiprocessing import Process

from structure import config
from DATABASE import info
from INTERFACE import asset
from API_MAINTENANCE import remote_maintenance
from SYSTEM import worker



def main(DATABASE=True, SYSTEM=True, INTERFACE=True, API_MAINTENANCE=True):


    if DATABASE:
        Process(target=info.main, name = 'DATABASE', args=('DATABASE', config.data,)).start()


    if SYSTEM:
        Process(target=worker.main, name = 'SYSTEM', args=('SYSTEM', config.data,)).start()


    if INTERFACE:
        Process(target=asset.main, name = 'INTERFACE', args=('INTERFACE', config.data,)).start()


    if API_MAINTENANCE:
        Process(target=remote_maintenance.main, name = 'API_MAINTENANCE', args=('API_MAINTENANCE', config.data,)).start()






if __name__ == '__main__':
    main()
