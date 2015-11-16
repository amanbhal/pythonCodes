# @param A : list of integers
# @param B : integer
# @return an integer

import math
def threeSumClosest(A, B):
	A = sorted(A)
	#print A
	distance = 1000000
	result = 0
	for i in range(0,len(A)-1):
		j=i+1
		k=len(A)-1
		#print "Step: " + str(i)
		while(j<k and k>i):
			#print A[i], A[j], A[k]
			if(math.fabs((A[i]+A[j]+A[k])-B)<distance):
				#print math.fabs((A[i]+A[j]+A[k])-B)
				distance = math.fabs((A[i]+A[j]+A[k])-B)
				result = A[i]+A[j]+A[k]
				#print result
			if(A[i]+A[j]+A[k]>B):
				#print 'greater'
				k -= 1
			elif(A[i]+A[j]+A[k]<B):
				#print 'smaller'
				j += 1
			elif(A[i]+A[j]+A[k]==B):
		#		print "equal"
				return (A[i]+A[j]+A[k])
	return result	
print threeSumClosest([-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3],-1)