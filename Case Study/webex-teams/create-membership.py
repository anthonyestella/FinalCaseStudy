# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests

access_token = 'NDI1NjU3ZmUtNWZhMC00NmFlLTg1MmMtMWViMzJhZGQ0YTYxODUxNmQzNTUtYTky_P0A1_0615a9a8-3f8a-4d33-aff0-1af12656603c'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYjE2ZjQ3MDAtNzc3ZC0xMWVjLTkyYmYtYzllZTdjNGFiODRi'
person_email = 'marigold.ditan@gmail.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
