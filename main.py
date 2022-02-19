import math
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

graph_config = {
    'id': "productivity",
    "name": "work hours",
    "unit": "hour",
    "type": "int",
    "color": "ajisai",
}

RESCUE_TIME_KEY = "B63ekrFHgsgvdPxReuffJaQwu4TBD0KrS2UrVWsg"
RESCUE_TIME_ENDPOINT = "https://www.rescuetime.com/anapi/daily_summary_feed"

rescue_time_params = {
    "key": RESCUE_TIME_KEY,
}

response = requests.get(url=RESCUE_TIME_ENDPOINT, params=rescue_time_params)
data = response.json()[0]

date = data["date"]
date = date.replace("-", "")
productive_hours = math.ceil(data["all_productive_hours"])

print(f"{date}: {productive_hours}")


post_pixel_config = {
    "date": date,
    "quantity": f"{productive_hours}",
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
update_pixel_endpoint = f"{post_pixel_endpoint}/{today}"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=post_pixel_endpoint, headers=headers, json=post_pixel_config)
print(response.text)
