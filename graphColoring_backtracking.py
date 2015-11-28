def graphColoring(graph,m,v,color):
	if(v==len(graph)):
		print color
		return True
	for c in range(1,m+1):
		if(isSafe(graph,color,c,v)):
			color[v]=c
			if(graphColoring(graph,m,v+1,color)==True):
				return True
			#backtracking
			color[v] = 0
	return False

def isSafe(graph,color,c,v):
	for i in range(v):
		if(graph[v][i]==1 and color[i]==c):
			return False
	return True
	
graph = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
color = [0]*len(graph)		#colors are 1,2,3,4,.....,m
m = 4
v = 0
print graphColoring(graph,m,v,color)