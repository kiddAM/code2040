"""
Step 2, Reversed String
program receives string from one API endpoint, 
returns reversed string to another endpoint
"""

import requests

# initial endpoint
url = 'http://challenge.code2040.org/api/reverse'

# validation endpoint
url_val = 'http://challenge.code2040.org/api/reverse/validate'

# API token
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"
data = {'token': token}

# get string from initial endpoint
r = requests.post(url, json=data)
str_ori = r.text
print(str_ori)

# reverse string
str_rev = str_ori[::-1]
print(str_rev)

# send reversed string to validation endpoint
dict = {}
dict['token'] = token
dict['string'] = str_rev

r_val = requests.post(url_val, json=dict)
print(r_val.text)
