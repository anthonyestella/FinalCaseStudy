# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'NDI1NjU3ZmUtNWZhMC00NmFlLTg1MmMtMWViMzJhZGQ0YTYxODUxNmQzNTUtYTky_P0A1_0615a9a8-3f8a-4d33-aff0-1af12656603c'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'anthony10.estella@gmail.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lNzlkOTJkMC0wZDRhLTRhY2MtODE5OS0wNWViMGQyZWNjNzI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
