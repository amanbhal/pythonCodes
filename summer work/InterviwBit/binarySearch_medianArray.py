def findMedianSortedArrays(A, B):
	if len(A)==0:
		if(len(B)%2 == 0):
			return ((B[len(B)/2]+B[len(B)/2-1]))
		else:
			return (B[len(B)/2])
	if len(B)==0:
		if(len(A)%2 == 0):
			return ((A[len(A)/2]+A[len(A)/2-1]))
		else:
			return (A[len(A)/2])
			
	first = (len(A)+len(B))/2
	if((len(A)+len(B))%2 == 0):
		median1 = 0
		median2 = 0
		flag1 = 1
	else:
		median1 = 0
		flag1 = 0
	
	flag2 = 0
	count = 0
	first_pointer = 0
	second_pointer = 0
	
	while(first_pointer<len(A) and second_pointer<len(B) and count<first):
		if(A[first_pointer] == B[second_pointer]):
			first_pointer += 1
			second_pointer += 1
			count += 2
		elif(A[first_pointer] < B[second_pointer]):
			first_pointer += 1
			flag2 = 0
			count += 1
		else:
			second_pointer += 1
			flag2 = 1
			count += 1
	
	while(first_pointer < len(A) and count<first):
		first_pointer += 1
		flag2 = 0
		count += 1
		
	while(second_pointer < len(B) and count<first):
		second_pointer += 1
		flag2 = 1
		count += 1
		
	if(flag1==1):
		if(flag2 == 0):	
				median1 = A[first_pointer-1]
		else:
				median1 = B[second_pointer-1]
	else:
		if(flag2 == 0):	
				median1 = A[first_pointer]
		else:
				median1 = B[second_pointer]
	print "median1: ", str(median1)
	if(flag1 == 0):
		return median1
	else:
		if(first_pointer<len(A) and second_pointer<len(B)):
			if(A[first_pointer] < B[second_pointer]):
				median2 = A[first_pointer]
			else:
				median2 = B[second_pointer]
		if(first_pointer>len(A)):
			median2 = B[second_pointer]
		if(second_pointer>len(B)):
			median2 = A[first_pointer]
		print "median2: ", str(median2)
		return (median1+median2)/2.0
		
A = [-50,-41,-40,-19,5,21,28,100]
B = [-50,-21,-10]
print findMedianSortedArrays(A,B)