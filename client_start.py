from multiprocessing import Process

from structure import configuration_shell, structure_client

from client import shell_client_database
from client import shell_client_io_asset



def main(client_database = True, client_io_asset = False):


    if client_database:
        Process(target=shell_client_database.main, name = 'shell_client_database', args=(configuration_shell.data,)).start()


    if client_io_asset:
        Process(target=shell_client_io_asset.main, name = 'shell_client_io_asset', args=(configuration_shell.data,)).start()


if __name__ == '__main__':
    main()
