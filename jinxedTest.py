import requests
import json

url = "https://jinxed.cf"

payload = {
  "url": "https://youtube.com",
  "alias": input(), 
  "max-clicks": 100, 
  "password": ""
}

headers = {
  "Accept": "application/json"
}

response = requests.post(url, data=payload, headers=headers)
print(json.loads(response.text))