def stringPermutation(A,k,n):
	if k==n:
		print A
	else:
		for i in xrange(k,n+1):
			t = A[k]
			A[k] = A[i]
			A[i] = t
			stringPermutation(A,k+1,n)
			t= A[k]	#backtracking
			A[k] = A[i]
			A[i] = t

A = "abc"
A = list(A)
#A = [1,2,3,4]
stringPermutation(A,0,len(A)-1)