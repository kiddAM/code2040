# step 4, prefix
# program receives prefix (string) and array of strings from one API endpoint
# returns new array of all strings not beginning with the prefix to alternate endpoint

import requests
import json

url = 'http://challenge.code2040.org/api/prefix'
url_val = 'http://challenge.code2040.org/api/prefix/validate'
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"

r = requests.post(url, data={'token': token})
print(r.text)

json_dict = r.json()
prefix = json_dict["prefix"]
arr = json_dict["array"]

new_arr = []

for s in arr:
	if s.find(prefix) != 0:
		new_arr.append(s)

print(new_arr)

dict = {}
dict['token'] = token
dict['array'] = new_arr

r_val = requests.post(url_val, json = dict)
print(r_val.text)