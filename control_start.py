from multiprocessing import Process
import json

from structure import structure_control
from structure import configuration_shell

from CONTROL import ctrl



def main():

    Process(target=ctrl.main, name = 'CONTROL', args=(configuration_shell.data,)).start()



if __name__ == '__main__':
    main()
