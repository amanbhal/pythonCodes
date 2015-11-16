import math

points = []
dist_matrix = []
cluster = []
def main():
	global points
	global dist_matrix
	global cluster
	no_of_points = int(raw_input("Enter the number of points: "))
	for i in range(no_of_points):
		points.append([float(raw_input("x"+str(i)+": ")),float(raw_input("y"+str(i)+": "))])
	
	for i in range(no_of_points):
		cluster.append([i+1])
	
	
	while(len(cluster)>3):	#because at the end we have to find 3 clusters
		#make distance matrix
		dist_matrix = []
		for i in range(len(cluster)):
			dist_matrix.append([])
			for j in range(0,i+1):
				if i==j:
					dist_matrix[i].append(0)
				else:
					dist_matrix[i].append(findDistanceBetweenPoints(cluster[i],cluster[j]))
		for i in range(len(cluster)):
			print dist_matrix[i]
		
		closest_point = min_of_2D_array (dist_matrix)
		new_cluster = cluster[closest_point[0]] + cluster[closest_point[1]]
        cluster.append(new_cluster)
        print "New Cluster : ",new_cluster
#       new_point = centroid (p, new_cluster)
        cluster.remove(cluster[closest_point[0]])       
        cluster.remove(cluster[closest_point[1]])       
        print cluster   

        print "Iteration completed\n"

def findDistanceBetweenPoints(c1,c2):
	minimum = 1000
	for i in c1:
		for j in c2:
			dist =  float ( math.sqrt( pow((points[i-1][0]-points[j-1][0]), 2) + pow((points[i-1][1]-points[j-1][1]), 2) ) )
			if minimum > dist:
                              minimum = dist
	return round(minimum,4)
	
def min_of_2D_array(dist):
	a = 0
	b = 0
	minimum = 100.0
	for i in range(len(dist_matrix)):
		for j in range(i):
			if minimum > dist_matrix[i][j]:
				minimum = dist_matrix[i][j]
				a = i
				b = j
	return [a,b]
	
	
if __name__ == "__main__":
	main()