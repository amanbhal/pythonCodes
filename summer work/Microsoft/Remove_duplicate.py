def loop_generator(i,size):
	global increment
	j = i+1
	while j < size:
		if increment == True:
			j += 1
			yield j
		else:
			yield j

def remove_duplicate(arr):		#without using extra memory
	global increment
	size = len(arr)
	for i in range(0,size):
		increment = True
		for j in loop_generator(i,size):
			if (arr[j] == arr[i]):
				for k in range(j,size-1):
					arr[k] = arr[k+1]
				size -= 1
				increment = False
	return arr[0:size]
			
def remove_duplicate_item(arr):		#with using extra space
	result = {}
	for i in range(0,len(arr)):
		if (result.get(arr[i])):
			result[arr[i]] += 1
		else:
			result[arr[i]] = 1
	for key in result.keys():
		print key,
		
arr = [1,1,1,1,1,2,5,8,1,1,1,1,1,1,1]
print arr
arr = remove_duplicate(arr)
print arr