import re
from string import Template


cart = []
cart.append(dict(item="coke",price=8,qty=4))
cart.append(dict(item="cake",price=12,qty=3))
cart.append(dict(item="fish",price=4,qty=6))

t = Template("$qty x $item = $price")
total = 0
print "Cart:"

for data in cart:
	print t.substitute(data)
	total += data["price"]
print "Total:",total
string = 'aman gaurav seema dilbag'
print Template("$name is present").substitute({'name': re.search('aman',string).group()})