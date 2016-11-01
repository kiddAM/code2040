# step 2, reversed string
# program receives string from one API endpoint, 
# returns reversed string to another endpoint

import requests

url = 'http://challenge.code2040.org/api/reverse'
url_val = 'http://challenge.code2040.org/api/reverse/validate'
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"

r = requests.post(url, data={'token': token})
str_ori = r.text
print(str_ori)

str_rev = str_ori[::-1]
print(str_rev)

r_val = requests.post(url_val, data={'token': token, 'string': str_rev})
print(r_val.text)