def sqrt1(A):
	if A==2 or A==1:
		return 1
	arr = [0]*(A+2)
	for i in range(0,A+2):
		arr[i] = i*i
	start = 0
	end = len(arr)-1
	while(start+1<end):
		mid = start + (end+start)/2
		if(arr[mid]==A):
			return mid
		if(arr[mid]>A):
			end = mid
		elif(arr[mid]<A):
			start = mid
	return start
			
def sqrt2(A):
	if A == 1:
		return 1
	low = 0
	high = A/2 + 1
	while low+1<high:
		mid=low+(high-low)/2
		square=mid**2
		if square==A:
			return mid
		elif square<A:
			low=mid
		else:
			high=mid
	return low

print sqrt2(5)