from multiprocessing import Process
import json


from structure import structure_module
from structure import configuration_shell


from database import shell_database
from io_asset import shell_io_asset
from communication import shell_communication
from functionality import remote_maintenance
from service import shell_worker



def main(database = True, io_asset = True, communication = True, functionality = True, service = True):


    if database:
        Process(target=shell_database.main, name = 'shell_database', args=('database', configuration_shell.data,)).start()


    if io_asset:
        Process(target=shell_io_asset.main, name = 'shell_io_asset', args=('io_asset', configuration_shell.data,)).start()


    if communication:
        Process(target=shell_communication.main, name = 'shell_communication', args=('communication', configuration_shell.data,)).start()


    if functionality:
        Process(target=remote_maintenance.main, name = 'remote_maintenance', args=('remote_maintenance', configuration_shell.data,)).start()


    if service:
        Process(target=shell_worker.main, name = 'shell_worker', args=('worker', configuration_shell.data,)).start()



if __name__ == '__main__':
    main()
