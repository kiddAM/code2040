# step 1, registration
# program posts API token to registration endpoint, connects to github repository

import requests

url = 'http://challenge.code2040.org/api/register'
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"; github = "https://github.com/kiddam/code2040"

r = requests.post(url, data={'token': token, 'github': github})
print(r.text)