#!/usr/bin/python

import sys
import os
import datetime 

isodate = lambda y, m, d, hh, mm, ss: '%04d%02d%02dT%02d%02d%02dZ'%(y,m,d,hh,mm,ss)

def currisodate():
    dateObj = datetime.datetime.now()
    return isodate(dateObj.year,dateObj.month,dateObj.day,dateObj.hour,dateObj.minute,dateObj.second)

def isOrdinal(inpLine):
    try:
        return int(inpLine)
    except ValueError:
        return 0

def checkSRT(fileName):
    inLines = []
    outLines = []
    try:
        f=open(fileName)
        inLines = f.readlines()
        f.close()
    except FileNotFoundError:
        print('Input error!!!')
        pass
    subCounter = 0
    for line in inLines:
        if isOrdinal(line):
            subCounter += 1
            outLines.append('%d\n'%(subCounter,))
        else:
            outLines.append('%s'%(line,))

    outFileName = '%s_mod_%s'%(currisodate(),fileName)
    f=open(outFileName,'w')
    f.writelines(outLines)
    f.close()

try:    
    checkSRT(sys.argv[1])
except IndexError:
    pass
