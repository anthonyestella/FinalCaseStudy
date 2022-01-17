# Fill in this file with the messages code from the Webex Teams exercise
import requests

access_token = 'NDI1NjU3ZmUtNWZhMC00NmFlLTg1MmMtMWViMzJhZGQ0YTYxODUxNmQzNTUtYTky_P0A1_0615a9a8-3f8a-4d33-aff0-1af12656603c'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYjE2ZjQ3MDAtNzc3ZC0xMWVjLTkyYmYtYzllZTdjNGFiODRi'
message = 'GOOD DAY! Welcome to the CASE STUDY ROOM, Marigold! Good luck!!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
