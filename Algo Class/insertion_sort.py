def insertion_sort(arr):
	for i in range(1,len(arr)):
		value = arr[i]
		hole = i
		while(hole > 0 and arr[hole-1] > value):
			arr[hole] = arr[hole-1]
			hole -= 1
		arr[hole] = value
	print arr

arr = [1,5,3,8,6,54,2,4,23,532]
insertion_sort(arr)