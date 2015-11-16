"""Here we've imported the json module for parsing JSON, and we're using the open() method as before to read from 
pets.txt (under the "Files") tab. Reading from this file is just like reading JSON sent by a server. We've also 
imported the pprint function from the pprint module to use "pretty print" functionality that will print the output 
in a formatted way that's easier to read."""

import json
from pprint import pprint

f = open('pets1.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)