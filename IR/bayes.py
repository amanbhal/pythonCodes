import re
import math
from operator import itemgetter

points = []
grid_points = []
def main():
	global points
	global grid_points
	fileO = open("Files/output (4).txt", "r")
	fileTxt = fileO.readline()
	c1 = 0
	c2 = 0
	while(fileTxt):
		matchObj1 = re.search(r'\W([-]?\d*)\W',fileTxt)
		matchObj2 = re.search(r'\W([-]?\d*)\W\W',fileTxt)
		matchObj3 = re.search(r'C(\d)',fileTxt)
		if matchObj3!=None:
			points.append([matchObj1.group(1), matchObj2.group(1), matchObj3.group(1)])
			if matchObj3.group(1)=='1':
				c1 += 1
			else:
				c2 += 1
		else:
			points.append([matchObj1.group(1),matchObj2.group(1)])
			
		fileTxt = fileO.readline()
	P1 = c1/(c1+c2)
	P2 = c2/(c1+c2)
	for i in range(0,1000):
		for j in range(0,3):
			points[i][j] = int(points[i][j])
	points[1000][0] = int(points[1000][0])
	points[1000][1] = int(points[1000][1])
	
	temp = sorted(points,key = itemgetter(0))
	x_min = temp[0][0]
	x_max = temp[999][0]
	
	temp = sorted(points,key = itemgetter(1))
	y_min = temp[0][1]
	y_max = temp[999][1]
	
	divisions = 8.0
	x_width = (float((x_max-x_min)/divisions))
	y_width = (float((y_max-y_min)/divisions))
	
	#print x_width, y_width
	x_lower = abs(points[1000][0]/x_width)*x_width
	y_lower = abs(points[1000][1]/y_width)*y_width
	x_upper = x_lower + x_width
	y_upper = y_lower + y_width
	#print x_lower, y_lower, x_upper, y_upper
	
	for i in range(0,1000):
		if(points[i][0]>=x_lower and points[i][0]<=x_upper and points[i][1]>=y_lower and points[i][1]<=y_upper):
			grid_points.append(points[i])
	
	grid_count1 = 0
	grid_count2 = 0
	for point in grid_points:
		#print point
		if point[2]==1:
			grid_count1 += 1
		else:
			grid_count2 += 1
	p1 = grid_count1/c1
	p2 = grid_count2/c2
			
	if P1*p1>P2*p2:
		print "Point lines in cluster 1"
	else:
		print "Point lines in cluster 2"
	
	
	
if __name__ == "__main__":
	main()