from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
kittens = urlopen("http://placekitten.com")
response = kittens.read()
body = response[559:1000]

# Add your 'print' statement here!
print body