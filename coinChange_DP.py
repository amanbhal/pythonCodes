def coinChange(A,count):
	sol = [0 for x in range(count+1)]
	for cents in range(count+1):		#
		coinCount = cents
		for i in [c for c in A if c<=cents]:
			if coinCount > sol[cents-i]+1:
				coinCount = sol[cents-i]+1
		sol[cents] = coinCount
	print sol[count]
coinChange([1,5,10,21,25],63)