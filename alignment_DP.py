def alignment(A,B):
	s1 = 2	#match
	s2 = -1	#mis-match
	s3 = -2	#blank
	matrix = [[0 for x in range(len(A)+1)] for y in range(len(B)+1)]
	matrix[0][0] = 0
	for i in range(1,len(A)+1):
		matrix[0][i] = s3
	for i in range(1,len(B)+1):
		matrix[i][0] = s3
	#for i in matrix:
	#	print i
	print "-------------"
	for i in range(1,len(B)+1):
		for j in range(1,len(A)+1):
			if(i==0 or j==0):
				matrix[i][j] = 0
			else:
				if(B[i-1]==A[j-1]):
					matrix[i][j] = max((matrix[i-1][j-1]+s1),(matrix[i-1][j])+s3,(matrix[i][j-1])+s3)
				else:
					matrix[i][j] = max((matrix[i-1][j-1]+s2),(matrix[i-1][j])+s3,(matrix[i][j-1])+s3)
	#backtrace
	backtrace = matrix[len(B)][len(A)]
	i = len(B)
	j = len(A)
	while(i>=0 and j>=0):
		if(B[i-1]==A[j-1]):
			print "match"
			i = i-1
			j = j-1
		elif(backtrace==matrix[i-1][j]+s3):
			print "blank A"
			i = i-1
		elif(backtrace==matrix[i][j-1]+s3):
			print "blank B"
			j = j-1
		else:
			print "mismatch"
			i = i-1
			j = j-1
		backtrace = matrix[i][j]
	for i in matrix:
		print i
	#return matrix[len(A)][len(B)]
A = "GAATTCAGTTA"
B = "GGATCGA"
alignment(A,B)