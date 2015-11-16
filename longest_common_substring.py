def common_substring(string1,string2):
	count = []
	
	for i in range(0,len(string2)):
		value = 0
		for j in range(i+1,len(string2)+1):
			search = string2[i:j]
			if search in string1:
				value = j-i
			else:
				break
		count.append(value)
	
	maximum = max(count)
	index = count.index(maximum)
	
	print string2[index:index+maximum]

string1 = raw_input("Enter the longer string\n")
string2 = raw_input("Enter the shorter string\n")

common_substring(string1,string2)