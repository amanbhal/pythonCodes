# @param A : list of integers
# @param B : integer
# @param C : integer
# @return an integer

def numRange(A, B, C):
	count = 0
	for i in range(0,len(A)):
		sum = 0
		j = i
		while(j<len(A)):
			sum += A[j]
			if(sum>=B and sum<=C):
				count += 1
			j += 1
	return count

A = [ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ]	
print numRange(A,99,269)