# response from a server
import requests
response = requests.get("http://placekitten.com/")

# print the header information from the response
print response.headers