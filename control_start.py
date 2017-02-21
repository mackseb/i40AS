from multiprocessing import Process
import json

from structure import structure_control
from structure import configuration_shell

from control import shell_control



def main():

    Process(target=shell_control.main, name = 'shell_control', args=(configuration_shell.data,)).start()



if __name__ == '__main__':
    main()
