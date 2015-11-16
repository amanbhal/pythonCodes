def palindrome(name):
	list1 = []
	for i in range(0,len(name)):
		list1.append("|")
		list1.append(name[i])
	list1.append("|")
	length = len(list1)
	
	long_substring = []
	for key in range(0,length):
		if list1[key]=="|":
			left = key-1
			right = key+1
		else:
			left = key
			right = key
		count = 0
		while left>=0 and right<length and list1[left]==list1[right]:
			left -= 2
			right += 2
			count += 1
		long_substring.append(count)
	
	centre = max(long_substring)
	index = long_substring.index(centre)
	
	answer = list1[index-2*centre+1:index+2*centre]
	answer = "".join(answer)
	answer = answer.split("|")
	answer = "".join(answer)
	print answer
	

name = raw_input("Enter the string to be tested\n")
palindrome(name)