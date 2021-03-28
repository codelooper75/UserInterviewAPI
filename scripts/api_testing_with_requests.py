import json
import requests
from requests.auth import HTTPBasicAuth

BASE_URL= "http://127.0.0.1:8000/"

ENDPOINT = 'api/polls'

def get_polls():
    r = requests.get(BASE_URL + ENDPOINT, auth=HTTPBasicAuth('roman', '4826'))
    data = r.json()                 #type list
    # json_data = json.dumps(data)    #type 'str'
    print(r.status_code) #200
    for obj in data:
        """Just print obj"""
        print(obj)
        """Print some key"""
        print(obj['title'])

        """request details (not implemented yet)"""
        # r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']), auth=HTTPBasicAuth('roman', '4826'))
        # print(r2.json())

    return data

get_polls()