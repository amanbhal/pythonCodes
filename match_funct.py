				# use this link to read more [http://www.tutorialspoint.com/python/python_reg_expressions.html
						#use this link to read more [https://docs.python.org/2/library/re.html]
import re

string = "hi this is aman"

matchObj = re.match(r'(.*) this .*',string)
print matchObj.group()
print matchObj.group(1)

matchObj1 = re.match(r'.i.{6}(.*)(aman)',string)
print matchObj1.group()
print matchObj1.group(1)
print matchObj1.group(2)

#Characters that are not within a range can be matched by complementing the set. 
#If the first character of the set is '^', all the characters that are not in the set will be matched.
num = "584587412598563"
matchObj2 = re.match(r'[^4][0-9]*',num)
matchObj3 = re.match(r'[^8][0-9]*',num)
if matchObj2!=None and matchObj3!=None:
	print matchObj2.group()
else:
	print "num starts with either 4 or 8"

#(?P<group_name>[expression]) gives a name to the group so that it can be used to reference afterwards
character = "asdfg"
matchObj4 = re.match(r'(?P<grp>[\w]+)',character)
print matchObj4.group('grp')

string = "amansingh"
matchObj5 = re.search(r'(?#comment)(?<=aman)singh',string)
print matchObj5.group()

# re.compile
string = "qwerty6uiop"
obj = re.compile(r'\D+')
print "The string contains only non numeric characters:",obj.search(string).group()

# re.split
string = "0a1f2g4h6jgh5"
print re.split('[a-z]+',string,flags = re.IGNORECASE)

# re.findall
string = "Wow aman! You are really nice person aman. I must say that aman"
print re.findall('aman',string)

# re.sub(pattern, repl, string, count=0, flags=0) substitutes the string match with repl and returns the new string

# re.subn(pattern, repl, string, count=0, flags=0) sustitutes the string with repl and returns new string with the
#no.of substitutions made

# re.error Exception raised when a string passed to one of the functions here is not a valid regular expression
