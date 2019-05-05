#!/user/bin/env python3
import sys 
import os
import re

textlines=[] #all lines go in here
varTypeD={} #var name and type
varValueD={} #var name and value
labelD={} #label name and line number

def printVariables():
    print("Variables:")
    print("    Variable    Type    Value")
    for name in varTypeD:
        print("    {}    {}    {}".format(name, varTypeD[name], varValueD[name]))

def printLabels():
    print("Labels:")
    print("    Label    Statement")
    for label in labelD:
        print("    {}    {}".format(label, labelD[label]))

def printFile(f):
    print("BEEP source code in {}:".format(f))
    for i in range(len(textlines)):
        print("{}. {}".format(i+1, textlines[i].rstrip()))

def declab(t, l, c):
    ts = str(t)
    st = ts.split(":")
    st[0] = st[0].replace(" ", "") 
    if not st[0] in labelD:
        labelD[st[0]] = c+1
    else:
        print("***Error: label '{}' appears on mutliple lines: {} and {}".format(st[0], labelD[st[0]], c+1))
        return

#t=token vt=varType vv=varValue
def declareVar(t, vt, vV):
    ts = str(t)
    st = ts.split()
    varname = st[2] #""""""""fix it
    vt[varname]= st[1]
    if len(st) == 3:
        vV[varname] = ""
    else:
        vV[varname] = st[3]
    return

def argCheck():
    '''check args''' 
    if len(sys.argv) != 2:         
        print("Error incorrect arguments!\nPlease use only one file")        
        exit(1)
    return

#t = list, vT = dictionary var type, vV = dictionary var value, l = label dictionary, s = line being read
def parseFile(line, count):
    textlines.append(line)
    if re.search(r'^VAR[ ]', textlines[count]):
    #print(re.search(r'^VAR[ ]', textlines[count]))
        declareVar(textlines[count], varTypeD, varValueD)
    elif re.search(r'^.*:[ ]', textlines[count]):
        #print(re.search(r'^.*:[ ]', textlines[count]))
        declab(textlines[count], labelD, count)
    return

def printtext():
    print(textlines)
    
    '''
    textlines=[] #all lines go in here
    varTypeD={} #var name and type
    varValueD={} #var name and value
    labelD={} #label name and line number
    '''
def transferData2():
    tl = textlines
    vtd = varTypeD
    vvd = varValueD
    ld = labelD  
    return(tl, vtd, vvd, ld)
