import types
import re

file = open("IR.txt","r")
find = "316-320"
for line in file.readlines():
	line = line.strip("\n\r")
	print line
	result = re.search(find,line)
	if result!=None:
		print "exist"