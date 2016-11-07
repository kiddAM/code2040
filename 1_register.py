"""
Step 1, Registration
program posts API token to registration endpoint, 
connects to GitHub repository
"""

import requests

# API endpoint
url = 'http://challenge.code2040.org/api/register'

# API token
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"

# personal GitHub repository
github = "https://github.com/kiddam/code2040"
data = {'token': token, 'github': github}

# send JSON dictionary to endpoint
r = requests.post(url, json=data)
print(r.text)
