import requests
payload = {'q': 'marcovnyc'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL:", r.response)
