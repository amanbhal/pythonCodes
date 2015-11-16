					#INFIX COMPUTATION: Enter a string like "1+2-(3/4)*5" and get the result

					
def operation(string):
	#we have to use parser in this function
	if string[1]=='+':
		return str(float(string[0]) + float(string[2]))
	elif string[1]=='-':
		return str(float(string[0]) - float(string[2]))
	elif string[1]=='/':
		return str(float(string[0]) / float(string[2]))
	elif string[1]=='*':
		return str(float(string[0]) * float(string[2]))
	#elif string[1]==".":		#Find a way to handle this situation. One way is to enter the stack one by one i.e by using for loop
	#	result = []
	#	result.append("".join(string))
	#	return str(result[0])
	else:
		return "wrong operator:" + str(string[1])

def parentheses(stack):
	if stack.count('(')==stack.count(')'):
		for i in range(0,len(stack)):
			if stack[i]=='(':
				index = i
			elif stack[i]==')':
				start = index
				stack[start] = operators(stack[start+1:i])
				for x in range(start+1,i+1):
					stack[x] = " "
				break
			else:
				pass
		while stack.count(" ")!=0:
			del stack[stack.index(" ")]
		if stack.count("(")!=0 and stack.count(")")!=0 and stack.count("(")==stack.count(")"):
			stack = parentheses(stack)
		else:
			stack = operators(stack)
	else:
		print "Entered string does not have balanced parantheses"
	return stack

def operators(stack):
	for i in range(0,len(stack)):
		if stack[i] in "+-*/.":
			start = i
			stack[start+1] = operation(stack[start-1:start+2])
			for x in range(start-1,start+1):
				stack[x] = " "
		else:
			pass
	result = stack.pop()
	return result
	
stack = list(raw_input("Enter the string to be calculated\n"))
stack = parentheses(stack)
print "\nResult of the entered string is: ", stack
print "\n"