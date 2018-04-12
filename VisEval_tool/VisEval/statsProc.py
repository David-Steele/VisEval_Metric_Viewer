# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:48:46 2017
@author: david
"""

#create stats page for the whole data set

sep = '~'*88

def getTerScores(rw):
    terLine = rw.readFile('tr.sum')
    terLine = terLine[-1]
    tmpLine = terLine.split('|')
    terScore = float(tmpLine[-1].strip())/100.0
    
    return terLine, terScore
    
def getMeteorScores(rw):
    metList = rw.readFile('vb_METEOR_output.txt')
    metInfo = metList[-11:]
    metInfo[0] = '<b>METEOR Information...</b>'
    metS = '<br>'.join(metInfo)
    return metS

def getBeerScores(rw):
    beerList = rw.readFile('vb_BEER_output.txt')
    beerScore = beerList[-1].replace('total BEER ','Total BEER = ')
    beerInfo = ['<b>BEER Information...</b>']
    beerInfo.append(beerScore)
    beerS = '<br>'.join(beerInfo)
    return beerS
'''    
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>
'''    
def createMtEvalTable(lineList, header = 'Individual N-gram Scoring:'):
    tableHtml = ['\n<table>\n']
    cols = None
    nextScore = True
    for line in lineList:
        if '1-gram' in line:
            s = 'Metric ' + line
            tmpS = s.split()
            cols = (len(tmpS))
            if nextScore:
                tableHtml.append('<tr><td colspan="{0}">Individual N-gram Scoring:</td></tr>\n'.format(cols))
            tableHtml.append('<tr>\n')
            for el in tmpS:
                tableHtml.append('<td style="padding:0 12px 0 12px;"><b>{0}</b></td>\n'.format(el))
            tableHtml.append('</tr>\n')
        elif 'NIST:' in line:
            tmpS = line.split()
            tableHtml.append('<tr>\n')
            for el in tmpS[:-1]:
                tableHtml.append('<td style="padding:0 12px 0 12px;"><b>{0}</b></td>\n'.format(el))
            tableHtml.append('</tr>\n')
        elif 'BLEU:' in line:
            tmpS = line.split()
            tableHtml.append('<tr>\n')
            for el in tmpS[:-1]:
                tableHtml.append('<td style="padding:0 12px 0 12px;"><b>{0}</b></td>\n'.format(el))
            tableHtml.append('</tr>\n')
            if nextScore:
                tableHtml.append('<tr><td colspan="{0}">Cumulative N-gram Scoring:</td></tr>\n'.format(cols))
                nextScore = False
    tableHtml.append('</table>\n')
    return ''.join(tableHtml)
    

def getMtEvalInfo(rw):
    tmpMt = rw.readFile('mtEvalStats.txt')
    returnMt = [tmpMt[0] + '<br>']
    for line in tmpMt:
        if 'NIST score' and 'BLEU score' in line:
            returnMt.append(line)
    #returnMt.append(tmpMt[-1])
    s = '<br>'.join(returnMt)
    s = s.replace('NIST','<b> MT NIST</b>').replace('=','=<b>').replace('BLEU',
            '</b><br><b> MT BLEU</b>').replace('for system','</b><br>for system')
    s += createMtEvalTable(tmpMt)
    s += '<br>' + tmpMt[-1] 
    return s
    
def buildPage(src, ref, hyp, rw, cBleu, wer, hs, maindir,
              edDist, hasTer = False, hasMtEval = False, hasMet = False, hasBeer = False):
    htmlList = [hs.head]
    srcSum = 0; refSum = 0; hypSum = 0;
    srcAvg = None; refAvg = None; hypAvg = None;
    
    terLine = 'N/A'; terScore = 'N/A'; mtEvalInfo = 'N/A'
    
    srcSet = set(); refSet = set(); hypSet = set()
    
    for idx, line in enumerate(src):
        tmpsrc = line.split()
        srcSum += len(tmpsrc)
        for wrd in tmpsrc:
            srcSet.add(wrd)
        
        tmpref = ref[idx].split()
        refSum += len(tmpref)
        for wrd in tmpref:
            refSet.add(wrd)
        
        tmphyp = hyp[idx].split()
        hypSum += len(tmphyp)
        for wrd in tmphyp:
            hypSet.add(wrd)
    
    srcAvg = (srcSum * 1.0)/len(src)
    refAvg = (refSum * 1.0)/len(ref)
    hypAvg = (hypSum * 1.0)/len(hyp)
    
    print('Building Stats Page')
    print(srcAvg, refAvg, hypAvg)
    print(len(srcSet), len(refSet), len(hypSet))
    print('~'*64)
    
    
    htmlList.append("<h2>General Statistics for the Dataset as a Whole</h2><h4>(See individual file folders for more details)</h4>\n")
    htmlList.append(sep + '\n')
    htmlList.append("<p>The number of sentences in each of the dataset files is: {0}</p>\n".format(len(ref)))
    
    htmlList.append("<p>The <b>SRC</b> file contains a total of {0} words and {1} unique words.".format(srcSum,len(srcSet)))
    htmlList.append(" It has an average of {0} words per sentence.</p>\n".format(srcAvg))
    
    htmlList.append("<p>The <b>REF</b> file contains a total of {0} words and {1} unique words.".format(refSum,len(refSet)))
    htmlList.append(" It has an average of {0} words per sentence.</p>\n".format(refAvg))
    
    htmlList.append("<p>The <b>HYP</b> file contains a total of {0} words and {1} unique words.".format(hypSum,len(hypSet)))
    htmlList.append(" It has an average of {0} words per sentence.</p>\n{1}\n".format(hypAvg, sep))
    
    htmlList.append("<p>The standard <b>BLEU</b> score for the whole dataset is: <b>{0}</b><br>\n".format(cBleu))
    htmlList.append("The average <b>Edit Distance</b> score for the whole dataset is: <b>{0}</b><br>\n".format("{0:.4f}".format(edDist/len(ref))))
    htmlList.append("The average <b>WER</b> per sentence is: <b>{0}</b><br>\n".format("{0:.4f}".format(wer[2])))
    htmlList.append("The <b>WER</b> score for the whole dataset is: <b>{0}</b><br>\n".format("{0:.4f}".format(wer[3]/100.0)))
    
    if hasTer:
        terLine, terScore = getTerScores(rw)
        htmlList.append("The <b>TER</b> score for the whole dataset is: <b>{0}</b></p>\n{1}\n".format("{0:.4f}".format(terScore), sep))
    else:
        htmlList.append('</p>{0}\n'.format(sep))
    
    if hasMtEval:
        mtEvalInfo = getMtEvalInfo(rw)
        htmlList.append("<p>{0}</p>\n{1}\n".format(mtEvalInfo,sep))
        
    if hasMet:
        metSen = getMeteorScores(rw)
        htmlList.append('<p>{0}</p>{1}'.format(metSen, sep))
    if hasBeer:
        beerSen = getBeerScores(rw)
        htmlList.append('<p>{0}</p>{1}'.format(beerSen, sep))
    
    htmlList.append(hs.sortFunc)
    rw.writeFile(htmlList, maindir + '/dataSetStats.html')
    return {'SRC Words\n(total)':srcSum, 'SRC Unique\nWords':len(srcSet),
            'REF Words\n(total)':refSum, 'REF Unique\nWords':len(refSet),
            'HYP Vocab\n(total)':hypSum, 'HYP Unique\nWords':len(hypSet)}