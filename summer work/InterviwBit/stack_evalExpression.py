def evalRPN(A):
	B = []
	for i in A:
		try:
			if(i=='+' or i=='-' or i=='*' or i=='/'):
				a = B.pop()
				b = B.pop()
				if(i=='+'):
					c = int(a) + int(b)
				elif(i=='-'):
					c = int(b) - int(a)
				elif(i=='*'):
					c = int(a) * int(b)
				else:
					c = int(b) / int(a)
				B.append(str(c))
			else:
				B.append(i)
		except IndexError:
			return ''
	return int(B.pop())
	
print evalRPN(['1','2','+','3','*'])