# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:49:52 2017
@author: david
"""

#TER score generator

def makeTerRefAndHypFiles(rw, ref, hyp):
    rlist = rw.readFile(ref)
    hlist = rw.readFile(hyp)
    
    for i, row in enumerate(rlist):
        rlist[i] = '{0} (terIdx{1})\n'.format(row.strip(),i)
        hlist[i] = '{0} (terIdx{1})\n'.format(hlist[i].strip(),i)
    
    rw.writeFile(rlist, 'trRef.txt')
    rw.writeFile(hlist, 'trHyp.txt')
    
def generateTerScores(os, rw, ref, hyp):
    
    makeTerRefAndHypFiles(rw, ref, hyp)
    terSegScores = []
    sep = '~'*64
    tScore = None
    
    print("Generating TER scores, please wait a moment...")
    try: 
        hypLoc =  'trHyp.txt' #'tercom-0.7.25/sample-data/hyp.txt'
        refLoc = 'trRef.txt' #'tercom-0.7.25/sample-data/ref.txt'
        terLoc = 'tercom-0.7.25/tercom.7.25.jar'
        #java = 'java -jar tercom-0.7.25/tercom.7.25.jar -r ref.en.txt -h hyp.txt'# -n <output_prefix>
        
        java = 'java -jar {0} -r {1} -h {2} -n tr > trOutput.txt'.format(terLoc, refLoc, hypLoc)
        #print(java)
        os.system(java)
        
        iniTerResults = rw.readFile('tr.ter')
        for line in iniTerResults:
            if "terIdx" in line:
                tmp = line.strip().split()
                
                try:
                    tScore = float(tmp[-1])
                    tScore = "%.4f" % tScore
                    tScore = float(tScore)
                except:
                    tScore = 1.0 
                    print('Could not caluclate a TER score for current line...')
                if float(tScore) > 1:
                    tScore = 1.0
                terSegScores.append(tScore)
                
        print('Finished generating the TER scores')
        print("The TER scores are stored in the files prefixed with 'tr'")       
    except Exception as e:
        print("Couldn't run TER. Is JAVA installed?")
        print(type(e))
        print(e)
    print(sep)
    
    return terSegScores