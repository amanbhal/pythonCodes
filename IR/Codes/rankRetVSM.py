#! /usr/bin/python

from helpers import getStopList, getFileList, printDict, tokenize
import math

def main():
    stopList = getStopList("../Files/")
    [fileList, tPath] = getFileList("../Files/","sampleDocs/")
    qVector = queryInput(stopList)
    docVs = docVectorGen(fileList, tPath, stopList)
    simDict = simCalc(docVs, qVector)
    printDict(simDict)
    evaluateSim(simDict)

def queryInput(stopList):
    #option = raw_input("Query File (0) or String (1):\n-> ")
    option = 1
    matter = raw_input("Enter the FileName/QueryString\n-> ")
    if int(option):
        qVector = tokenize(matter, stopList, 0, 1)
    else:
        fileO = open(matter)
        qVector = tokenize(fileO, stopList, 0)
    return qVector

def docVectorGen(fileList, tPath, stopList):
    docVs = {}
    for f in fileList:
        fileO = open(tPath+f)
        docVs[f] = tokenize(fileO, stopList, 0)
    return docVs

def simCalc(docVs, qVector):
    qWeight = weigh(qVector)
    simV = {}
    for f in docVs:
        fVector = docVs[f]
        fWeight = weigh(fVector)
        dotP = 0
        for term in qVector:
            if term in fVector:
                dotP += qVector[term]*fVector[term]
        simV[f] = float( dotP ) / (fWeight * qWeight)
    return simV

def weigh(vector):
    sum = 0
    for key in vector:
        sum += vector[key]*vector[key]
    return math.sqrt(sum)

def evaluateSim(simDict):
    maxSim = ['file', 0]
    minSim = ['file', 2]
    allKeys = sorted(simDict.keys())
    for f in allKeys:
        if simDict[f] > maxSim[1]:
            maxSim = [f, simDict[f]]
        if simDict[f] < minSim[1]:
            minSim = [f, simDict[f]]
    print "Most Similar Doc :",maxSim[0]," & Similarity:",maxSim[1]
    print "Least Similar Doc :",minSim[0]," & Similarity:",minSim[1]

if __name__ == "__main__":
    main()
