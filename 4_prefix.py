"""
Step 4, Prefix
program receives prefix (string) and array of strings from one 
API endpoint returns new array of all strings not beginning 
with the prefix to alternate endpoint
"""

import requests
import json

# initial endpoint
url = 'http://challenge.code2040.org/api/prefix'

# validation endpoint
url_val = 'http://challenge.code2040.org/api/prefix/validate'

# API token
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"
data = {'token': token}

# get prefix and string array from initial endpoint
r = requests.post(url, json=data)
print(r.text)

json_dict = r.json()
prefix = json_dict["prefix"]
arr = json_dict["array"]

# initialize new string array and for loop to identify strings
# that do not begin with the prefix
new_arr = []
for s in arr:
	if s.find(prefix) != 0:
		new_arr.append(s)

print(new_arr)

# send new array to validation endpoint
dict = {}
dict['token'] = token
dict['array'] = new_arr

r_val = requests.post(url_val, json = dict)
print(r_val.text)
