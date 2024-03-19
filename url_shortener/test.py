import requests

url = "http://127.0.0.1:5000/create"

# Replace these with your actual values
payload = {
    "url": "https://example.com",
}

# Necessary to get a non-html response
headers = {
    "Accept": "application/json"
}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    # If the request was successful, print the shortened URL
    shortened_url = response.text
    print(f"http://localhost:5000/{shortened_url}")
else:
    # If the request failed, print the error message
    print(f"Error: {response.status_code}")