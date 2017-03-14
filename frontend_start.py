from multiprocessing import Process
import json


from structure import module
from structure import config


from HTTPOUT import http_requests


def main(HTTPOUT = True):


    if HTTPOUT:
        Process(target=http_requests.main, name = 'HTTPOUT', args=('HTTPOUT', config.data,)).start()



if __name__ == '__main__':
    main()
