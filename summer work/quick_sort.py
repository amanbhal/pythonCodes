import time
def quickSort(A,start,end):
	if start<end:
		pIndex = part(A,start,end)
		quickSort(A,start,pIndex-1)
		quickSort(A,pIndex+1,end)
	
def part(A,start,end):
	pivot = A[end]
	pIndex = start
	for i in range(start,end):
		if A[i]<=pivot:
			temp = A[i]
			A[i] = A[pIndex]
			A[pIndex] = temp
			pIndex += 1
	temp = A[end]
	A[end] = A[pIndex]
	A[pIndex] = temp
	
	return pIndex

A = [9,8,7,6,5,4,3,2,1,0]
quickSort(A,0,len(A)-1)
print A