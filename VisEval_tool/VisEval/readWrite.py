# -*- coding: utf-8 -*-
"""@author: david, Date Fri Jan 22 17:17:38 2016"""


def readFile(fileIn):
    # Open a file in read mode
    fi = open(fileIn, "r")  
    lines = fi.readlines()
    fi.close()
    return lines

def writeFile(outList, fileOut):
    fo = open(fileOut, "w")
    for line in outList:
        fo.write(line)
    fo.close()