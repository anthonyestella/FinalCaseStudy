# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json

access_token = 'NDI1NjU3ZmUtNWZhMC00NmFlLTg1MmMtMWViMzJhZGQ0YTYxODUxNmQzNTUtYTky_P0A1_0615a9a8-3f8a-4d33-aff0-1af12656603c'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))



