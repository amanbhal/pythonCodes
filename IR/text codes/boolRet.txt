#! /usr/bin/python

from helpers import getStopList, getFileList, growDict, printDict

def main():
    stopLst = getStopList("../Files/")
    [fList, tPath] = getFileList("../Files/","sampleDocs/")
    tokDict = {}
    for f in fList:
        tokDict = growDict(tokDict, f, fList.index(f), tPath,\
                     stopLst, len(fList), 1)
    query = queryInput()
    #printDict(tokDict, 1)
    print query
    boolSearch(tokDict, query, fList)

def boolSearch(tokDict, query, fList):
    qTokens = query.split()
    qLen = len(qTokens)
    res = []
    count = 0
    parRes = fList[:]
    while True:
        term = qTokens[count]
        if not term in tokDict:
            parRes = []
        tempRes = parRes[:]
        for f in parRes:
            ind = fList.index(f)
            if not tokDict[term][ind]:
                tempRes.remove(f)
        parRes = tempRes[:]
        if count == (qLen - 1):
            print parRes
            res = list( set(res) | set(parRes) )
            break
        count += 1
        op = qTokens[count]
        count += 1
        if op == 'or':
            print parRes
            res = list( set(res) | set(parRes) )
            parRes = fList[:]
    print sorted(res)

def queryInput():
    cont = 1
    query = ''
    while cont != 3:
        term = raw_input("Term\n-> ")
        if ( not term.isalpha() ) and ( not term.isdigit() ):
            continue
        query += term
        cont = raw_input("And : 1, Or : 2, End : 3\n-> ")
        if int(cont) == 1:
            query += ' and '
        elif int(cont) == 2:
            query += ' or '
        else:
            cont = int(cont)
    return query

if __name__ == "__main__":
    main()
