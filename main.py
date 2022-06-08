import requests
from datetime import datetime
import os

USERNAME_API = os.environ.get("USERNAME")
TOKEN_API = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN_API,
    "username": USERNAME_API,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME_API}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Time On Computer",
    "unit": "minutes",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN_API
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME_API}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "680",
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME_API}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "32323243"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME_API}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
