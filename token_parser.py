import re
"""
scanf() Token		Regular Expression
%c						.
%5c						.{5}
%d						[-+]?\d+
%e, %E, %f, %g			[-+]?(|\.\d+)([eE][-+]?\d+)?
%i						[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)
%o						[-+]?[0-7]+
%s						\S+
%u						\d+
%x, %X					[-+]?(0[xX])?[\dA-Fa-f]+

"""

string = raw_input("Enter a string to be parsed:\n")

individual = re.split(' ',string)
print individual

character = []
integer = []
expresion = []
float = []

for x in individual:
	if re.match('\D+',x)!=None:
		character.append(re.match('\D+',x).group())
	elif re.match('(\d+(\.\d*)?)[-+*/](\d+(\.\d*)?)',x)!=None:
		expresion.append(re.match('(\d+(\.\d+)?)[-+*/](\d+(\.\d+)?)',x).group())
	elif re.match('\d+\.\d+',x)!=None:
		float.append(re.match('\d+\.\d+',x).group())
	elif re.match('\d+',x)!=None:
		integer.append(re.match('\d+',x).group())
	else:
		print "Out of Parser list"
		
print "character", character
print "integer", integer
print "float", float
print "expresion", expresion