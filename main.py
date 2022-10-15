import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USER_NAME = "necode"
TOKEN = "jsdfiujraoijdfn83749dfj"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Graph",
    "unit": "hours",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()
date = today.strftime("%Y%m%d")

post_params = {
    "date": date,
    "quantity": input("How many hours did you spend learning today? "),
}

post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

# post pixel
# response = requests.post(url=post_endpoint, json=post_params, headers=headers)

put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"

put_params = {
    "date": date,
    "quantity": "2",
}

# update pixel
# response = requests.put(url=put_endpoint, json=put_params, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"

# delete pixel
response = requests.delete(url=delete_endpoint, headers=headers)
