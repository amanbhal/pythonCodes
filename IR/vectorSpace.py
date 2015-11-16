import os

def main():
	global stopList
	stopList = makeStopList()
	global fileList
	fileList = makeFileList()
	makeTdMatrix(stopList,fileList)
	vectorSearch()
	
	
def makeStopList():
	fileO = open("StopWord.txt", "r")
	fileTxt = fileO.read()
	stopList = fileTxt.split()
	return stopList
	
def makeFileList():
	fileList = os.listdir("sampleDocs")
	return fileList
	
def makeTdMatrix(stopList,fileList):
	global tdMatrix
	tdMatrix = {}
	for file in fileList:
		fileO = open("sampleDocs/"+file)
		line = fileO.readline()
		while line:
			lineWords = line.split()
			for word in lineWords:
				word = word.lower()
				if word not in stopList:
					if word not in tdMatrix.keys():
						tdMatrix[word] = [0]*len(fileList)
					tdMatrix[word][fileList.index(file)] += 1
			line = fileO.readline()
	#for key in tdMatrix.keys():
	#	print key, tdMatrix[key]
 
def calculate_tf_idf():
	idf_dict = {}
	global wMatrix
	wMatrix = {}
	for key in tdMatrix.keys():
		wMatrix[key] = [0]*len(fileList)
		files = tdMatrix[key]
		idf_dict[key] = 0.0
		for file in files:
			if file!=0:
				idf_dict[key] += 1
		idf_dict[key] = 1/idf_dict[key]
		index = 0
		while index < len(fileList):
			wMatrix[key][index] = idf_dict[key]*tdMatrix[key][index]
			index += 1
	calculate_d_vector()
	#for key in wMatrix.keys():
	#	print key, wMatrix[key]

def calculate_d_vector():
	global d_vector
	d_vector = {}
	for file in range(0,len(fileList)):
		dict = {}
		for key in wMatrix.keys():
			dict[key] = wMatrix[key][file]
		d_vector[fileList[file]] = dict
	
def calculate_q_vector(query):
	global q_vector
	q_vector = {}
	query = query.split()
	for key in wMatrix.keys():
		q_vector[key] = 0
	for word in query:
		q_vector[word] = query.count(word)
	
def calculate_dot_product():
	global dot_product
	dot_product = []
	for file in fileList:
		result = 0
		for word in q_vector.keys():
			result += q_vector[word]*d_vector[file][word]
		dot_product.append((file,result))
	dot_product = sorted(dot_product, key= lambda tup: tup[1], reverse=True)
	
def vectorSearch():
	query = raw_input("Enter the query to be searched: ")
	calculate_tf_idf()
	calculate_q_vector(query)
	calculate_dot_product()
	for tuple in dot_product:
		if tuple[1]!=0:
			print tuple[0]
	
if __name__ == "__main__":
	main()