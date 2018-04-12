# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:46:02 2017
@author: david
"""
try:
    from distutils.dir_util import copy_tree
    from operator import itemgetter
    import datetime as dt
    from collections import defaultdict

    import os
    import argparse
    import sys
    import math
    import csv
    
    import buildGraphPages as bgp
    import buildSearchPage as bsp
    import graphMaker as gm
    import htmlStrings as hs
    import makeScorePagesHTML as mspHTML
    import meteorProc as mp
    import beerProc as bp
    import mtEvalProc as mt
    import newVisualBleu as vb
    import readWrite as rw
    import simpleWer as sWer
    import statsProc as sp
    import terProc as tp
    
    ################################### args ######################################
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--ref", required=True, help="the reference file to be used (required)")
    parser.add_argument("-s","--src", required=True, help="the source file (for display purposes - required)")
    parser.add_argument("-hp","--hyp", required=True, help="the hypothesis file to be used (required)")
    ################################### args ######################################
    parser.add_argument("-g", "--graphs", help="flag to plot and draw graphs", action='store_true')
    parser.add_argument("-sz", "--showZeros", help="flag to display zero score buckets", action='store_true')
    parser.add_argument("-a", "--advHist", help="show advanced histogram, requires seaborn", action='store_true')
    parser.add_argument("-p", "--poly", help="show a linear line of best fit", action='store_true')
    parser.add_argument("-nb", "--numberOfBins", help="the scores will be split up into numberOfBins", default = 100, type=int)
    parser.add_argument("-ob", "--orderBy", help="choose which metric to order by [bleu, mtbleu, mtnist, ter, wer, edit, met]", default = 'bleu')
    parser.add_argument("-ca", "--colourAssist", help="removes colours that can be difficult to distinguish", action='store_true')
    parser.add_argument("-x", "--extension", help="extension name given to the output directory", default = '', type=str)
    ### START EXTRA SCORING METRICS ###
    parser.add_argument("-m", "--meteor", help="include METEOR scores (requires Java)", action='store_true')
    parser.add_argument("-t", "--ter", help="include TER scores (requires Java)", action='store_true')
    parser.add_argument("-mt", "--mtEval", help="include MT-eval scores (Perl)", action='store_true')
    parser.add_argument("-b", "--beer", help="include BEER scores (requires Java)", action='store_true')
    #### END EXTRA SCORING METRICS ###
    args = parser.parse_args()
    ################################# end args ####################################
    
    #lineTemplate = ['src','ref','hyp','senBleu','edScore','ed','senWer','goodMeas','refLen',
                    #'meteor', 'ter', 'mtBleu', 'mtNist','beer']
    
    start = dt.datetime.now()
    adv = args.advHist
    numberOfBins = args.numberOfBins
    doGraphs = args.graphs
    factors = [100, 50, 25, 20, 10, 5, 4, 2, 1]
    orderBy = args.orderBy
    orderChoices = {'bleu':3,'mtbleu':11 , 'mtnist':13,'ter':10,'wer':7,'edit':4,'met':9,'beer':14}
    poly = args.poly
    r = 0; g = 255; b = 10    
    refList = None; srcList = None; hypList = None
    sep = '~'*64    
    sz = args.showZeros
    
    hasMet = False
    hasTer = False
    hasMtEval = False
    hasBeer = False
    
    refLenPos =2
    senWer = 3
    goodnessMeasurePos = 4
    goodnessMeasureUnderOnePos = 5
    metPos = 7
    terPos = 8
    editDistPos = 9
    editSenDistPos =10
    bleuPos = 11
    
    metScores = []
    terScores = []
    mtBleuScores = []
    mtNistScores = []
    mtNormedNist = []
    beerScores =[]
    
    corpusEvalBleu = None
    corpusEvalNist = None
    
    try:
        refList = rw.readFile(args.ref)
        srcList = rw.readFile(args.src)
        hypList = rw.readFile(args.hyp)
        
        if len(refList) == len(hypList) and len(refList) == len(srcList):
            pass
        else:
            raise UnboundLocalError
    except IOError as io:
        print('There was a problem Loading your named files...')
        print(io)
        print('Please check and try again...')
        print('Exiting...')
        sys.exit()
    except UnboundLocalError as ule:
        print('Your given files have different lengths, please check and try again')
        print(len(refList),len(hypList),len(srcList))
        print('Please check and try again...')
        print('Exiting...') 
        sys.exit()
    except Exception as e:
        print('The following error occurred:')
        print(e)
        print('Please check and try again...')
        print('Exiting...')
        sys.exit()
    directory = '../vm_scores_' + dt.datetime.now().strftime("%d-%m-%Y")#_%H-%M")#_%H")#:%M:%S")
    if args.extension == '':   
        pass
    else:
        directory = '../vm_scores_' + args.extension + '_' + dt.datetime.now().strftime("%d-%m-%Y")#_%H-%M")#_%H")#:%M:%S")
    imgDir = directory + '/images/'
    metDir = None
    terDir = None
    mtEvalDir = None
    beerDir = None
    
    print('')
    print('REF = {0} --> HYP = {1} --> SRC = {2}'.format(len(refList),len(hypList),len(srcList)))
    print(sep)
    print('WORKING, please wait a moment... :-)')
    print(sep)
    
    if numberOfBins not in factors:
        numberOfBins = min(factors, key=lambda nb:abs(nb-args.numberOfBins))
        print("Your 'adjusted' number of bins is {0}:".format(numberOfBins))
    else:
        print("Your selected number of bins is {0}:".format(numberOfBins))
        
    webPageScores = []
    for i in range(100, 0, -int(100/numberOfBins)):
        webPageScores.append((float(i)/100))
    #print(webPageScores)
    
    print(sep)
    
    werScores, cList = sWer.getWerStats(refList,hypList,srcList)
    bleuScores, corpusBleu, totalEdSenDist = vb.generateBleuScores(refList, hypList)
    for idx, val in enumerate(bleuScores):
        if val[1] < 0:
            print(idx, refList[idx], val[1])
    if args.meteor:
        metScores = mp.generateMeteorScores(os, rw, args.hyp, args.ref)
        if len(metScores) == len(refList):
            hasMet = True
            metDir = directory + '/metFiles/'
    
    if args.ter:
        terScores = tp.generateTerScores(os, rw, args.ref, args.hyp)
        if len(terScores) == len(refList):
            hasTer = True
            terDir = directory + '/terFiles/'
    
    if args.mtEval:
        mtBleuScores, mtNistScores, corpusEvalBleu, corpusEvalNist, mtNormedNist = mt.generateMTEVALScores(os, 
                                                                                            rw, args.ref, args.hyp, args.src)
                                                                                            
        if len(mtBleuScores) == len(refList) and len(mtNistScores) == len(refList):
            hasMtEval = True
            mtEvalDir = directory + '/mtEvalFiles/'
            print('mtEval files will be saved in --> {0}'.format(mtEvalDir.replace('../','')))
            print(sep)
    
    if args.beer:
        beerScores = bp.generateBeerScores(os, rw, args.hyp, args.ref)
        if len(beerScores) == len(refList):
            hasBeer = True
            beerDir = directory + '/beerFiles/'

    #lineTemplate = ['src','ref','hyp','senBleu','edScore','ed','senWer','goodMeas','refLen',
                    #'meteor', 'ter', 'mtBleu', 'mtNistMain', 'mtNistNorm', 'beer']
    allResults = []
    
    for i in range(len(refList)):
        lineTemplate = []
        lineTemplate.append(srcList[i].strip())
        lineTemplate.append(refList[i].strip())
        lineTemplate.append(hypList[i].strip())
        lineTemplate.append(bleuScores[i][2])
        lineTemplate.append(bleuScores[i][1])
        lineTemplate.append(bleuScores[i][0])
        lineTemplate.append(werScores[i][0])
        lineTemplate.append(werScores[i][1])
        lineTemplate.append(werScores[i][2])
        
        if hasMet:
            lineTemplate.append(metScores[i])
        else:
            lineTemplate.append('N/A')
        if hasTer:
             lineTemplate.append(terScores[i])
        else:
            lineTemplate.append('N/A')
        if hasMtEval:
            lineTemplate.append(mtBleuScores[i])
            lineTemplate.append(mtNistScores[i])#[0])
            lineTemplate.append(mtNormedNist[i])
        else:
            lineTemplate.append('N/A')
            lineTemplate.append('N/A') 
            lineTemplate.append('N/A') 
            
        if hasBeer:
            lineTemplate.append(beerScores[i])
        else:
            lineTemplate.append('N/A')
          
        allResults.append(lineTemplate)

    if not os.path.exists(directory):
        os.mkdir(directory)
    
    headers = [['src','ref','hyp','bleu','eScore','eDist','wer','werScore',
               'refLen','meteor','ter','mtbleu','mtNistMain','mtNistNorm','beer']]
    headers += allResults    
    with open(directory+'/allResults.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(headers)
		
    lineNumber = None
    
    if orderBy == 'bleu':
        allResults = sorted(allResults, key = itemgetter(3,8, 6), reverse = True); lineNumber = 3
    elif hasMet and orderBy == 'met':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    elif hasTer and orderBy == 'ter':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    elif hasMtEval and orderBy == 'mtbleu':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    elif hasMtEval and orderBy == 'mtnist':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    elif orderBy == 'wer':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    elif orderBy == 'edit':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    elif orderBy == 'beer':
        allResults = sorted(allResults, key = itemgetter(orderChoices[orderBy],8,6), reverse = True)
        lineNumber = orderChoices[orderBy]
    else:
        allResults = sorted(allResults, key = itemgetter(3,8, 6), reverse = True)
        lineNumber = orderChoices[orderBy]
    
    def getClosestBinScore(val):
        if val >= 1:
            return 1.0
        else:
            return min(x for x in webPageScores if x > val)
    
    webPagesDict = defaultdict(list)
    
    if orderBy == 'wer':
        for idx, line in enumerate(allResults):
            webPagesDict[getClosestBinScore(line[lineNumber]/100.0)].append(line) #default lineNumber = 3
    else:
        for idx, line in enumerate(allResults):
            webPagesDict[getClosestBinScore(line[lineNumber])].append(line) #default lineNumber = 3
    
    def safeMakeDirectoryFolders(directory, ext):
        if not os.path.exists(directory+'/'+ext):
            os.mkdir(directory+'/'+ext) #images')
   
    safeMakeDirectoryFolders(directory,'images')
    safeMakeDirectoryFolders(directory,'jQuery')
    safeMakeDirectoryFolders(directory,'scorepages')
   
    if doGraphs:
        safeMakeDirectoryFolders(directory,'graphs')
        safeMakeDirectoryFolders(directory,'graphs/Sen_Bleu')   
        if hasMtEval:
            safeMakeDirectoryFolders(directory,'graphs/MT_Bleu') 
            safeMakeDirectoryFolders(directory,'graphs/MT_NIST') 
        if hasMet:
            safeMakeDirectoryFolders(directory,'graphs/METEOR')
        if hasTer:
            safeMakeDirectoryFolders(directory,'graphs/TER')
        if hasBeer:
             safeMakeDirectoryFolders(directory,'graphs/BEER')
        safeMakeDirectoryFolders(directory,'graphs/WER') 
        safeMakeDirectoryFolders(directory,'graphs/Edit_Dist') 
    
    barsForPlot = sp.buildPage(srcList, refList, hypList, rw, corpusBleu, cList, 
                               hs, directory, totalEdSenDist, hasTer, hasMtEval, hasMet, hasBeer) #*****
        
    if metDir != None:
        if not os.path.exists(directory+'/meteorFiles'):
            os.mkdir(directory+'/meteorFiles')
        fi = 'vb_METEOR_output.txt'
        try:
                os.rename(fi, directory+'/meteorFiles/' + fi)
        except Exception as e:
            print('File {0} could not be moved, please check and try again...'.format(fi))
            print(e)
    
    if beerDir != None:
        if not os.path.exists(directory+'/beerFiles'):
            os.mkdir(directory+'/beerFiles')
        fi = 'vb_BEER_output.txt'
        try:
                os.rename(fi, directory+'/beerFiles/' + fi)
        except Exception as e:
            print('File {0} could not be moved, please check and try again...'.format(fi))
            print(e)
              
    if terDir != None:
        if not os.path.exists(directory+'/terFiles'):
            os.mkdir(directory+'/terFiles')
        trFiles =['trHyp.txt', 'trRef.txt', 'tr.pra', 'tr.pra_more',
                  'tr.sum', 'tr.sum_nbest', 'tr.ter', 'tr.xml', 'trOutput.txt']
        for fi in trFiles:
            try:
                os.rename(fi, directory+'/terFiles/' + fi)
            except Exception as e:
                print('File {0} could not be moved, please check and try again...'.format(fi))
                print(e)
                
    if mtEvalDir != None:
        if not os.path.exists(directory+'/mtEvalFiles'):
            os.mkdir(directory+'/mtEvalFiles')
        mtFiles =['mtEvalBleu.txt', 'mtEvalNist.txt', 'mtEvalStats.txt', 'out_MTEval.txt',
                  'refset.txt', 'srcset.txt', 'tstset.txt']
        
        for fi in mtFiles:
            try:
                os.rename(fi, directory+'/mtEvalFiles/' + fi)
            except Exception as e:
                print('File {0} could not be moved, please check and try again...'.format(fi))
                print(e)
  
    # copy subdirectory images
    copy_tree('images/', directory+'/images')
    copy_tree('jQuery/', directory+'/jQuery')
    
    # undo this
    bList = [hs.head]
    bList.append("""
            <div style="width:100%; text-align:center;">
                <h2 style="margin: 4 auto;">~~~~~~~~~~~~~~~~~~~~ View Sentence Level scores ~~~~~~~~~~~~~~~~~~~~ </h2>
            </div>""")
    topVal = 100
    #tmpDeeList = []
    searchList = []
    icnLeft = 0
    icnLeft = (1732 - (len(webPagesDict.keys()) * (1732/20)))/2
    if icnLeft < 0:
        icnLeft = 0
    for idx, k in enumerate(sorted(webPagesDict.keys(), reverse = True)):
        #print(k)
        mspHTML.makeScorePage(k, webPagesDict[k], rw, hs, directory+'/scorepages/', hasMet, hasTer, hasMtEval, hasBeer, itemgetter) #*****

        if args.colourAssist:
            r = 238; g =232; b = 170
        bList.append(hs.btnDiv.replace('###','{0},{1},{2}'.format(int(r),
                                       int(g),int(b))).replace('%%%',
                                       '{0}'.format(k)).replace('lft',str(icnLeft)).replace('xxx',
                                       '[{0}]'.format(len(webPagesDict[k]))).replace('~~~',
                                       'scorepages/upto_{0}.html'.format(k)))

        if g > 0:
            r += math.ceil(255.0/(numberOfBins)) 
            g -= math.ceil(255.0/(numberOfBins)) 
         
        dirStr = '{0}/scorepages/upto_{1}.html'.format(directory,k)
        searchList.append([webPagesDict[k], dirStr])
    
    def graphTable():
        scores = [('senBleuGraphs.html','Sen Bleu'), ('mtBleuGraphs.html','MT Bleu'), ('mtNistGraphs.html','MT NIST'), 
                  ('meteorGraphs.html','METEOR'),('terGraphs.html','TER'),('werGraphs.html','WER'),
                  ('editGraphs.html','Edit Dist'),('beerGraphs.html','BEER')]
        
        graphHtml = ['<h2>~~~~~~~~~~~~~~~~~~~~ View Graphs ~~~~~~~~~~~~~~~~~~~~ </h2>']
        graphHtml.append('<table style="margin: 0px auto;border-spacing: 0px;">\n<tr>')
        
        for idx, el in enumerate(scores):
            if not hasMtEval and idx == 1: continue
            if not hasMtEval and idx == 2: continue
            if not hasMet and idx == 3: continue
            if not hasTer and idx == 4: continue
            if not hasBeer and idx == 7: continue
        
            miniGraphIcon = 'tabIconNoText.png'
            if args.colourAssist:
                miniGraphIcon = 'tabIconNoTextNoCol.png'
                
            hStr = """<td style="padding:0 15px 0 15px;"><a href="graphs/{0}">
                    <img src="images/{2}" alt="{1}" title="{1}" style="width:64px;height:64px;"></a></td>""".format(el[0], el[1], miniGraphIcon)
            
            graphHtml.append(hStr)
        graphHtml.append("""<td style="padding:0 15px 0 15px;"><a href="graphs/gen.html">
                    <img src="images/{0}" alt="General" title="General" style="width:64px;height:64px;"></a></td>""".format(miniGraphIcon))   
        graphHtml.append("</tr><tr>")
        for idx, el in enumerate(scores):
            if not hasMtEval and idx == 1: continue
            if not hasMtEval and idx == 2: continue
            if not hasMet and idx == 3: continue
            if not hasTer and idx == 4: continue
            if not hasBeer and idx == 7: continue
            hStr = """<td style="text-align:center;"><a href="graphs/{0}">{1}</a></td>""".format(el[0], el[1])
            
            graphHtml.append(hStr)
        graphHtml.append("""<td style="text-align:center;"><a href="graphs/gen.html">General</a></td>""")
        graphHtml.append("</tr></table>")
        return '\n'.join(graphHtml)
        
    if doGraphs:
        print("Generating Graphs...")
        bgp.buildGraphPages(webPagesDict, hs, rw, directory, hasMet, hasTer, hasMtEval, hasBeer, gm, poly) 
        bList.append(hs.graphsTail.replace('TABLETOP', graphTable()))
    else:
        bList.append(hs.tail)
    rw.writeFile(bsp.showList(searchList), directory + '/search.html')    
    rw.writeFile(bList, directory+'/main.html')
    rw.writeFile([hs.css], directory+'/style.css')
    #undo this
    
    if doGraphs:
        print(sep)
        print('Creating the final general graphs...')
        graphList = [hs.scorepagesHead]
        #graphStr = hs.graphs
        graphList.append(hs.graphs)
        graphList.append(hs.shortTail)
        gm.makeGraphs(webPagesDict, imgDir, adv, poly, barsForPlot)
        rw.writeFile(graphList,'{0}/graphs/gen.html'.format(directory))
    else:
        print("The graph option was not selected...")
    print(sep)    
    print('ALL Done :-)')
    print('Time taken to complete ---> {0}'.format(dt.datetime.now() - start))
    print(sep)
except ImportError as imerr:
    print(sep)
    print('Sorry could not import the required packages')
    if 'Smoothing' in str(imerr):
        print(sep)
        print("Err = '{0}'".format(imerr))
        print('Please check your NLTK install')
    else:
        print('another error')
        print(imerr)
except ZeroDivisionError as zde:
    print("")
    print("There was a zero division error,")
    print("This usually means the BLEU score was too low...")
    print("***{0}***".format(zde))
    print("STOPPING...\n")
except Exception as e:
    print("")
    print("There was an error :-(")
    print("ERROR TYPE = {0}".format(e))
    print("Please check and try again...")
