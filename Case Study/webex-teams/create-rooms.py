# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests

access_token = 'NDI1NjU3ZmUtNWZhMC00NmFlLTg1MmMtMWViMzJhZGQ0YTYxODUxNmQzNTUtYTky_P0A1_0615a9a8-3f8a-4d33-aff0-1af12656603c'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'CTEST'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
