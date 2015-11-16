def largestRectangleArea(A):
	area = 0
	for i in range(0,len(A)):
		x = 0
		j = 0
		while(j<len(A)):
			if(j<i):
				if(A[j]<A[i]):
					x = 0
				else:
					x += A[i]
				j += 1
			else:
				if(A[j]<A[i]):
					break
				else:
					x += A[i]
					j += 1
		if(x>area):
			area = x
	return area

print largestRectangleArea([ 6, 2, 5, 4, 5, 1, 6 ])	