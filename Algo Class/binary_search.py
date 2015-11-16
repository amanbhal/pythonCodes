def binary_search(arr,start,end,searchItem):
	if (start <= end):
		middle = (start+end)//2
		if (searchItem == arr[middle]):
			print "Found at: " + str(middle)
		elif (searchItem > arr[middle]):
			binary_search(arr,middle+1,end,searchItem)
		elif (searchItem < arr[middle]):
			binary_search(arr,start,middle-1,searchItem)

arr = [1,4,7,8,5,88,45,75,36,874,67,32,78,31]
arr.sort()
print "\n"
print arr
print "\n"
binary_search(arr,0,len(arr)-1,7)