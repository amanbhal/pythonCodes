# @param A : tuple of integers
# @return an integer
def singleNumber(A):
	bits = [0]*32
	for i in A:
		C = list(bin(i))
		C = C[2:]
		C = C[::-1]
		print C
		index = 0
		for i in C:
			#print i,bits[index]
			bits[index] = bits[index]^int(i)
			index += 1
	
	bits = bits[::-1]
	print bits
	result = ""
	for i in bits:
		result += str(i)
	return int(result,2)
	
print singleNumber([1,1,2,2,44,33,44,56,78,56,33])