import requests
payload = {'q': 'aws-labs'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL:", r.content)
