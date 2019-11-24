# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:45:43 2017
@author: david
"""

#makes all graphs pages including:
#the links to all graph pages
#the graphs pages themselves

#####################################
# start of graph building functions #
#####################################
import matplotlib.pyplot as plt
import numpy as np
gsep = '~'*64
hasTerG = False
hasMetG = False
hasMtEvalG = False
hasBeerG = False
srcG = None
refG = None
hypG = None
gm = None

def makeScatter(x,y,xlbl, ylbl, title, xlim = None, id = '', sf = False, bestFit = False, ylim = None, poly = 3, picSize=(9,9)):
    plt.figure(figsize=picSize)
    plt.scatter(x,y)#, color= '#7777aa')
    plt.xlabel(xlbl,fontsize=14)
    plt.ylabel(ylbl,fontsize=14)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, poly))(np.unique(x)), '-r', linewidth=3)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        #plt.ylim(ymin=0)
        plt.ylim(ylim)
    plt.title(title,fontsize=16)
    if sf:
        plt.savefig(id+xlbl+'_'+ylbl+'_scatter.png')
    else:
        plt.show()
    plt.close()

def makeAlphaHist(x,y,xName, yName, xlbl, title, xLim = None, id = '', ylbl = 'Frequency', sf = False):
    plt.figure(figsize=(16,9))    
    bins = 25
    val = 0
    binVals = []
    for i in range (bins):
        binVals.append(val)
        val += 1/float(bins)
    if binVals[-1] < 1:
        binVals.append(1.0)
        
    (bn, bbins, bpatches) = plt.hist(x,bins=binVals, alpha = 0.5,label=xName);
    (tn, tbins, tpatches) = plt.hist(y, bins=binVals, alpha = 0.5, label=yName);
    plt.legend()
    plt.title(title, fontsize = 16)
    plt.xlabel(xlbl, fontsize = 14)
    plt.ylabel(ylbl, fontsize = 14)
    
    if sf:
        plt.savefig(id + xName + '_' + yName + '_alphaHist.png')
    else:
        plt.show()
    plt.close()
    
def makeHistAndBox(x, title, xlbl='', id = '', sf = False):
    try:
        import seaborn as sns
        sns.set(style="ticks")
        
        fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, figsize=(16,9), 
              gridspec_kw={"height_ratios": (.12, .88)})
        sns.distplot(x, ax=ax_hist, bins = 25)
        sns.boxplot(x, ax=ax_box, whis=[0,100])
        
        plt.xlim([0,1])
        ax_box.set(yticks=[])
        ax_hist.set_xlabel(xlbl, fontsize = 18)
        ax_hist.set_ylabel('Density', fontsize = 18)
        ax_box.set_title(title, fontsize = 22)
        sns.despine(ax=ax_box, left=True)
        sns.despine(ax=ax_hist)
        plt.xticks(fontsize = 14)
        plt.yticks(fontsize = 14)
    
        if sf:
            plt.savefig(id+xlbl +'_histAndBox.png') 
        else:
            plt.show()
        plt.close()
    except:
        print(gsep)
        print("No 'seaborn' package detected, reverting to a simple histogram...")
        print("Please install the 'seaborn' package to use the '-a' feature flag!")
        makeHist(x, xlbl, title, id,sf)
    
def makeHist(x,xlbl,title, id = '', sf = False):
    plt.figure(figsize=(16,9))
    plt.hist(x,bins=25,normed=False, color= '#7777aa')
    plt.xlabel(xlbl, fontsize = 14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title(title, fontsize=16)
    if sf:
        plt.savefig(id+xlbl +'_histAndBox.png') #except no box
    else:
        plt.show()
    plt.close()
    
def boxplots(data, labels, title, xlbl, id = '', sf = False, yTickSize=[1,2,3], xMax = 1.05):
    # multiple box plots on one figure
    plt.figure(figsize=(16,9))
    bp = plt.boxplot(data,0,'', 0,whis=[0, 100], patch_artist=True)
    for box in bp['boxes']:
        # change outline color
        box.set( color='#000000', linewidth=2)
        # change fill color
        box.set( facecolor = '#7777aa' )
    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#000000', linewidth=2)
    
    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#000000', linewidth=2)
    
    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#000000', linewidth=2)
    
    plt.tick_params(axis='both', top='off')
    plt.xlabel(xlbl,fontsize=14)
    plt.xlim(-0.05,xMax)
    plt.title(title, fontsize=16)
    plt.yticks(yTickSize,labels, fontsize = 14 )
    if sf:
        plt.savefig(id+labels[0] + '_' + labels[1] + '_' + 'boxplots.png')
    else:
        plt.show()
    plt.close()
        
###################################
# end of graph building functions #
###################################

def buildGraphsLinks(hs, hasMet, hasTer, hasMtEval, hasBeer):
    linkHtml = [hs.graphHead]
    linkHtml.append('<p><a href="senBleuGraphs.html">Graphs for Sen Bleu Scores</a></p>\n')
    if hasMtEval:
        linkHtml.append('<p><a href="mtBleuGraphs.html">Graphs for MT Bleu Scores</a></p>\n')
        linkHtml.append('<p><a href="mtNistGraphs.html">Graphs for MT NIST Scores</a></p>\n')
    if hasMet:
        linkHtml.append('<p><a href="meteorGraphs.html">Graphs for METEOR Scores</a></p>\n')
    if hasBeer:
        linkHtml.append('<p><a href="beerGraphs.html">Graphs for BEER Scores</a></p>\n')
    if hasTer:
        linkHtml.append('<p><a href="terGraphs.html">Graphs for TER Scores</a></p>\n')
    linkHtml.append('<p><a href="werGraphs.html">Graphs for WER Scores</a></p>\n')
    linkHtml.append('<p><a href="editGraphs.html">Graphs for Edit Distance Scores</a></p>\n')
    #tmp line for testing
    linkHtml.append('<p><a href="../scorepages/graphs.html">General Graphs</a></p>\n')
    linkHtml.append(hs.sortFunc)
    return linkHtml

def scoreFullDivReplacements(nameA, hs):
    newDiv = hs.scoreTopRow.replace('alph',
                                   nameA + '_alphaHist.png').replace('boxy',
                                   nameA + '_boxplots.png').replace('scatty',
                                   nameA + '_Score_' + '_Score_scatter.png').replace('idhere', 
                                   nameA).replace('graphs',nameA).replace('histBox', nameA + '_histAndBox.png')
                                   
    newDiv = newDiv.replace('hb1',nameA).replace('hb2','xl'+nameA+'HB').replace('lrghb3',
                                'xl'+nameA+'HB').replace('lrghb4', 'xl'+nameA+'HB').replace('lrghb5', 
                                nameA).replace('lrghb6', nameA + '_histAndBox.png')
    ###
    newDiv = newDiv.replace('al1',nameA).replace('al2','xl'+nameA+'REF').replace('lrgREF',
                                'xl'+nameA+'REF').replace('lrgal4', 'xl'+nameA+'REF').replace('lrgal5', 
                                nameA)
                               
    newDiv = newDiv.replace('bx1',nameA).replace('bx2','xl'+nameA+'HYP').replace('lrgHYP',
                                'xl'+nameA+'HYP').replace('lrgbx4', 'xl'+nameA+'HYP').replace('lrgbx5', 
                                nameA)
                                
    newDiv = newDiv.replace('sc1',nameA).replace('sc2','xl'+nameA+'SRC').replace('lrgSRC',
                                'xl'+nameA+'SRC').replace('lrgsc4', 'xl'+nameA+'SRC').replace('lrgsc5', 
                                nameA)
    return newDiv
    
def generateTopScoreRow(scoreA, nameA, title, mainDir, hs, scoreLists, poly):
    sRowHtml = []
    #makeAlphaHist(x,y,xName, yName, xlbl, title, xLim = None, id = '', ylbl = 'Frequency', sf = False):
    titleHistBox = 'Showing the Distribution of {0} Scores'.format(nameA)
    makeHistAndBox(scoreA, titleHistBox, xlbl=nameA, id =mainDir+'/graphs/'+nameA+'/', sf = True) 
    
    #def makeScatter(x,y,xlbl, ylbl, title, xLim = None, id = '', sf = False, bestFit = False, ylim = None, poly = 3):
    titleScatter = 'A Scatter Plot Comparing the Sentence Level\n{0} Score with the Reference Sentence Length'.format(nameA)
    makeScatter(scoreA, scoreLists[0], nameA + '_Score', 'REF' + '_Length', titleScatter,  
                id=mainDir + '/graphs/'+nameA+'/', sf=True, poly = poly,xlim=(-0.002,1.002), picSize=(16,9)) 
    
    titleScatter = 'A Scatter Plot Comparing the Sentence Level\n{0} Score with the Hypothesis Sentence Length'.format(nameA)
    makeScatter(scoreA, scoreLists[1], nameA + '_Score', 'HYP' + '_Length', titleScatter,  
                id=mainDir + '/graphs/'+nameA+'/', sf=True, poly = poly,xlim=(-0.002,1.002), picSize=(16,9)) 
    
    titleScatter = 'A Scatter Plot Comparing the Sentence Level\n{0} Score with the Source Sentence Length'.format(nameA)
    makeScatter(scoreA, scoreLists[2], nameA + '_Score', 'SRC' + '_Length', titleScatter,  
                id=mainDir + '/graphs/'+nameA+'/', sf=True, poly = poly,xlim=(-0.002,1.002), picSize=(16,9)) 
                        
    sRowHtml.append(scoreFullDivReplacements(nameA, hs))
    
    return sRowHtml

def scoreDivReplacements(nameA, nameB, hs):
    newDiv = hs.graphTable.replace('alph',
                                   nameA + '_' + nameB + '_alphaHist.png').replace('boxy',
                                   nameA + '_' + nameB + '_boxplots.png').replace('scatty',
                                   nameA + '_Score_' + nameB + '_Score_scatter.png').replace('idhere', 
                                   nameA+nameB).replace('graphs',nameA)
    
    newDiv = newDiv.replace('al1',nameA+nameB).replace('al2','xl'+nameA+nameB+'AL').replace('lrgal3',
                                'xl'+nameA+nameB+'AL').replace('lrgal4', 'xl'+nameA+nameB+'AL').replace('lrgal5', 
                                nameA+nameB).replace('lrgal6', nameA + '_' + nameB + '_alphaHist.png')
                                
    newDiv = newDiv.replace('bx1',nameA+nameB).replace('bx2','xl'+nameA+nameB+'BX').replace('lrgbx3',
                                'xl'+nameA+nameB+'BX').replace('lrgbx4', 'xl'+nameA+nameB+'BX').replace('lrgbx5', 
                                nameA+nameB).replace('lrgbx6', nameA + '_' + nameB + '_boxplots.png')
                                
    newDiv = newDiv.replace('sc1',nameA+nameB).replace('sc2','xl'+nameA+nameB+'SC').replace('lrgsc3',
                                'xl'+nameA+nameB+'SC').replace('lrgsc4', 'xl'+nameA+nameB+'SC').replace('lrgsc5', 
                                nameA+nameB).replace('lrgsc6', nameA + '_Score_' + nameB + '_Score'+ '_scatter.png')
    return newDiv
    
def generateScoreRow(scoreA, scoreB, nameA, nameB, title, mainDir, hs, poly):
    sRowHtml = []
    #makeAlphaHist(x,y,xName, yName, xlbl, title, xLim = None, id = '', ylbl = 'Frequency', sf = False):
    titleAlpha = 'An Overlay Histogram Comparing the {0} and {1} Score Distributions'.format(nameA,nameB)
    makeAlphaHist(scoreA, scoreB, nameA, nameB, 'Score', titleAlpha, id=mainDir + '/graphs/'+nameA+'/',sf=True)  
    #def boxplots(data, labels, title, xlbl, id = '', sf = False, yTickSize): 
    titleBox = 'Boxplots Showing the Key Points of the {0} and {1} Score Distributions'.format(nameA,nameB)
    boxplots([scoreB, scoreA],[nameA, nameB], titleBox, 'Score', id=mainDir + '/graphs/'+nameA+'/', sf=True, yTickSize=[2,1]) 
    #def makeScatter(x,y,xlbl, ylbl, title, xLim = None, id = '', sf = False, bestFit = False, ylim = None, poly = 3):
    titleScatter = 'A Scatter Plot Comparing the {0} and {1}\nSentence Level Scores for Individual Sentences'.format(nameA,nameB)
    makeScatter(scoreA, scoreB, nameA + '_Score', nameB + '_Score', titleScatter,  
                id=mainDir + '/graphs/'+nameA+'/', sf=True, poly = poly,xlim=(-0.002,1.002),ylim=(-0.002,1.002))                     
    sRowHtml.append(scoreDivReplacements(nameA, nameB, hs))
    
    return sRowHtml
    
    
#lineTemplate = ['src','ref','hyp','senBleu','edScore','ed','senWer','goodMeas','refLen',
#'meteor', 'ter', 'mtBleu', 'mtNist'] 
    
# scoreLists = [refLengths,hypLengths,srcLengths, senBleus, edScores,editDists,
                 # wers,wergoods,meteorScores,ters,mtBleus,mtNists]
    
def buildGraphPageForScore(hs, scoreIdx, scoreLists, hasMet, hasTer, hasMtEval, hasBeer, mainDir, scoreName, combList, poly):
    global hasTerG, hasMetG, hasMtEvalG,  hasBeerG
    hasTerG = hasTer; hasMetG = hasMet; hasMtEvalG = hasMtEval; hasBeerG = hasBeer
    scoreHtml = [hs.graphHead]
    
    #combinations = {'Sen_Bleu':['MT_Bleu','MT_NIST','METEOR','TER','WER','E_Dist']}
    scoreHtml.append('<div style="text-align:center;"><p>{0} {1} Score Graphs {0}</p></div>'.format('~'*24,scoreName))
    scoreHtml+=generateTopScoreRow(scoreLists[scoreIdx],scoreName, '', mainDir,hs, scoreLists, poly)
    
    for idx, score in enumerate(combList):
        if score[0] == 'METEOR' and not hasMet:
            continue
        if score[0] == 'TER' and not hasTer:
            continue
        if score[0] == 'MT_Bleu' and not hasMtEval:
            continue
        if score[0] == 'MT_NIST' and not hasMtEval:
            continue
        if score[0] == 'BEER' and not hasBeer:
            continue
        #print(gsep)
        #print('Generating graphs for {0} and {1}...'.format(scoreName, score[0]))
        #titleAlpha = 'Comparing the distribution of {0} scores against the distribution of {1} scores'.format(scoreName,score[0])
        newRow = generateScoreRow(scoreLists[scoreIdx],scoreLists[score[1]],scoreName, score[0], '', mainDir,hs,poly)
        '''
        #print('Generating boxplots for {0} and {1}...'.format(scoreName, score[0]))
        titleBox = 'Boxplots showing the distribution of {0} and {1} scores'.format(scoreName,score[0])
        generateScoreRow(scoreLists[scoreIdx],scoreLists[score[1]],scoreName, score[0], titleBox, mainDir,hs)
        
        #print('Generating scatter plots for {0} and {1}...'.format(scoreName, score[0]))
        titleScatter = 'Correlation between {0} scores and {1} scores'.format(scoreName,score[0])
        generateScoreRow(scoreLists[scoreIdx],scoreLists[score[1]],scoreName, score[0], titleScatter, mainDir,hs)
        '''
        scoreHtml.append('<div style="text-align:center;"><p>{0} {1} and {2} {0}</p></div>'.format('~'*24,scoreName,score[0]))
        scoreHtml += newRow
        
    scoreHtml.append(hs.sortFunc)
    return scoreHtml

    
def buildGraphPages(allStatsDict, hs, rw, mainDir, hasMet, hasTer, hasMtEval, hasBeer, gm, poly = False):
    rw.writeFile(buildGraphsLinks(hs, hasMet, hasTer, hasMtEval, hasBeer), mainDir + '/graphs/graphLinks.html')
        
    refLengths = []
    hypLengths = []
    srcLengths = []
    
    senBleus = []
    edScores = []
    editDists =[]
    wers = []
    wergoods = []
    meteorScores = []
    beerScores = []
    ters = []
    mtBleus = []
    mtNists = []
    
    if poly:
        poly = 1
    else:
        poly = 3
    
    processed = 0
    for k in allStatsDict.keys():
        for idx, el in enumerate(allStatsDict[k]):
            refLengths.append(el[8])
            hypLengths.append(len(el[2].split()))
            srcLengths.append(len(el[0].split()))
            
            senBleus.append(el[3])
            edScores.append(el[4])
            editDists.append(el[5])
            wers.append(el[6])
            wergoods.append(el[7])
            meteorScores.append(el[9])
            ters.append(el[10])
            mtBleus.append(el[11])
            mtNists.append(el[13])
            beerScores.append(el[14])
            
            processed += 1
            if processed%200 == 0:
                print('Processed {0} lines for drawing graphs'.format(processed))
    print('~'*64)           
    scoreLists = [refLengths,hypLengths,srcLengths, senBleus, edScores,editDists,
                  wers,wergoods,meteorScores,ters,mtBleus,mtNists,beerScores]
    
    combinations = {'Sen_Bleu':[('MT_Bleu',10),('MT_NIST',11),('METEOR',8),('BEER',12),('TER',9),('WER',7),('Edit_Dist',4)],
                    'MT_Bleu':[('Sen_Bleu',3),('MT_NIST',11),('METEOR',8),('BEER',12),('TER',9),('WER',7),('Edit_Dist',4)],
                    'MT_NIST':[('Sen_Bleu',3),('MT_Bleu',10),('METEOR',8),('BEER',12),('TER',9),('WER',7),('Edit_Dist',4)],
                    'METEOR':[('Sen_Bleu',3),('MT_Bleu',10),('MT_NIST',11),('BEER',12),('TER',9),('WER',7),('Edit_Dist',4)],
                    'BEER':[('Sen_Bleu',3),('MT_Bleu',10),('MT_NIST',11),('METEOR',8),('TER',9),('WER',7),('Edit_Dist',4)],
                    'TER':[('Sen_Bleu',3),('MT_Bleu',10),('MT_NIST',11),('METEOR',8),('BEER',12),('WER',7),('Edit_Dist',4)],
                    'WER':[('Sen_Bleu',3),('MT_Bleu',10),('MT_NIST',11),('METEOR',8),('BEER',12),('TER',9),('Edit_Dist',4)],
                    'Edit_Dist':[('Sen_Bleu',3),('MT_Bleu',10),('MT_NIST',11),('METEOR',8),('BEER',12),('TER',9),('WER',7)],
                    }
                   
    

    def f(name, idx,dirAffix):
        print ('Building the {0} graphs, please wait...'.format(name))
        
        rw.writeFile(buildGraphPageForScore(hs, idx, scoreLists, hasMet, hasTer, hasMtEval, hasBeer, mainDir, name, combinations[name], poly),
                 mainDir + '/graphs/'+dirAffix)
        print(gsep)
        print ('Finished the {0} graphs...'.format(name))
        
    def doGraphs():
        
        print('Drawing graphs in a single thread...')
        
        f('Sen_Bleu',3,'senBleuGraphs.html')
    
        if hasMtEval:
            f('MT_Bleu',10,'mtBleuGraphs.html')
            f('MT_NIST',11,'mtNistGraphs.html')
        if hasMet:
            f('METEOR',8,'meteorGraphs.html')
        if hasTer:
            f('TER',9,'terGraphs.html')
        
        if hasBeer:
            f('BEER',12,'beerGraphs.html')
            
        f('WER',7,'werGraphs.html')
        
        f('Edit_Dist',4,'editGraphs.html')
        
    try:
        print('Trying Multiprocessing... please wait...')
        
        from multiprocessing import Process
           
        sb = Process(target=f, args=('Sen_Bleu',3,'senBleuGraphs.html',)); sb.start()
        
        if hasMtEval:
            mb = Process(target=f, args=('MT_Bleu',10,'mtBleuGraphs.html',)); mb.start()
            mn = Process(target=f, args=('MT_NIST',11,'mtNistGraphs.html',)); mn.start()
        if hasMet:
            m = Process(target=f, args=('METEOR',8,'meteorGraphs.html',)); m.start()
        if hasTer:
            t = Process(target=f, args=('TER',9,'terGraphs.html',)); t.start()
        
        if hasBeer:
            b = Process(target=f, args=('BEER',12,'beerGraphs.html',)); b.start()
            
        w = Process(target=f, args=('WER',7,'werGraphs.html',)); w.start()
        
        ed = Process(target=f, args=('Edit_Dist',4,'editGraphs.html',)); ed.start()
        
        sb.join()
        if hasMtEval:
            mb.join(); mn.join()
        if hasMet:
            m.join()
        if hasTer:
            t.join()
        if hasBeer:
            b.join()
        w.join()
        ed.join()
    except Exception as e:
        print('General exception...')
        print(type(e))
        print(e)
        print('~'*64)
        print('There was a problem with multiprocessing, reverting back to a single thread...')
    
        doGraphs()
        
    
    '''     
    rw.writeFile(buildGraphPageForScore(hs, 3, scoreLists, hasMet, hasTer, hasMtEval, mainDir, 'Sen_Bleu', combinations['Sen_Bleu']),
                 mainDir + '/graphs/senBleuGraphs.html')
    
    rw.writeFile(buildGraphPageForScore(hs, 10, scoreLists, hasMet, hasTer, hasMtEval, mainDir, 'MT_Bleu', combinations['MT_Bleu']),
                 mainDir + '/graphs/mtBleuGraphs.html')'''
    
    