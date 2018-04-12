# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:12:16 2017
@author: david
"""

#meteor processor



def generateBeerScores(os, rw, hyp, ref):
    beerSegScores = []
    sep = '~'*64
    tScore = None
    finalBeer = None
    
    print("Running BEER, please wait a moment...")
    try: 
        beerFileName = 'vb_BEER_output.txt'
        bash = './beerMain/beer_2.0/beer -s {0} -r {1} --printSentScores > {2}'.format(hyp, ref,beerFileName)
        os.system(bash)
        iniBeerResults = rw.readFile(beerFileName)
        cnt = 0
        for line in (iniBeerResults):
            if "sent" in line:
                tmp = line.strip().split()
                
                try:
                    tScore = float(tmp[-1])
                    tScore = "%.4f" % tScore
                    tScore = float(tScore)
                    beerSegScores.append(tScore)
                    cnt += 1
                except:
                    tScore = -1.0  
                    beerSegScores.append(tScore)
            elif 'BEER' in line:
                finTmp = line.strip().split()
                finalBeer = float(finTmp[-1])
                
        print('Finished generating the BEER scores')
        print('The BEER scores are stored in --> {0}'.format(beerFileName))
        print('The BEER score list has {0} elements'.format(cnt)) 
        print('The overall BEER score is: {0}'.format(finalBeer))
    except:
        print("Couldn't run BEER. Is JAVA installed?")
    print(sep)
    
    return beerSegScores