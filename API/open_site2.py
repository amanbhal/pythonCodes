#Another way to communicate through HTTP in Python is with the requests library 

import requests

# Make a GET request here and assign the result to kittens:
kittens = requests.get("http://placekitten.com")

print kittens.text[559:1000]