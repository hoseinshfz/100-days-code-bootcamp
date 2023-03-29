import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "***"
USERNAME = "***"
GRAPH_ID = "graph1"
UNIT = "hour"
NAME = "my_project"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id": GRAPH_ID,
    "name": NAME,
    "unit": UNIT,
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# creating graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

record_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

# today
date = datetime.today().strftime("%Y%m%d")

# custom date
# date = datetime(year=2023, month=3, day=26).strftime("%Y%m%d")

record_param = {
    "date": date,
    "quantity": input(f"how many {UNIT}s did you spend on the {NAME}? "),
}

record_res = requests.post(url=record_endpoint, json=record_param, headers=headers)
print(record_res.text)

change_pixel_endpoint = f'{record_endpoint}/{date}'
change_param = {
    "quantity": "3.0"
}

# updating a pixel's value
# response = requests.put(url=change_pixel_endpoint, json=change_param, headers=headers)
# print(response.text)

# deleting a pixel
# response = requests.delete(url=change_pixel_endpoint, headers=headers)
# print(response.text)
