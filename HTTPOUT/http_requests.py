import json
import urllib.parse
import requests

from structure import module



def main(name, info):

    httpout_module = module.entity(name, info)


    while True:
        try:

            MESSAGE = httpout_module.receive()
            CORE_pyobj = httpout_module.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            main_api = request['main_api']
            address = request["address"]
            url = main_api + urllib.parse.urlencode({'address':address})
            response = requests.get(url).json()
            print(response)


            MESSAGE = httpout_module.create_message(CORE_pyobj = response, MESSAGE_received = MESSAGE )
            httpout_module.send(MESSAGE)


        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()
