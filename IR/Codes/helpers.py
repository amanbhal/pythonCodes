from os.path import join, isfile
import os

def growDict(tokDict, fName, fIndex, tPath, sLst, noCol, binary=0):
    fileO = open(tPath+fName)
    fileDict = tokenize(fileO, sLst, binary)
    for word in fileDict:
        if word in tokDict:
            tokDict[word][fIndex] = fileDict[word]
        else:
            tokDict[word] = zeroButOneList(noCol, -1)
            tokDict[word][fIndex] = fileDict[word]
    return tokDict

def tokenize(fileO, stopLst, binary, isString = 0):
    if isString:
        line = fileO
    else:
        line = fileO.readline()
    tokenized = {}
    while line:
        lineTokens = line.split()
        for token in lineTokens:
            token = token.lower()
            token = token.strip('.,"\'()`')
            if token in stopLst:
                pass
            else:
                if token in tokenized:
                    if not binary:
                        tokenized[token] += 1
                else:
                    tokenized[token] = 1
        if isString:
            line = ''
        else:
            line = fileO.readline()
    return tokenized

def printDict(tokDict, doSort=0):
    allKeys = tokDict.keys()
    if doSort:
        allKeys.sort()
    for key in allKeys:
        print key,":",tokDict[key]

def getFileList(rPath,sDPath):
    targetPath = join(rPath, sDPath)
    fileLst = [f for f in os.listdir( targetPath )\
                   if isfile( join(targetPath, f) ) ]
    fileLst.sort()
    return [fileLst, targetPath]

def getStopList(root):
    fileO = open(root+"StopWord.txt")
    fileStr = fileO.read()
    stopLst = fileStr.split()
    fileO.close()
    return stopLst

def zeroButOneList(n, ind):
    lst = [0] * n
    if ind != -1:
        lst[ind] = 1
    return lst
