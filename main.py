import requests

from datetime import datetime

USER_NAME = "wisang"
PIXELA_TOKEN = "faljqjowiflsawpqfas;lfk"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    'id': "productivity",
    "name": "work hours",
    "unit": "hour",
    "type": "int",
    "color": "ajisai",
}

today = datetime.now().strftime("%Y%m%d")

print(today)

post_pixel_config = {
    "date": today,
    "quantity": "3",
}

# update_pixel_config = {
#     "quantity": "4"
# }

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
update_pixel_endpoint = f"{post_pixel_endpoint}/{today}"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config,
#                          headers=headers)
#
# print(response.text)

response = requests.post(url=post_pixel_endpoint, headers=headers, json=post_pixel_config)
print(response.text)

# response = requests.put(url=update_pixel_endpoint, headers=headers, json=update_pixel_config)
# print(response)

# PRODUCTIVITY_GRAPH = "https://pixe.la/v1/users/wisang/graphs/productivity.html"
