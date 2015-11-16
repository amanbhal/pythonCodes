import os

def main():
	stopList = makeStopList()
	global fileList
	fileList = makeFileList()
	makeTdMatrix(stopList,fileList)
	wordSearch = raw_input("Enter the word: ")
	boolRetrieval(wordSearch)
	queryResult()
	
	
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
	
def boolRetrieval(wordSearch):
		if wordSearch in tdMatrix.keys():
			for word in tdMatrix.keys():
				if word == wordSearch:
					files = tdMatrix[word]
					index = 0
					while index < len(files):
						if files[index] != 0:
							print fileList[index]
						index += 1
		else:
			print "Word Does not Exist."
		
def queryResult():
	query = ""
	seperator = ""
	while seperator!="end":
		term = raw_input("Enter the query term: ")
		if ( not term.isalpha() ) and ( not term.isdigit() ):
			continue
		query += " "+term+" "
		seperator = raw_input("Enter either 'and' or 'or' or 'end'")
		if seperator!="end":
			query += " "+seperator+" "
	query = query.split()
	print query
	index = 0
	resultFiles1 = []
	resultFiles2 = []
	while index<len(query):
		word = query[index]
		if word in tdMatrix.keys():
			files = tdMatrix[word]
			print files
			fileIndex = 0
			while fileIndex < len(files):
				if files[fileIndex]!=0:
					if index == 0:
						resultFiles1.append(fileList[fileIndex])
					else:
						resultFiles2.append(fileList[fileIndex])
				fileIndex += 1
		index += 2
	resultFiles = []
	if query[1] == "and":
		for file1 in resultFiles1:
			for file2 in resultFiles2:
				if file1 == file2:
					resultFiles.append(file1)
	elif query[1] == "or":
		resultFiles = resultFiles1+resultFiles2
	print resultFiles
	
	
if __name__ == "__main__":
	main()