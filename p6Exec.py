#!/user/bin/env python3
import os
import sys
import re
from p5Dict import transferData2

textlines=[]
varTypeD={}
varValueD={}
labelD={}

def transferData():
    global textlines, varTypeD, varValueD, labelD
    textlines, varTypeD, varValueD, labelD = transferData2()
    #print("{}".format(textlines[13].lstrip()))


def flabels():
    for i in range(len(textlines)):
        if textlines[i] == "\n":
            continue
        line = textlines[i]
        line = line.lstrip()
        line = line.split()
        if re.search(r'^.*:', line[0]):
            textlines[i] = line[1:]
        else:
            textlines[i] = line
    return 

def execute():
    print("execution begins...")
    i=0
    infloop = 0
    global varTypeD, varValueD
    flabels()
    #for i in range(len(textlines)):
    while(1):
        #note  line = line[at the index]
        if i > len(textlines)-1:
            break;
        if infloop > 5000:
            print("YALL DON FUCKED UP")
            break
        line = textlines[i]
        #print(line)
        
        if line[0] == "VAR":
            i += 1
            infloop += 1
            continue
        elif line[0] == "PRINT":
            i += 1
            infloop += 1
            printfunc(line[1:], i)
            continue
        elif line[0] == "ASSIGN":
            i += 1
            infloop += 1
            assfunc(line[1:], i)
            continue
        elif line[0].upper() == "IF":
            if (iffunc(line[1:], i)):
                i = labelD[line[-1]]-1
                #print(textlines[i])
            else:
                i += 1
                infloop += 1
        elif line[0] == "GOTO":
           i = gotofunc(line[1:], i)
           infloop +=1
        else:
            i+=1
            infloop += 1

def printfunc(line, count):
    #print("PRINT: {}".format(line))
    string = ""
    for e in line:
        if e[0] == "\"":
            e = re.sub("\"", "", e)
            string += e
        else:
            try:
                string  += (" "+str(varValueD[e])+" ")
            except Exception as ex:
                 print("*** line %d error detected ***" % (count)) 
                 print("*** Var not defined: %s ***" % (e))
                 exit(0)
        #string += e
    print(string)
        
def assfunc(line, count):
    ''''''
    if len(line[1:]) == 1:
        varValueD[line[0]] = varValueD[line[1]]
        return
    else:
        op = line[1]
        var1 = line[2]
        var2 = line[3]
        if not var1.isdigit():
            var1 = str(varValueD[var1])
        if not var2.isdigit():
            var2 = str(varValueD[var2])
        varValueD[line[0]] = eval(var1+op+var2) #error handle

def iffunc(line, count):
    ''''''
    var1 = line[1]   
    var2 = line[2]
    if not var1.isdigit():
        var1 = str(varValueD[var1])
    if not var2.isdigit():
        var2 = str(varValueD[var2])
    return(eval(var1+line[0]+var2)) #error handle

def gotofunc(line, count):
    ''''''
    line = line[0]
    return labelD[line]-1
'''
class TooFewOperands(Exception):
    def __init__(self, args, kwargs):
        super().__init__(self, args, kwargs)

class VarNotDefined(Exception):
    def __init__(self, args, kwargs):
        super().__init__(self, args, kwargs)

class LabelNotDefined(Exception):
    def __init__(self, args, kwargs):
        super().__init__(self, args, kwargs)

class InvalidExpression(Exception):
    def __init__(self, args, kwargs):
        super().__init__(self, args, kwargs)

class InvalidvalueType(Exception):
    def __init__(self, args, kwargs):
        super().__init__(self, args, kwargs)
'''
