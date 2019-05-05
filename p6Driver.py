#!/user/bin/env python3
import os
import sys
from p5Dict import argCheck, parseFile, printtext, printVariables, printLabels, printFile
from p6Exec import transferData, execute

count=0

def openFILE(F):
    '''open file then read the line'''
    global count
    try:
        with open(F, 'r') as FILE:
            for line in FILE:
                parseFile(line, count)
                count +=1
    except Exception as e:
        print(e)
        exit(1)

def main():
    '''main function'''
    argCheck()
    FILE = sys.argv[1]
    openFILE(FILE)
    printFile(FILE)
    printVariables()
    printLabels()
    transferData()
    if "-v" in sys.argv:
        execute(v = True)
    else:
        execute()

if __name__ == "__main__":
    main()
