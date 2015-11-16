def func(A):
	total_row_col = 1+((A-1)*2)
	arr = [0]*total_row_col
	left = 0
	right = total_row_col - 1
	for j in range(0,A):
		arr[left+j] = A-j
		arr[right-j] = A-j
	#print arr
	middle = (left+right)/2
	#print middle
	indexL = middle
	indexR = middle
	
	table = [[i for i in range(0,total_row_col)] for j in range(0,total_row_col)]
	#print table
	
	while(indexL>=0 and indexR<total_row_col):
		for i in range(0,total_row_col):
			table[indexL][i] = arr[indexL]
			table[i][indexL] = arr[indexL]
			table[indexR][i] = arr[indexR]
			table[i][indexR] = arr[indexR]
		indexL -= 1
		indexR += 1
	
	for list in table:
		print list
func(1)