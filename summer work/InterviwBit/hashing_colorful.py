def colorful(self, A):
	if(A/10==0):
		return True
	x = str(A)
	C = list(x)
   # print C
	D = []
	for i in range(0,len(C)):
		count = i
		num = ""
		while(count<len(C)):
			num += str(C[count])
			D.append(num)
			count += 1
	#print D
	hashmap = dict()
	for i in D:
		E = list(i)
		#print E
		mul = 1
		for i in E:
			mul *= int(i)
		if(mul not in hashmap):
			hashmap[mul] = int(''.join(E))
			#print hashmap
		else:
			return False
	return True
	
print colorful(56676)