#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 10:24:31 2017
@author: david
"""
import numpy
#from operator import itemgetter
from collections import defaultdict
#import math

exampleRefs = ["i love you", "i really love you", "i can 't help myself as i love you so much"]
badExampleHyps = ["i don 't love you", "i do not love you at all", "this sentence has no bearing on anything"]

werSep = '~'*64
emptyDict = defaultdict(list)

def getWerStats(refs, hyps, src):
    print("Calculating WER scores...")
    
    fullCorpusStats = []
    allWers = []
    if len(refs) == len(hyps):
        sumWers = 0
        sumGoodness = 0; sumLens = 0
        
        for i, el in enumerate(refs):
            senWer, goodnessMeas, refLen = wer(el.strip(), hyps[i].strip())
            sumWers += senWer
            sumGoodness += refLen*(goodnessMeas*1.0)
            sumLens += refLen
            allWers.append([senWer, goodnessMeas/100.0, refLen])
        fullCorpusStats = [len(refs), sumWers,sumWers/len(refs),sumGoodness/sumLens,sumLens/len(refs)]
        print(werSep)
        print('Total WER = {0}'.format(sumWers))
        print('Mean WER = {0}'.format(sumWers/(len(refs)*1.0)))
        print('Mean Sentence Length = {0}'.format(sumLens/(len(refs)*1.0)))
        print(werSep)
        return allWers, fullCorpusStats
    else:
        return None

def wer(r, h):
    r = r.split()
    rLen = len(r)
    
    h = h.split()
    
    
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint16)
    d = d.reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                subs = d[i-1][j-1] + 1
                ins    = d[i][j-1] + 1
                dels     = d[i-1][j] + 1
                d[i][j] = min(subs, ins, dels)
    
    returnVal = d[len(r)][len(h)]
    goodnessVal = ((returnVal/(rLen*1.0))*-100)+100
    if goodnessVal < 0:
        goodnessVal = 0
    return d[len(r)][len(h)], goodnessVal, rLen