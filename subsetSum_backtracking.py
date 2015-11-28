def subsetSum(a,start,sum,sol,tempSum):
	"""if tempSum==sum:
		for i in sol:
			print a[i],
		print ""
		return True"""
	for i in range(start,len(a)):
		#print start,a[start],sol,tempSum
		if(tempSum+a[i]<sum):
			sol.append(i)
			tempSum += a[i]
			if subsetSum(a,start+1,sum,sol,tempSum)==True:
				return True
			#print "backtrack"
			sol.pop()
			tempSum -= a[i]
		if(tempSum+a[i]==sum):
			for j in sol:
				print a[j],
			print a[i]
			if(subsetSum(a,start+1,sum,sol,tempSum)==True):
				return True
	return False
		
a = [10,7,5,18,12,20,15]
sum = 35
sol = []
tempSum = 0
start = 0
subsetSum(a,start,sum,sol,tempSum)