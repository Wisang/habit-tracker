from wsgiref import headers

import PRODUCTIVITY as PRODUCTIVITY
import requests

USER_NAME = "wisang"
PIXELA_TOKEN = "faljqjowiflsawpqfas;lfk"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_config = {
    'id': "productivity",
    "name": "work hours",
    "unit": "hour",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config,
                         headers=headers)

print(response.text)

PRODUCTIVITY_GRAPH = "https://pixe.la/v1/users/wisang/graphs/productivity.html"
