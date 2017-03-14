from multiprocessing import Process
import json


from structure import structure_module
from structure import configuration_shell


from HTTPOUT import http_requests


def main(HTTPOUT = True):


    if HTTPOUT:
        Process(target=http_requests.main, name = 'HTTPOUT', args=('HTTPOUT', configuration_shell.data,)).start()



if __name__ == '__main__':
    main()
