query = {}
avg_precision = {}
precision = {}
recall = {}
fScore = {}
def main():
	global points
	global avg_precision
	fileO = open("Files/irAnalysis.txt","r")
	fileTxt = fileO.readline()
	while fileTxt:
		fileTxt = fileTxt.strip('\r\n')
		fileTxt = fileTxt.split(" ")
		if fileTxt[0] not in query.keys(): #imp
			query[fileTxt[0]] = []			#imp
		query[fileTxt[0]].append(int(fileTxt[3]))	#imp
		fileTxt = fileO.readline()
	for key in query.keys():
		calculate_p_r_f(key,query[key])
	
	calculate_map()
	for i in range(10):
		print query["302"][i],precision["302"][i]
	print "Average Precision: ",avg_precision["302"],"\n"
	
from pygame import gfxdraw
gfxdraw.pixel(surface, x, y, color)
		
def calculate_p_r_f(query,list):
	global precision
	global recall
	global fScore
	global avg_precision
	total_relevant_count = 0.0
	for i in range(0,len(list)):
		if list[i]==1:
			total_relevant_count += 1	
	
	#calculating precision and recall and fScore
	temp_precision = 0.0
	temp_recall = 0.0
	count = 0
	for i in range(0,10):
		if query not in precision.keys():
			precision[query] = []
			recall[query] = []
			fScore[query] = []
		if list[i]==1:
			count += 1
		temp_precision = count/float(i+1)
		if count!=0:
			temp_recall = count/total_relevant_count
		else:
			temp_recall = 0
		precision[query].append(temp_precision)
		recall[query].append(temp_recall)
		if temp_precision!=0 and temp_recall!=0:
			fScore[query].append((2*temp_precision*temp_recall)/(temp_precision+temp_recall))
		else:
			fScore[query].append(0)
	sum = 0.0
	for i in range(0,10):
		if list[i] == 1:
			sum += precision[query][i]
	if total_relevant_count!=0:
		avg_precision[query] = sum/total_relevant_count
	else:
		avg_precision[query] = 0.0
	#print query, avg_precision[query]
	
def calculate_map():
	total_query = len(query.keys())
	sum = 0.0
	for item in query.keys():
		sum += avg_precision[item]
	map = sum/total_query
	print map,"\n"
		
		
if __name__ == "__main__":
	main()