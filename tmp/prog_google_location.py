import urllib.parse
import requests
import time
import zmq
import json



def main(json_input):

    main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

    pyobj_input = json_input
    data = pyobj_input
    payload = data["payload"]
    address = payload["address"]

    url = main_api + urllib.parse.urlencode({'address':address})

    json_output = requests.get(url).json()

    return json_output



if __name__ == "__main__":
    print(main( {"payload":{'address':"Darmstadt"}} ))
