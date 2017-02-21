import json
import urllib.parse
import requests

from structure import structure_module



def main(name, info):

    shell_communication = structure_module.entity(name, info)


    while True:
        try:

            MESSAGE = shell_communication.receive()
            CORE_pyobj = shell_communication.extract_core(MESSAGE)


            request = CORE_pyobj["request"]
            main_api = request['main_api']
            address = request["address"]
            url = main_api + urllib.parse.urlencode({'address':address})
            response = requests.get(url).json()
            print(response)


            MESSAGE = shell_communication.create_message(CORE_pyobj = response, MESSAGE_received = MESSAGE )
            shell_communication.send(MESSAGE)


        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()
