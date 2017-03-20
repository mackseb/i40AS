import json
import urllib.parse
import requests

from structure.configuration import config
from structure.module import module



def main():

    httpout = module('HTTPOUT', config)


    while True:
        try:

            MESSAGE = httpout.receive()
            CORE_pyobj = httpout.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            main_api = request['main_api']
            address = request["address"]
            url = main_api + urllib.parse.urlencode({'address':address})
            response = requests.get(url).json()
            print(response)


            MESSAGE = httpout.create_message(CORE_pyobj = response, MESSAGE_received = MESSAGE )
            httpout.send(MESSAGE)


        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()
