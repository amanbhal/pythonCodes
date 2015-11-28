def LCS(X,Y):
	L = [[None]*(len(Y)+1)]*(len(X)+1)
	for i in range(len(X)+1):
		for j in range(len(Y)+1):
			if(i==0 or j==0):
				L[i][j] = 0
			elif(X[i-1]==Y[j-1]):
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j],L[i][j-1])
	return L[len(X)][len(Y)]
		


X = "AGGTAB"
Y = "GXTXAYB"
print LCS(X,Y)