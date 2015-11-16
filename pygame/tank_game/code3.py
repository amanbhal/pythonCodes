matrix = [[1 for x in range(3)] for x in range(3)]
global count
count = 0
def path(matrix):
	#base
	if matrix[0][1]==1:
		path(matrix[1:][1:])

path(matrix)