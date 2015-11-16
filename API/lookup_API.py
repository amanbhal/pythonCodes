#lookup API

# Try running the program. You should see information about the user in the response.
#The format in the response are always in JavaScript Object Notation (JSON).

import urllib, urllib2, json

url     = 'https://stage.wepayapi.com/v2/user'
headers = {
           'Content-Type': 'application/json',
           'User-Agent': 'Codecademy WePay Demo',
           'Authorization': 'Bearer STAGE_df1684a1c7b91f0de51b72e5890891b92d34e47fb3cb48d4dbd8d2a89fa253cc'
          }
params  = {} # any parameters needed for the API call
request = urllib2.Request(url, json.dumps(params), headers)

try:
	response = urllib2.urlopen(request, timeout=30).read()
	print json.loads(response)
except urllib2.HTTPError as e:
	print e