def bubble_sort(arr):
	for i in range(0,len(arr)):
		for j in range(0,len(arr)-1):
			if (arr[j] > arr[j+1]):
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	
	print arr
arr = [1,5,3,8,6,54,2,4,23,532]
bubble_sort(arr)