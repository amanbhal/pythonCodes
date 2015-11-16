#! /usr/bin/python

import os
from os.path import join, isfile

def main():
    searchStr = raw_input("Enter string to be searched\n->")
    targetPath = "../Files/sampleDocs/"
    lst = [f for f in os.listdir(targetPath) if isfile( join(targetPath, f) ) ]
    lst.sort()
    for f in lst:
        print "File: ",f,
        if search(searchStr, f, targetPath)==1:
            print "-> Found"
        else:
            print "-> notFound"

def search(sStr, fName, tPath):
    fileO = open(tPath+fName)
    fileStr = fileO.read()
    if sStr in fileStr:
        return 1
    else:
        return 0
    fileO.close()

if __name__ == "__main__":
    main()