# step 3, needle in a haystack
# progrm receives needle (string) and haystack (array of strings) from
# one API endpoint, returns index of needle to alternate endpoint

import requests

url = 'http://challenge.code2040.org/api/haystack'
url_val = 'http://challenge.code2040.org/api/haystack/validate'
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"

r = requests.post(url, data={'token': token})
#print(r.text)

json_dict = r.json()
needle = json_dict["needle"]
hstack = json_dict["haystack"]

print("find " + needle + " in:")
print(hstack)

ndl_ind = hstack.index(needle)
print(ndl_ind)

r_val = requests.post(url_val, data={'token': token, 'needle': ndl_ind})
print(r_val.text)
