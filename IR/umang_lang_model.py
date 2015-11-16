#! /usr/bin/python
from __future__ import division
import os

def main():
	lam= 0.5
	totalword = 0
	word_in_docs = {}
	filelist = os.listdir("SampleDocs/")
	docs_term = {}
	term_in_all_docs = {}
	for file in filelist:
		docs_term[file] = {}
		word_in_docs[file] = 0
		words = open("SampleDocs/"+file).read().split()
		for word in words:
			if word in docs_term[file]:
				docs_term[file][word] += 1
			else:
				docs_term[file][word] = 1
			totalword += 1
			word_in_docs[file] +=1
			
			if word in term_in_all_docs:
				term_in_all_docs[word] += 1
			else:
				term_in_all_docs[word] = 1
				
	
	prob = {}

	query = raw_input("Enter the query")
	qwords = query.split()
	for file in filelist:
		prob[file] = 0.0
		for qword in qwords:
			if qword in docs_term[file]:				
				prob[file] += lam*(docs_term[file][qword]/word_in_docs[file]) + (1-lam)*(term_in_all_docs[qword]/totalword)
	
	print prob
main()
