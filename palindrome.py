def palindrome(string):
	left = 0
	right = len(string)-1
	while left<right:
		if string[left]==string[right]:
			left += 1
			right -=1
		else:
			return False
	else:
		return True
string = raw_input("Enter a string..")
print string[-2] #prints second character from last
print palindrome(string)