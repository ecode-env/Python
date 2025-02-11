import requests

TOKEN = "srgbntrjghftdgswtrjkjthysa"

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME =  "eyob"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"

}
header = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs", json=graph_config, headers=header)
#
#
# print(response.text)

pixel_config = {
    "date": "20250211",
    "quantity": "10",
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=header)

print(response.text)