# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:12:16 2017
@author: david
"""

#meteor processor



def generateMeteorScores(os, rw, hyp, ref):
    metSegScores = []
    sep = '~'*64
    tScore = None
    
    print("Running METEOR, please wait a moment...")
    try: 
        metFileName = 'vb_METEOR_output.txt'
        java = 'java -Xmx2G -jar meteor-1.5/meteor-*.jar {0} {1} -l en -norm'.format(hyp, ref)
        os.system(java +" > " + metFileName)
        iniMetResults = rw.readFile(metFileName)
        cnt = 0
        for line in (iniMetResults):
            if "Segment" in line:
                tmp = line.strip().split()
                
                try:
                    tScore = float(tmp[-1])
                    tScore = "%.4f" % tScore
                    tScore = float(tScore)
                    metSegScores.append(tScore)
                    cnt += 1
                except:
                    tScore = -1.0  
                    metSegScores.append(tScore)
                
        print('Finished generating the METEOR scores')
        print('The METEOR scores are stored in --> {0}'.format(metFileName))
        print('The METEOR score list has {0} elements'.format(cnt)) 
        #print(len(metSegScores))
    except:
        print("Couldn't run Meteor. Is JAVA installed?")
    print(sep)
    
    return metSegScores