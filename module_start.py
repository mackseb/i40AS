from multiprocessing import Process

from API_MAINTENANCE import remote_maintenance
from DATABASE import info
from HTTPOUT import http_requests
from INTERFACE import asset
from SYSTEM import worker



def main(API_MAINTENANCE=True, DATABASE=True, HTTPOUT=True, INTERFACE=True, SYSTEM=True):

    if API_MAINTENANCE:
        Process(target=remote_maintenance.main,).start()

    if DATABASE:
        Process(target=info.main,).start()

    if HTTPOUT:
        Process(target=http_requests.main,).start()

    if INTERFACE:
        Process(target=asset.main,).start()

    if SYSTEM:
        Process(target=worker.main,).start()



if __name__ == '__main__':
    main()
