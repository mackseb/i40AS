from multiprocessing import Process
import json


from structure import structure_module
from structure import configuration_shell


from database import shell_database
from io_asset import shell_io_asset



def main(database = True, io_asset = True):


    if database:
        Process(target=shell_database.main, name = 'shell_database', args=('database', configuration_shell.data,)).start()

    if io_asset:
        Process(target=shell_io_asset.main, name = 'shell_io_asset', args=('io_asset', configuration_shell.data,)).start()



if __name__ == '__main__':
    main()
