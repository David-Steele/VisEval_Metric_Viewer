# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:33:11 2017
@author: david
"""

#mt evaluation metric v14, requires Perl

def buildSegmentedFiles(ref, hyp, src, rw, trglang='en', srclang='en'):

    pIn = '<p>\n'
    pOut = '</p>\n'
    docOut = '</doc>\n'
    outList = []
    
    for fin in [[ref,'refset'],[hyp, 'tstset'], [src,'srcset']]:
        head = '<{0} trglang="{1}" setid="testName" srclang="any">\n'.format(fin[1], trglang)
        docHead = '<doc sysid="mt_build" docid="sys_eval" genre="any" origlang="{0}">\n'.format(srclang)
    
        endFile = '</{0}>'.format(fin[1])
    
     
        inList = rw.readFile(fin[0])
        
        outList = []
        outList.append(head)
        outList.append(docHead)
        outList.append(pIn)
        
        for i, line in enumerate(inList):
            outList.append('<seg id="{0}">{1}</seg>\n'.format(i+1, line.strip()))
            
        outList.append(pOut)
        outList.append(docOut)
        outList.append(endFile)
        
        rw.writeFile(outList, '{0}.txt'.format(fin[1]))
        print('Built ---> MT {0} (total segments = {1})'.format(fin[1], len(outList) - 6))

def normaliseNist(aList):
    normList = []
    nMin = min(aList)
    nMax = max(aList)
    nDiff = nMax - nMin
    
    for val in aList:
        normList.append(round( ((val - nMin)*1.0)/nDiff, 4))
    
    return normList
        
def generateMTEVALScores(os, rw, ref, hyp, src):
    print("Generating MT_Eval scores, please wait a moment...")
    
    sep = '~'*64
    miniSep = '~'*44
    print(miniSep)
    buildSegmentedFiles(ref, hyp, src, rw, 'zh')
    print(miniSep)
    
    r = 'refset.txt'
    h = 'tstset.txt'
    s = 'srcset.txt'
    
    mtEvalNist = None
    mtEvalBleu = None
    mtStats = []
    mtNist = []
    mtBleu = []
    mtNormedNist = None
    
    try: 
        #'cmd = "perl -version"
        mtCmd = "./mtEval/mteval-v14.pl -r {0} -t {1} -s {2} -d 2 > out_MTEval.txt".format(r, h, s) 
        os.system(mtCmd)
        
        mtEvalList = rw.readFile('out_MTEval.txt')
        
        for line in mtEvalList:
            if "BLEU score using" in line:
                mtBleu.append(line)
            elif "NIST score using" in line:
                mtNist.append(line)
            else:
                mtStats.append(line)
        
        print('Writing MT EVAL output files, please wait...')
        rw.writeFile(mtStats, 'mtEvalStats.txt')
        rw.writeFile(mtNist, 'mtEvalNist.txt')
        rw.writeFile(mtBleu, 'mtEvalBleu.txt')
        print('MT EVAL output files have been saved.')
        print(miniSep)
        
        for idx, line in enumerate(mtNist):
            tmpNist = line.split()
            mtNist[idx] = float(tmpNist[5])
            
            tmpBleu = mtBleu[idx].split()
            mtBleu[idx] = float(tmpBleu[5])
        
        mtEvalNist = mtNist[-1]; mtEvalBleu = mtBleu[-1]   
        print('Corpus MT EVAL NIST = {0}, Corpus MT EVAL BLEU = {1}'.format(mtEvalNist, mtEvalBleu))

    except Exception as e:
        print("Couldn't run MT_Eval. Is PERL installed?")
        print("If Perl is installed, have you installed the 'Sort-Naturaly-1.03 module?'")
        print("(it can be found in visMet/mtEval...)")
        print(type(e))
        print(e)
    
    maxSize = len(mtNist) - 1
    mtNormedNist = normaliseNist(mtNist[:maxSize])
    print('Segment list sizes to be returned are: NIST {0}, BLEU {1}'.format(len(mtNist) -1, len(mtBleu) - 1))
    print(sep)
    #return mtBleu[:maxSize], mtNist[:maxSize], mtEvalBleu, mtEvalNist
    return mtBleu[:maxSize], mtNist[:maxSize], mtEvalBleu, mtEvalNist, mtNormedNist