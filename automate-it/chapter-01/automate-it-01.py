import requests
r =requests.get('http://twitter.com/NASA')
print('Response object:', r)
print('Response Text:', r.text)
