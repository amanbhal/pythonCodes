def nextGreater(A):
	stack = []
	B = [-1]*len(A)
	for i in range(0,len(A)):
		removal = False
		if(len(stack)==0 or A[i]<=A[stack[-1]]):
			stack.append(i)
		while(len(stack)!=0 and A[i]>A[stack[-1]]):
			index = stack.pop()
			B[index] = A[i]
			removal = True
		if(removal==True):
			stack.append(i)
	return B	
print nextGreater([ 34, 35, 27, 42, 5, 28, 39, 20, 28])
		