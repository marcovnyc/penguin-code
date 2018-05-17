import requests
payload = {'q': 'chetan'} 
r = requests.get('https://github.com/search', params=payload)
print("Request URL:", r.url)
