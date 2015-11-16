import re
import math

points = []
means = []
new_means = [[0,0],[0,0],[0,0]]

def main():
	global means
	global new_means
	global points
	fileO = open("Files/k-means.txt", "r")
	fileTxt = fileO.readline()
	while(fileTxt):
		fileTxt = fileTxt.strip('\r\n')
		matchObj = re.findall('\s\d*\s',fileTxt)
		matchObj[0] = int(matchObj[0])
		matchObj[1] = int(matchObj[1])
		xy_list = [matchObj[0],matchObj[1],0]
		points.append(xy_list)
		fileTxt = fileO.readline()
	means.append([points[0][0],points[0][1]])
	means.append([points[1][0],points[1][1]])
	means.append([points[2][0],points[2][1]])
	
	while(1):
		sumx1=0
		sumy1=0
		sumx2=0
		sumy2=0
		sumx3=0
		sumy3=0
		count1=0
		count2=0
		count3 = 0
		for xy in points:
			dist1 = euclidean_dist(xy[0],xy[1],means[0][0],means[0][1])
			dist2 = euclidean_dist(xy[0],xy[1],means[1][0],means[1][1])
			dist3 = euclidean_dist(xy[0],xy[1],means[2][0],means[2][1])
			xy[2] = mini(dist1,dist2,dist3)
			if xy[2] == 1:
				sumx1 += xy[0]
				sumy1 += xy[1]
				count1 += 1
			elif xy[2] == 2:
				sumx2 += xy[0]
				sumy2 += xy[1]
				count2 += 1
			else:
				sumx3 += xy[0]
				sumy3 += xy[1]
				count3 += 1
		new_means[0][0] = sumx1/count1
		new_means[0][1] = sumy1/count1
		new_means[1][0] = sumx2/count2
		new_means[1][1] = sumy2/count2
		new_means[2][0] = sumx3/count3
		new_means[2][1] = sumy3/count3
		if(new_means==means):
			break
		else:
			means=new_means
	print means
	
def mini(x,y,z):
	if x<y and x<z:
		return 1
	elif y<x and y<z:
		return 2
	else:
		return 3
			
def euclidean_dist(x,y,xm,ym):
	#print math.sqrt((x-xm)**2 + (y-ym)**2)
	return math.sqrt((x-xm)**2 + (y-ym)**2)
	
if __name__ == "__main__":
	main()