#wrong program

def letterCombinations(A):
	B = list(A)
	C = []
	D = []
	mapping = [['0'], ['1'], ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]
	for i in B:
		C.append(int(i))
	D = transform("",len(A),mapping,C,D)
	print D
        
def transform(string,length,mapping,C,D):
	if(len(string)==length):
		D.append(string)
		return
	for i in C:
		for j in mapping[i]:
			string += j
			print string
			#mapping[i].remove(j)
			ind = C.index(i)
			C.remove(i)
			transform(string,length,mapping,C,D)
			string = string[0:len(string)-1]
			C.append(i)
			temp = C[-1]
			for x in range(len(C)-2,-1,-1):
				C[x+1] = C[x]
			C[0] = temp
	return D[0:len(D)/2]
			
letterCombinations("231")