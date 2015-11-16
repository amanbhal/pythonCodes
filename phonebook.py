import re
text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
# The entries are separated by one or more newlines. Now we convert the string into a list with each nonempty line 
#having its own entry:
entries = re.split("\n+", text)

# The :? pattern matches the colon after the last name, so that it does not occur in the result list. With a maxsplit 
#of 4
for entry in entries:
	print re.split(":? ", entry, 4)