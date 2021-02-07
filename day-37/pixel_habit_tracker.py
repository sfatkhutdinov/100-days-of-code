import requests
from datetime import datetime

USERNAME = 'stan'
TOKEN = 'laskdfhsauefas'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Reading Graph',
    'unit': 'page(s)',
    'type': 'int',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now().strftime('%Y%m%d')
pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
pixel_config = {
    'date': today,
    'quantity': '20'
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f'{pixel_endpoint}/{today}'
update_config = {
    'quantity': '50',
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# Delete pixel
delete_endpoint = f'{pixel_endpoint}/{today}'
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
