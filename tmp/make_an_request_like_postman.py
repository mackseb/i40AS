import requests
import json

url = "http://localhost:5000/test"
bla = {"213":"atkjt"}
payload = json.dumps(bla)
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "8f9c7937-15ad-149a-882e-11e58f31d445"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
