import os

def main():
	stopList = makeStopList()
	fileList = makeFileList()
	makeTdMatrix(stopList,fileList)
	
def makeStopList():
	fileO = open("StopWord.txt", "r")
	fileTxt = fileO.read()
	stopList = fileTxt.split()
	return stopList
	
def makeFileList():
	fileList = os.listdir("sampleDocs")
	return fileList
	
def makeTdMatrix(stopList,fileList):
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
	for key in tdMatrix.keys():
		print key, tdMatrix[key]
	
if __name__ == "__main__":
	main()