def minCostPath(A):
	sol = [[0 for i in range(len(A[0]))] for i in range(len(A))]
	sol[0][0] = A[0][0]
	for i in range(1,len(A)):
		sol[i][0] = sol[i-1][0] + A[i][0]
	for j in range(1,len(A[0])):
		sol[0][j] = sol[0][j-1] + A[0][j]
	for i in range(1,len(A)):
		for j in range(1,len(A[0])):
			sol[i][j] = min(sol[i-1][j-1],sol[i-1][j],sol[i][j-1]) + A[i][j]
	print sol[len(A[0])-1][len(A)-1]
	
A = [[1,2,3],[4,8,2],[1,5,3]]
minCostPath(A)