# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:13:09 2017
@author: david
"""

#make the score pages with a sortable table

#lineTemplate = ['src','ref','hyp',
                    #'senBleu','edScore','ed','senWer','goodMeas',
                    #'refLen', #'meteor', 'ter', 'mtBleu', 'mtNist', mtNormedNist, 'beer' 'pos']
sep = "~"*88



    
dictDivSwap = {'stPos':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],'stPosRev':[1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                'stSen':[2,3,0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],'stSenRev':[3,2,0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                'stBleu':[4,5,2,3,0,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],'stBleuRev':[5,4,2,3,0,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                'stWer':[6,7,2,3,4,5,0,1,8,9,10,11,12,13,14,15,16,17,18,19,20,21], 'stWerRev':[7,6,2,3,4,5,0,1,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                'stEd':[8,9,6,7,2,3,4,5,0,1,10,11,12,13,14,15,16,17,18,19,20,21], 'stEdRev':[9,8,6,7,2,3,4,5,0,1,10,11,12,13,14,15,16,17,18,19,20,21],
                'stTer':[10,11,6,7,2,3,4,5,0,1,8,9,12,13,14,15,16,17,18,19,20,21], 'stTerRev':[11,10,6,7,2,3,4,5,0,1,8,9,12,13,14,15,16,17,18,19,20,21],
                'stMet':[12,13,10,11,6,7,2,3,4,5,0,1,8,9,14,15,16,17,18,19,20,21], 'stMetRev':[13,12,10,11,6,7,2,3,4,5,0,1,8,9,14,15,16,17,18,19,20,21],
                'stMtBleu':[14,15,10,11,6,7,2,3,4,5,0,1,8,9,12,13,16,17,18,19,20,21], 'stMtBleuRev':[15,14,11,10,6,7,2,3,4,5,0,1,8,9,12,13,16,17,18,19,20,21],
                'stMtNist':[16,17,12,13,10,11,6,7,2,3,4,5,0,1,8,9,14,15,18,19,20,21], 'stMtNistRev':[17,16,13,12,10,11,6,7,2,3,4,5,0,1,8,9,14,15,18,19,20,21],
                'stRef':[18,19,16,17,12,13,10,11,6,7,2,3,4,5,0,1,8,9,14,15,20,21], 'stRefRev':[19,18,17,16,13,12,10,11,6,7,2,3,4,5,0,1,8,9,14,15,20,21],
                'stBeer':[20,21,18,19,16,17,12,13,10,11,6,7,2,3,4,5,0,1,8,9,14,15], 'stBeerRev':[21,20,19,18,17,16,13,12,10,11,6,7,2,3,4,5,0,1,8,9,14,15]
              }

def getParamList(divName, sortedLines):
    divArray = dictDivSwap[divName]
    s=''
    for el in divArray: 
        s += ",\'{0}\'".format(   sortedLines[el][1])  
    return s[1:]

def createCheckBoxes(hasMet, hasTer, hasMtEval, hasBeer):
    
    checkBoxDiv = ['<div id="chboxes">\n']
    checkBoxDiv.append('<input type="checkbox" name="POS" checked />POS\n')
    checkBoxDiv.append('<input type="checkbox" name="REF" checked />REF Length\n')
    checkBoxDiv.append('<input type="checkbox" name="Sentence" checked />Sentence\n')
    checkBoxDiv.append('<input type="checkbox" name="SentenceBleu" checked />Sen Bleu\n')
    if hasMtEval:
        checkBoxDiv.append('<input type="checkbox" name="mtBleu" checked />MT Bleu\n')
        checkBoxDiv.append('<input type="checkbox" name="mtNist" checked />MT Nist\n')
    if hasMet:
        checkBoxDiv.append('<input type="checkbox" name="MET" checked />METEOR\n')
    if hasBeer:
        checkBoxDiv.append('<input type="checkbox" name="BEER" checked />BEER\n')
    if hasTer:
        checkBoxDiv.append('<input type="checkbox" name="TER" checked />TER\n')
    checkBoxDiv.append('<input type="checkbox" name="WER" checked />WER\n')
    checkBoxDiv.append('<input type="checkbox" name="ed" checked />Edit Dist\n')
    checkBoxDiv.append('</div>\n')

    return checkBoxDiv                   
    
def makeScoreTables(stLine, hs, itemgetter, hasMet, hasTer, hasMtEval, hasBeer):
    stPos = stLine
    stPosRev = sorted(stLine, key = itemgetter(15), reverse = True)
    stRef = sorted(stLine, key = itemgetter(8), reverse = True)
    stRefRev = sorted(stLine, key = itemgetter(8), reverse = False)
    stSen = sorted(stLine, key = itemgetter(1), reverse = False)
    stSenRev = sorted(stLine, key = itemgetter(1), reverse = True)
    stBleu = sorted(stLine, key = itemgetter(3), reverse = False)
    stBleuRev = sorted(stLine, key = itemgetter(3), reverse = True)
    stWer = sorted(stLine, key = itemgetter(7), reverse = False)
    stWerRev = sorted(stLine, key = itemgetter(7), reverse = True)
    stEd = sorted(stLine, key = itemgetter(4), reverse = False)
    stEdRev = sorted(stLine, key = itemgetter(4), reverse = True)
    
    sortedLines = [(stPos, 'stPos'), (stPosRev, 'stPosRev'), (stSen, 'stSen'),
                   (stSenRev, 'stSenRev'), (stBleu, 'stBleu'), (stBleuRev, 'stBleuRev'),
                   (stWer, 'stWer'), (stWerRev, 'stWerRev'), (stEd, 'stEd'), (stEdRev, 'stEdRev')]
                   
    stTer = sorted(stLine, key = itemgetter(10), reverse = False)
    stTerRev = sorted(stLine, key = itemgetter(10), reverse = True)
    sortedLines.append((stTer, 'stTer')); sortedLines.append((stTerRev, 'stTerRev'))
    
    stMet = sorted(stLine, key = itemgetter(9), reverse = False)
    stMetRev = sorted(stLine, key = itemgetter(9), reverse = True)
    sortedLines.append((stMet, 'stMet')); sortedLines.append((stMetRev, 'stMetRev'))
    
    stMtBleu = sorted(stLine, key = itemgetter(11), reverse = False)
    stMtBleuRev = sorted(stLine, key = itemgetter(11), reverse = True)
    sortedLines.append((stMtBleu, 'stMtBleu')); sortedLines.append((stMtBleuRev, 'stMtBleuRev'))
    
    stMtNist = sorted(stLine, key = itemgetter(12), reverse = False)
    stMtNistRev = sorted(stLine, key = itemgetter(12), reverse = True)
    sortedLines.append((stMtNist, 'stMtNist')); sortedLines.append((stMtNistRev, 'stMtNistRev'))
    
    sortedLines.append((stRef, 'stRef')); sortedLines.append((stRefRev, 'stRefRev'))
    
    stBeer = sorted(stLine, key = itemgetter(14), reverse = False)
    stBeerRev = sorted(stLine, key = itemgetter(14), reverse = True)
    sortedLines.append((stBeer, 'stBeer')); sortedLines.append((stBeerRev, 'stBeerRev'))
    
    htmlList = []
    htmlList.append(hs.scorepagesHead)
    htmlList += (createCheckBoxes(hasMet, hasTer, hasMtEval, hasBeer))
    for idx, tup in enumerate(sortedLines):
        disp = 'block'
        if idx > 0:
            disp = 'none'
        htmlList.append('<div id="{0}" style="display:{1};">'.format(tup[1], disp))
        htmlList.append('\n<table id="myTable">\n<thead>\n')
        htmlList.append('   <tr>\n')
        htmlList.append('      <th class="POS" onclick="sortTable({0})">POS</th>\n'.format(getParamList('stPos', sortedLines)))
        htmlList.append('      <th class="REF" onclick="sortTable({0})">REF<br>Length</th>\n'.format(getParamList('stRef', sortedLines)))
        htmlList.append('      <th class="Sentence" onclick="sortTable({0})">Sentence</th>\n'.format(getParamList('stSen', sortedLines)))
        htmlList.append('      <th class="SentenceBleu" onclick="sortTable({0})">Sen<br>Bleu</th>\n'.format(getParamList('stBleu', sortedLines)))
        if hasMtEval:
            htmlList.append('      <th class="mtBleu" onclick="sortTable({0})">MT<br>Bleu</th>\n'.format(getParamList('stMtBleu', sortedLines)))
            htmlList.append('      <th class="mtNist" onclick="sortTable({0})">MT<br>NIST</th>\n'.format(getParamList('stMtNist', sortedLines)))
        if hasMet:
            htmlList.append('      <th class="MET" onclick="sortTable({0})">MET-<br>EOR</th>\n'.format(getParamList('stMet', sortedLines)))
        if hasBeer:
            htmlList.append('      <th class="BEER" onclick="sortTable({0})">BEER</th>\n'.format(getParamList('stBeer', sortedLines)))
        if hasTer:
            htmlList.append('      <th class="TER" onclick="sortTable({0})">TER</th>\n'.format(getParamList('stTer', sortedLines)))
        htmlList.append('      <th class="WER" onclick="sortTable({0})">WER<br>(Score)</th>\n'.format(getParamList('stWer', sortedLines)))
        htmlList.append('      <th class="ed" onclick="sortTable({0})">E Dist<br>(Score)</th>\n'.format(getParamList('stEd', sortedLines)))
        htmlList.append('  </tr>\n</thead>\n<tbody>\n')
        
        for pos, stList in enumerate(tup[0]):
            htmlList.append('  <tr>\n')
            htmlList.append('    <td class="POS" title="POS" id="{0}">{0}</td>\n'.format(stList[-1]))
            htmlList.append('    <td class="REF" title="Ref Len" id="{0}">{0}<br>({1})</td>\n'.format(stList[8], len(stList[1])))
            htmlList.append('    <td class="Sentence" title="Sentence">\n      <h4>SRC: {0}</h4>\n'.format(stList[0]))
            htmlList.append('      <h4>REF: {0}</h4>\n'.format(stList[1]))
            htmlList.append('      <h4>HYP: {0}</h4>\n<h6><a href="../main.html">HOME</a></h6>&emsp;<h6><a href="#">TOP</a></h6>\n    </td>\n'.format(stList[2]))
            htmlList.append('    <td class="SentenceBleu" title="Sen Bleu"><h4>{0}</h4></td>\n'.format(stList[3]))
            if hasMtEval:
                htmlList.append('      <td class="mtBleu" title="Mt Bleu"><h4>{0}</h4></td>\n'.format(stList[11]))
                htmlList.append('      <td class="mtNist" title="Mt Nist"><h4>{0}<br>({1})</h4></td>\n'.format(stList[12], stList[13]))
            if hasMet:
                htmlList.append('    <td class="MET" title="METEOR"><h4>{0}</h4></td>\n'.format(stList[9]))
            if hasBeer:
                htmlList.append('    <td class="BEER" title="BEER"><h4>{0}</h4></td>\n'.format(stList[14]))
            if hasTer:
                htmlList.append('    <td class="TER" title="TER"><h4>{0}</h4></td>\n'.format(stList[10]))
            werScore = float("{0:.4f}".format(stList[7]/1.0))
            htmlList.append('    <td class="WER" title="WER"><h4>{0}<br>({1})</h4></td>\n'.format(stList[6], werScore))
            htmlList.append('    <td class="ed" title="Edit Dist"><h4>{0}<br>({1})</h4></td>\n'.format(stList[5], stList[4]))
            #htmlList.append('    <td class="WER"><h4>{0}<br>({1})</h4></td>\n'.format(stList[6], "%.4f" % (stList[7]/100.0))) 
            htmlList.append('</tr>\n')
        htmlList.append('</tbody>\n</table>\n</div>\n')
    htmlList.append(hs.sortFunc)
    return htmlList
            
def makeScorePage(key, line, rw, hs, dirName, hasMet, hasTer, hasMtEval, hasBeer, ig):
    
    for pos, aList in enumerate(line):
            aList.append(pos + 1)
            #for i, a in enumerate(aList):
    rw.writeFile(makeScoreTables(line, hs, ig, hasMet, hasTer, hasMtEval, hasBeer), dirName + 'upto_' + str(key) + '.html')
