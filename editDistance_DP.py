def editDistance(A,B):
	matrix = [[0 for i in range(len(A)+1)] for i in range(len(B)+1)]
	for i in range(len(B)+1):
		for j in range(len(A)+1):
			if i==0:
				matrix[i][j] = j
			elif j==0:
				matrix[i][j] = i
			elif B[i-1]==A[j-1]:
				matrix[i][j] = matrix[i-1][j-1]
			else:
				matrix[i][j] = 1 + min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
	for i in matrix:
		print i

A = "geek"
B = "gesek"
editDistance(A,B)