# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:51:31 2017

@author: david
"""

import readWrite as rw
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-r","--ref", help="the reference file to be used (required)")
parser.add_argument("-hp","--hyp", help="the hypothesis file to be used (required)")
parser.add_argument("-s","--src", help="the src file to be used (required)")

args = parser.parse_args()

outList = []

head = '<srcset setid="testName" srclang="any">\n'
docHead = '<doc sysid="src" docid="evaluation" genre="any" origlang="zh">\n'
pIn = '<p>\n'
pOut = '</p>\n'
docOut = '</doc>\n'
endFile = '</srcset>'

for fin in [args.ref, args.hyp, args.src]: 
    inList = rw.readFile(fin)
    outList = []
    outList.append(head)
    outList.append(docHead)
    outList.append(pIn)
    
    for i, line in enumerate(inList):
        outList.append('<seg id="{0}">{1}</seg>\n'.format(i+1, line.strip()))
        
    outList.append(pOut)
    outList.append(docOut)
    outList.append(endFile)
    
    rw.writeFile(outList,fin.replace('.txt','_mt_seg.txt'))
    print('DONE')