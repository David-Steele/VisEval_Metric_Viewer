# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:18:38 2017
@author: david
"""
import matplotlib.pyplot as plt
import numpy as np
gsep = '~'*64

def makeScatter(x,y,xlbl, ylbl, title, xLim = None, id = '', sf = False, bestFit = False, ylim = None, poly = 3):
    plt.figure(figsize=(16,9))
    plt.scatter(x,y)#, color= '#7777aa')
    plt.xlabel(xlbl,fontsize=14)
    plt.ylabel(ylbl,fontsize=14)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, poly))(np.unique(x)), '-r', linewidth=3)
    if xLim:
        plt.xlim(xLim)
    if ylim:
        plt.ylim(ymin=0)
    plt.title(title,fontsize=16)
    if sf:
        plt.savefig(id+'scatter.png')
    else:
        plt.show()

def makeAlphaHist(x,y,xName, yName, xlbl, title, xLim = None, id = '', ylbl = 'Frequency', sf = False):
    plt.figure(figsize=(16,9))    
    bins = 25
    val = 0
    binVals = []
    for i in range (bins):
        binVals.append(val)
        val += 1/bins
    if binVals[-1] < 1:
        binVals.append(1.0)
        
    (bn, bbins, bpatches) = plt.hist(x,bins=binVals, alpha = 0.5,label=xName);
    (tn, tbins, tpatches) = plt.hist(y, bins=binVals, alpha = 0.5, label=yName);
    plt.legend()
    plt.title(title, fontsize = 16)
    plt.xlabel(xlbl, fontsize = 14)
    plt.ylabel(ylbl, fontsize = 14)
    
    if sf:
        plt.savefig(id+'alphaHist.png')
    else:
        plt.show()
    
def makeHistAndBox(x, title, xlbl='', id = '', sf = False):
    try:
        import seaborn as sns
        sns.set(style="ticks")
        
        fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, figsize=(16,9), 
              gridspec_kw={"height_ratios": (.12, .88)})
        sns.distplot(x, ax=ax_hist)
        sns.boxplot(x, ax=ax_box, whis=[0,100])
        
        plt.xlim([0,1])
        ax_box.set(yticks=[])
        ax_hist.set_xlabel(xlbl, fontsize = 14)
        ax_hist.set_ylabel('Density', fontsize = 14)
        ax_box.set_title(title, fontsize = 16)
        sns.despine(ax=ax_box, left=True)
        sns.despine(ax=ax_hist)
    
        if sf:
            plt.savefig(id+'histAndBox.png')
        else:
            plt.show()
    except:
        print(gsep)
        print("No 'seaborn' package detected, reverting to a simple histogram...")
        print("Please install the 'seaborn' package to use the '-a' feature flag!")
        makeHist(x, xlbl, title, id,sf)
    
def makeHist(x,xlbl,title, id = '', sf = False):
    plt.figure(figsize=(16,9))
    plt.hist(x,bins=50,normed=False, color= '#7777aa')
    plt.xlabel(xlbl, fontsize = 14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title(title, fontsize=16)
    if sf:
        plt.savefig(id+'histAndBox.png') #except no box
    else:
        plt.show()
    
def boxplots(data, labels, title, xlbl, id = '', sf = False):
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
    plt.title(title, fontsize=16)
    plt.yticks([1,2,3],labels, fontsize = 14 )
    if sf:
        plt.savefig(id+'boxplots.png')
    else:
        plt.show()

def barChart(barDict, id, sf=False):    
    vals = []
    keys = sorted(barDict.keys(), reverse = True)
    #sorted(keys)
    
    for k in keys:
        vals.append(barDict[k])
    y_pos = np.arange(len(vals))
    plt.figure(figsize=(16,9))
    plt.bar(y_pos, vals, align='center', alpha=0.5, color=['red', 'red', 'green', 'green', 'blue', 'blue'])
    plt.xticks(y_pos, keys, fontsize=18)
    plt.ylabel('Number of Words', fontsize=18)
    plt.title('Showing the Total Vocabulary Sizes and Number of\nUnique Words for the SRC, REF, and HYP Files Respectively', fontsize=22)
    for i,j in zip(y_pos,vals):
        plt.annotate(str(vals[i]),xy=(i,j), xytext=(i-0.12, vals[i] + 24), fontsize=18)
    if sf:
        plt.savefig(id+'barplot.png')
    else:
        plt.show()
    

#lineTemplate = ['src','ref','hyp','senBleu','edScore','ed','senWer','goodMeas','refLen',
                #'meteor', 'ter', 'mtBleu', 'mtNist']
def makeGraphs(bleuDict,imgDir, adv, poly, bars, hasMet = False):
    refLengths = []
    hypLengths = []
    srcLengths = []
    
    wers = []
    goods = []
    senBleus = []
    metScores = []
    
    if poly:
        poly = 1
    else:
        poly = 3
    
    processed = 0
    for k in bleuDict.keys():
        for idx, el in enumerate(bleuDict[k]):
            refLengths.append(el[8])
            hypLengths.append(len(el[2].split()))
            srcLengths.append(len(el[0].split()))
            wers.append(el[6])
            goods.append(el[7])
            senBleus.append(el[3])
            if hasMet:
                metScores.append(float(el[9]))
                
            
            processed += 1
            if processed%200 == 0:
                print('Processed {0} lines for drawing graphs'.format(processed))
    
    barChart(bars, imgDir, True)
       
    makeScatter(refLengths, hypLengths, 'Reference Sentence Length',
                'Hypothesis Sentence Length',
                'Showing the Correlation Between the Reference and Hypothesis Sentence Lengths', False,
                imgDir+'hyp_v_ref_', sf = True, bestFit=False, ylim=True, poly = poly)
    
    makeScatter(refLengths, srcLengths, 'Reference Sentence Length',
                'Source Sentence Length',
                'Showing the Correlation Between the Reference and Source Sentence Lengths', False,
                imgDir+'src_v_ref_', sf = True, bestFit=False, ylim=True, poly = poly)
    
    makeScatter(hypLengths, srcLengths, 'Hypothesis Sentence Length',
                'Source Sentence Length',
                'Showing the Correlation Between the Hypothesis and Source Sentence Lengths', False,
                imgDir+'src_v_hyp_', sf = True, bestFit=False, ylim=True, poly = poly)
    '''           
    makeScatter(refLengths, srcLengths, 'Reference Sentence Length',
                'Source Sentences Length',
                'Correlation Between the Relative Reference and Source Sentence Lengths')
    
    makeScatter(hypLengths, srcLengths, 'Hypothesis Sentence Length',
                'Source Sentences Length',
                'Correlation Between the Relative Hypothesis and Source Sentence Lengths')
    

    makeScatter(senBleus, refLengths, 'Bleu Score Per-sentence', 'Reference Sentence Length',
                'Correlation Between Sentence Level Bleu Scores and (REF) Sentence Length',[0,1.05],
                imgDir+'bleu_v_ref_', sf = True, bestFit = True, ylim=True, poly = poly)
                
    makeScatter(senBleus, srcLengths, 'Bleu Score Per-sentence', 'Source Sentence Length',
                'Correlation Between Sentence Level Bleu Scores and (SRC) Sentence Length',[0,1.05],
                imgDir+'bleu_v_src_', sf = True, bestFit = True, ylim=True, poly = poly)
                
    makeScatter(senBleus, hypLengths, 'Bleu Score Per-sentence', 'Hypothesis Sentence Length',
                'Correlation Between Sentence Level Bleu Scores and (HYP) Sentence Length',[0,1.05],
                imgDir+'bleu_v_hyp_', sf = True, bestFit = True, ylim=True, poly = poly)
    
    makeScatter(senBleus, wers, 'Bleu Score Per-sentence',
                'WER Per-sentence',
                'Correlation Between the Sentence Bleu Scores and the Respective WER', [0,1.05],
                imgDir+'bleu_v_wer_', sf = True, bestFit = True, ylim = True, poly = poly)
    
    makeScatter(senBleus, goods, 'Bleu Score Per-sentence',
                'WER Goodness Score Per-sentence',
                'Correlation Between the Relative Sentence Bleu Scores and the Respective WER Goodness Score', [0,1.05],
                imgDir+'bleu_v_werGood_', sf = True, bestFit = True, ylim = False, poly = poly)
    if hasMet:
        makeScatter(senBleus, metScores, 'Bleu Score Per-sentence',
                'METEOR Score Per-sentence',
                'Correlation Between the Relative Sentence Bleu Scores and the Respective METEOR Score', [0,1.05],
                imgDir+'bleu_v_meteor_', sf = True, bestFit = True, ylim = False, poly = poly)
        
        if adv:
            makeHistAndBox(metScores,'Showing the Distribution of Sentence Level Meteor Scores',
                       'Sentence Level Meteor Score', imgDir + '/hasMet_', sf = True)
        else:
           makeHist(metScores, 'Sentence Level Meteor Score',
           'Showing the Distribution of Sentence Level Meteor Scores', imgDir + '/hasMet_',sf = True)
    
    #makeHist(senBleus, 'Sentence Level Bleu Score','Showing the Distribution of Sentence Level Bleu Scores')
    
    #makeHist(wers, 'Sentence Level WER Goodness Score','Showing the Distribution of Sentence Level WER Goodness Scores')
    
    if adv:
        makeHistAndBox(senBleus,'Showing the Distribution of Sentence Level Bleu Scores',
                   'Sentence Level Bleu Score', imgDir,sf = True)
    else:
       makeHist(senBleus, 'Sentence Level Bleu Score',
       'Showing the Distribution of Sentence Level Bleu Scores', imgDir,sf = True) 
    '''
    boxplots([hypLengths, refLengths,srcLengths], ['HYP','REF','SRC'],
             'Boxplots showing the Distribution of Sentence Lengths for SRC, REF, and HYP Respectively',
             'Sentence Length', imgDir, sf = True,)
    
    #makeAlphaHist(x,y,xName, yName, xlbl, ylbl, title, xLim = None, id = '', sf = False):
    #alpTite = 'Comparing the distribution of Sen Bleu scores against the distribution of WER scores'
    #makeAlphaHist(senBleus, goods, xName = 'Sen Bleu', yName = 'WER Score', xlbl = 'Score',title=alpTite, id = imgDir, sf=True )
             
def makeGraphsOld(bleuDict,imgDir, adv, poly, hasMet = False):
    refLengths = []
    hypLengths = []
    srcLengths = []
    
    wers = []
    goods = []
    senBleus = []
    metScores = []
    
    if poly:
        poly = 1
    else:
        poly = 3
    
    processed = 0
    for i,k in enumerate(bleuDict):
        for idx, el in enumerate(bleuDict[k]):
            refLengths.append(el[2])
            hypLengths.append(len(el[1].split()))
            srcLengths.append(len(el[6].split()))
            wers.append(el[3])
            goods.append(el[5])
            senBleus.append(el[-1])
            if hasMet:
                metScores.append(float(el[7]))
                
            
            processed += 1
            if processed%100 == 0:
                print('Processed {0} lines for drawing graphs'.format(processed))
            
    makeScatter(refLengths, hypLengths, 'Reference Sentence Length',
                'Hypothesis Sentences Length',
                'Correlation Between the Relative Reference and Hypothesis Sentence Lengths', False,
                imgDir+'hyp_v_ref_', sf = True, bestFit=False, ylim=True, poly = poly)
    '''           
    makeScatter(refLengths, srcLengths, 'Reference Sentence Length',
                'Source Sentences Length',
                'Correlation Between the Relative Reference and Source Sentence Lengths')
    
    makeScatter(hypLengths, srcLengths, 'Hypothesis Sentence Length',
                'Source Sentences Length',
                'Correlation Between the Relative Hypothesis and Source Sentence Lengths')
    ''' 

    makeScatter(senBleus, refLengths, 'Bleu Score Per-sentence', 'Reference Sentence Length',
                'Correlation Between Sentence Level Bleu Scores and (REF) Sentence Length',[0,1.05],
                imgDir+'bleu_v_ref_', sf = True, bestFit = True, ylim=True, poly = poly)
                
    makeScatter(senBleus, srcLengths, 'Bleu Score Per-sentence', 'Source Sentence Length',
                'Correlation Between Sentence Level Bleu Scores and (SRC) Sentence Length',[0,1.05],
                imgDir+'bleu_v_src_', sf = True, bestFit = True, ylim=True, poly = poly)
                
    makeScatter(senBleus, hypLengths, 'Bleu Score Per-sentence', 'Hypothesis Sentence Length',
                'Correlation Between Sentence Level Bleu Scores and (HYP) Sentence Length',[0,1.05],
                imgDir+'bleu_v_hyp_', sf = True, bestFit = True, ylim=True, poly = poly)
    
    makeScatter(senBleus, wers, 'Bleu Score Per-sentence',
                'WER Per-sentence',
                'Correlation Between the Sentence Bleu Scores and the Respective WER', [0,1.05],
                imgDir+'bleu_v_wer_', sf = True, bestFit = True, ylim = True, poly = poly)
    
    makeScatter(senBleus, goods, 'Bleu Score Per-sentence',
                'WER Goodness Score Per-sentence',
                'Correlation Between the Relative Sentence Bleu Scores and the Respective WER Goodness Score', [0,1.05],
                imgDir+'bleu_v_werGood_', sf = True, bestFit = True, ylim = False, poly = poly)
    if hasMet:
        makeScatter(senBleus, metScores, 'Bleu Score Per-sentence',
                'METEOR Score Per-sentence',
                'Correlation Between the Relative Sentence Bleu Scores and the Respective METEOR Score', [0,1.05],
                imgDir+'bleu_v_meteor_', sf = True, bestFit = True, ylim = False, poly = poly)
        
        if adv:
            makeHistAndBox(metScores,'Showing the Distribution of Sentence Level Meteor Scores',
                       'Sentence Level Meteor Score', imgDir + '/hasMet_', sf = True)
        else:
           makeHist(metScores, 'Sentence Level Meteor Score',
           'Showing the Distribution of Sentence Level Meteor Scores', imgDir + '/hasMet_',sf = True)
    
    #makeHist(senBleus, 'Sentence Level Bleu Score','Showing the Distribution of Sentence Level Bleu Scores')
    
    #makeHist(wers, 'Sentence Level WER Goodness Score','Showing the Distribution of Sentence Level WER Goodness Scores')
    
    if adv:
        makeHistAndBox(senBleus,'Showing the Distribution of Sentence Level Bleu Scores',
                   'Sentence Level Bleu Score', imgDir,sf = True)
    else:
       makeHist(senBleus, 'Sentence Level Bleu Score',
       'Showing the Distribution of Sentence Level Bleu Scores', imgDir,sf = True) 
    
    boxplots([hypLengths, refLengths,srcLengths], ['HYP','REF','SRC'],
             'Boxplots showing the Distribution of Sentence Lengths for SRC, REF, and HYP Respectively',
             'Sentence Length', imgDir, sf = True,)
    
    