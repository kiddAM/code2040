"""
Step 3, Needle in a Haystack
program receives needle (string) and haystack (array of strings)
from one API endpoint, returns index of needle to alternate 
endpoint
"""

import requests

# initial endpoint
url = 'http://challenge.code2040.org/api/haystack'

# validation endpoint
url_val = 'http://challenge.code2040.org/api/haystack/validate'

# API token
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"
data = {'token': token}

# get needle (str) and haystack (arr) from initial endpoint
r = requests.post(url, json=data)
print(r.text)

json_dict = r.json()
needle = json_dict["needle"]
hstack = json_dict["haystack"]
print("find " + needle + " in:")
print(hstack)

# get index of needle in array
ndl_ind = hstack.index(needle)
print(ndl_ind)

# send index to validation endpoint
dict = {}
dict['token'] = token
dict['needle'] = ndl_ind

r_val = requests.post(url_val, json=dict)
print(r_val.text)
