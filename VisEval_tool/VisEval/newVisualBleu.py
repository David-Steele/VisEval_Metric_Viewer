#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:57:05 2017
@author: david
"""
import nltk.translate.bleu_score as bleu
import math
import nltk

from nltk.translate.bleu_score import SmoothingFunction
from nltk.metrics import edit_distance as ed

sf = SmoothingFunction()
bleuSep = '~'*64

def generateBleuScores(inRef, inHyp):
    refList = []    
    hypList = []
    allBleu = []
    
    totalEdSenDist = 0
    
    print('Using nltk version --> {0}... (should be >= 3.2.4)\n{1}'.format(nltk.__version__,bleuSep))
    for i,line in enumerate(inRef):
        listOfLists = []
        listOfLists = [line, inHyp[i]]
        #if i < 10:
            #print('***',listOfLists)
       
        #for al, aList in enumerate(listOfLists):
        refSen = line.strip().split()
        edRef = line.strip()
        refList.append([refSen])
        
        hypSen = listOfLists[1].strip().split()
        edHyp = listOfLists[1].strip()
        hypList.append(hypSen)
        
        #edDist = None; edSenDist = None
        
        try:
            edDist = ed(edRef,edHyp)
            edSenDist = edDist/(len(edRef)*1.0)
            edSenDist = 1 - edSenDist
            edSenDist = "%.4f" % edSenDist
        except Exception as e:
            edDist = -0
            edSenDist = -0
            print('Edit Distance Failed...')
            print(e)
        try:
            senBleu = bleu.sentence_bleu([refSen],hypSen,
                                    emulate_multibleu=True, auto_reweigh=True, 
                                    smoothing_function=sf.method4)
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            #print('General Exception')
            #print(type(e))
            #print(e)
            if i%50 == 0:
                print('Sentence',i,'Newer versions of NLTK set "emulate_multibleau=True" by default')
            senBleu = bleu.sentence_bleu([refSen],hypSen,
                                    auto_reweigh=True, 
                                    smoothing_function=sf.method4)
        #edSenDist =-1
        bleuKey = int(math.ceil(senBleu*100))
        if bleuKey == 0:
            bleuKey = 1
        totalEdSenDist += float(edSenDist)
        edSenDist = float(edSenDist)
        if edSenDist < 0:
            edSenDist = 0
        allBleu.append([edDist, edSenDist, senBleu])
        #bleuDict[bleuKey].append([edDist, float(edSenDist), senBleu])
        #print(aList)
    try:
        corpusBleu = bleu.corpus_bleu(refList,hypList,
                                            emulate_multibleu=True)
    except Exception as e:
        #print(type(e))
        #print(e)
        if i%50 == 0:
            print('Sentence',i,'Newer versions of NLTK set "emulate_multibleau=True" by default')
        corpusBleu = bleu.corpus_bleu(refList,hypList)
        
    print('Standard Corpus Bleu = {0}'.format(corpusBleu))
    print(bleuSep)
    return allBleu, corpusBleu, totalEdSenDist