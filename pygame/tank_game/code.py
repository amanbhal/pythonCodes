num = int(raw_input())
bnum = bin(num)
convert = []
for x in bnum[2:]:
	if x=='0':
		convert.append('1')
	else:
		convert.append('0')
print convert
convert = "".join(convert)
result = int(convert,2)
print result