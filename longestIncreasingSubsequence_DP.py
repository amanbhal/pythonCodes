def LIS(a):
	lis = [1]*len(a)
	#bottom-up approach
	for i in range(1,len(a)):
		for j in range(0,i):
			if(a[j]<a[i] and lis[j]+1>lis[i]):
				lis[i] = lis[j]+1
	maximum = 0
	print lis
	for i in lis:
		maximum = max(maximum,i)
	print maximum
				
		
a = [10,22,9,33,21,50,41,60,70,80,90,100,101,102]
LIS(a)
