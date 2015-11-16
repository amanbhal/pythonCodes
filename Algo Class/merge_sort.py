def merge_sort(arr):
	if len(arr) < 2:
		return
	middle = len(arr)/2
	left = arr[0:middle]
	right = arr[middle:len(arr)]
	merge_sort(left)
	merge_sort(right)
	merge(arr,left,right)
	
def merge(arr,left,right):
	i = 0
	j = 0
	k = 0
	while(i < len(left) and j < len(right)):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while(i < len(left)):
		arr[k] = left[i]
		i += 1
		k += 1
	while(j < len(right)):
		arr[k] = right[j]
		j += 1
		k += 1
	
arr = [1,5,3,8,6,54,2,4,23,532]
print arr
merge_sort(arr)
print arr