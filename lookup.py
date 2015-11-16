import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("word",help="The word to be searched in the file")
parser.add_argument("file",help="The file to be searched")
args = parser.parse_args()

f = open(args.file)

lineNum = 0

for line in f.readlines():
	line = line.strip('\n\r') #The method strip() returns a copy of the string in which all chars have been 
							  #stripped from the beginning and the end of the string. \n\r is the new line character for windows
	
	lineNum += 1
	searchResult = re.search(args.word,line,re.M|re.I)
	if searchResult: 
		print lineNum,line