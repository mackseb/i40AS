from multiprocessing import Process

from structure import structure_module
from structure import configuration_shell
from DATABASE import info
from INTERFACE import asset
from API_MAINTENANCE import remote_maintenance
from SYSTEM import worker



def main(DATABASE=True, SYSTEM=True, INTERFACE=True, API_MAINTENANCE=True):


    if DATABASE:
        Process(target=info.main, name = 'DATABASE', args=('DATABASE', configuration_shell.data,)).start()


    if SYSTEM:
        Process(target=worker.main, name = 'SYSTEM', args=('SYSTEM', configuration_shell.data,)).start()


    if INTERFACE:
        Process(target=asset.main, name = 'INTERFACE', args=('INTERFACE', configuration_shell.data,)).start()


    if API_MAINTENANCE:
        Process(target=remote_maintenance.main, name = 'API_MAINTENANCE', args=('API_MAINTENANCE', configuration_shell.data,)).start()






if __name__ == '__main__':
    main()
