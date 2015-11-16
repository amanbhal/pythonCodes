#! /usr/bin/python

from os.path import join, isfile
import os
from helpers import growDict, getFileList, getStopList

def main():
    rootPath = "../Files/"
    sampleDocPath = "sampleDocs/"
    stopLst = getStopList(rootPath)
    [fileLst, targetPath] = getFileList(rootPath, sampleDocPath)
    tokDict = {}
    for f in fileLst:
        print "Reading: %s",f
        tokDict = growDict(tokDict, f, fileLst.index(f), \
                                       targetPath, stopLst, \
                                       len(fileLst) )
    for key in tokDict:
        print key,":\t",tokDict[key]
    evalStats( tokDict )

def evalStats( tokDict ):
    tokens = tokDict.keys()
    tokens.sort()
    docMax = ['aword',0]
    for token in tokens:
        docNum = countNon( tokDict[token] )
        if docNum > docMax[1]:
            docMax = [token, docNum]
    print docMax
    print tokDict[ docMax[0] ]

def countNon( lst ):
    count = 0
    for item in lst:
        if int(item) != 0:
            count += 1
    return count

if __name__ == "__main__":
    main()
