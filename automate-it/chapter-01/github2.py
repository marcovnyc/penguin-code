import requests
payload = {'key1': 'value1'} 
r = requests.post('http://httpbin.org/post', data=payload)
print("Request URL:", r.rjson())
