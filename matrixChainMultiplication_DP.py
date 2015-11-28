import sys
def matrixChainMultiplication(sequence):
	n = len(sequence)
	sol = [[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		sol[i][i] = 0
	for L in range(2,n):
		for i in range(1,n-L+1):
			j = i+L-1
			sol[i][j] = sys.maxint
			for k in range(i,j):
				q = sol[i][k] + sol[k+1][j] + sequence[i-1]*sequence[k]*sequence[j]
				if q < sol[i][j]:
					sol[i][j] = q
	return sol[1][n-1]

sequence = [1,2,3,4]
print matrixChainMultiplication(sequence)