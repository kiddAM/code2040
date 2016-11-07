"""
Step 5, The Dating Game
program receives iso1806 datestamp and interval in seconds from one
API endpoint, uses datetime module to add interval to the datestamp,
and returns updated timestamp to alternate endpoint
"""

import requests
import datetime
import iso8601

# initial endpoint
url = 'http://challenge.code2040.org/api/dating'

# validation endpoint
url_val = 'http://challenge.code2040.org/api/dating/validate'

# API token
token = "2e604fae731b1c9d71d84d9e0a9f9c2e"
data = {'token': token}

# get datestamp and interval from initial endpoint
r = requests.post(url, json=data)
print(r.text)

json_dict = r.json()
date_ori = json_dict["datestamp"]
interval = json_dict["interval"]
print(date_ori)
print(interval)

# format original datestamp string as readable datetime object 
date_stamp = datetime.datetime.strptime(date_ori,\
	'%Y-%m-%dT%H:%M:%SZ')
print(date_stamp)

# add interval to original datestamp
add_int = datetime.timedelta(seconds = interval)
print(add_int)
date_stamp += add_int

# format new string as iso1806 datestamp
date_new = datetime.date.strftime(date_stamp,\
	'%Y-%m-%dT%H:%M:%SZ')
print(date_new)

# send new datestamp to validation endpoint
dict = {}
dict['token'] = token
dict['datestamp'] = date_new

r_val = requests.post(url_val, json=dict)
print(r_val.text)
