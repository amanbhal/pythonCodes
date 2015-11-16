#get the status code of a request
import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
print response.status_code