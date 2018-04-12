# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:52:19 2017
@author: david
"""
### html strings

graphHead = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="../style.css">
        <link rel="icon" href="../images/tabIconMini.png">
        <title>VisMet</title>
        
        <script type="text/javascript">
            function hideDiv(div1,div2)
            {
               d1 = document.getElementById(div1); d2 = document.getElementById(div2);
               
               if( d2.style.display == "none" )
               {
                  d1.style.display = "none";
                  d2.style.display = "block";
               }
               else
               {
                  d1.style.display = "block";
                  d2.style.display = "none";
               }
               
               if (navigator.userAgent.match(/Chrome|AppleWebKit/)) {
                   window.location.href = "#"+div2;
                   window.location.href = "#"+div2;  /* these take twice */
            } else {
                    window.location.hash = d;
            }
            }
        </script>
        
    </head>
    <body>
        <div class="centre" id="centreOfBody">
            <!--<div><a href="../main.html"><img src="../images/banner.png" alt="Sea View" style="width:1732px;height:304px;"></a></div>-->
            <div><a href="../main.html"><img src="../images/banner.png" alt="Sea View" style="width:100%;margin: 0 auto"></a></div>
            <div class="main">          
"""

head = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="style.css">
        <link rel="icon" href="images/tabIconMini.png">
        <title>VisMet</title> 
    </head>
    <body>
        <div class="centre" id="centreOfBody">
            <!--<div><a href="main.html"><img src="images/banner.png" alt="Sea View" style="width:1732px;height:304px;"></a></div>-->
            <div><a href="main.html"><img src="images/banner.png" alt="Sea View" style="width:100%;margin: 0 auto"></a></div>
            <div class="main">          
"""

scoreTopRow = """
<div id="idhere" name="idhere">
    <table style="width:100%">
      <tr>
        <td style="text-align:center;"><img onclick="hideDiv('hb1','hb2')" src="graphs/histBox" title="Showing the Score Distribution" style="width:320px;height:180px;"></td>
        <td style="text-align:center;"><img onclick="hideDiv('al1','al2')" src="graphs/graphs_Score_REF_Length_scatter.png" title="A Scatter Plot Comparing Sentence Lengths and Scores" style="width:320px;height:180px;"></td>
        <td style="text-align:center;"><img onclick="hideDiv('bx1','bx2')" src="graphs/graphs_Score_HYP_Length_scatter.png" title="A Scatter Plot Comparing Sentence Lengths and Scores" style="width:320px;height:180px;"></td>
        <td style="text-align:center;"><img onclick="hideDiv('sc1','sc2')" src="graphs/graphs_Score_SRC_Length_scatter.png" title="A Scatter Plot Comparing Sentence Lengths and Scores" style="width:320px;height:180px;"></td>
      </tr>
   </table>
</div>
<div id="lrghb3" name="lrghb3" style="text-align:center; display:none">
    <img onclick="hideDiv('lrghb4','lrghb5') "src="graphs/lrghb6" title="Showing the Score Distribution">
</div>
<div id="lrgREF" name="lrgREF" style="text-align:center; display:none">
    <img onclick="hideDiv('lrgal4','lrgal5') "src="graphs/graphs_Score_REF_Length_scatter.png" title="A Scatter Plot Comparing Sentence Lengths and Scores">
</div>
<div id="lrgHYP" name="lrgHYP" style="text-align:center; display:none">
    <img onclick="hideDiv('lrgbx4','lrgbx5') "src="graphs/graphs_Score_HYP_Length_scatter.png" title="A Scatter Plot Comparing Sentence Lengths and Scores">
</div>
<div id="lrgSRC" name="lrgSRC" style="text-align:center; display:none">
    <img onclick="hideDiv('lrgsc4','lrgsc5') "src="graphs/graphs_Score_SRC_Length_scatter.png" title="A Scatter Plot Comparing Sentence Lengths and Scores">
</div>
<h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
"""

graphTable = """
<div id="idhere" name="idhere">
    <table style="width:100%">
      <tr>
        <td style="text-align:center;"><img onclick="hideDiv('al1','al2')" src="graphs/alph" title="histogram to compare two distributions" style="width:320px;height:180px;"></td>
        <td style="text-align:center;"><img onclick="hideDiv('bx1','bx2')" src="graphs/boxy" title="boxplot showing key points of two distributions" style="width:320px;height:180px;"></td>
        <td style="text-align:center;"><img onclick="hideDiv('sc1','sc2')" src="graphs/scatty" title="scattergraph comparing two distributions" style="width:320px;height:180px;"></td>
      </tr>
   </table>
</div>
<div id="lrgal3" name="lrgal3" style="text-align:center; display:none">
    <img onclick="hideDiv('lrgal4','lrgal5') "src="graphs/lrgal6" title="histogram to compare two distributions">
</div>
<div id="lrgbx3" name="lrgbx3" style="text-align:center; display:none">
    <img onclick="hideDiv('lrgbx4','lrgbx5') "src="graphs/lrgbx6" title="boxplot showing key points of two distributions">
</div>
<div id="lrgsc3" name="lrgsc3" style="text-align:center; display:none">
    <img onclick="hideDiv('lrgsc4','lrgsc5') "src="graphs/lrgsc6" title="scattergraph comparing two distributions">
</div>
<h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
"""

scorepagesHead = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
        <link rel="stylesheet" type="text/css" href="../style.css">
        <link rel="icon" href="../images/tabIconMini.png">
        <title>VisMet</title>
        <script data-require="jquery" data-semver="3.2.1" src="../jQuery/jquery-3.2.1.js"></script>
        <!--<script src="../jQuery/script.js"></script>-->
        
        <style>
            table {
                border-spacing: 0;
                width: 100%;
                border: 1px solid #ddd;
            }
            
            thead {
				background-color: #ddd;				
			}
            
            th {
                cursor: pointer;
            }
            
            th, td {
                text-align: left;
                padding: 4px;
            }
            
            tr:nth-child(even) {
                background-color: #ddd
            }
            
            h6 {
                display: inline;
            }
            
        </style>
        
        <script>
                $(window).on('load', (function(){
                    $("input:checkbox:not(:checked)").each(function() {
                        var column = "table ." + $(this).attr("name");
                        $(column).hide();
                    });
        
                    $("input:checkbox").click(function(){
                        var column = "table ." + $(this).attr("name");
                    $(column).toggle();
                    });
                }));
        </script>
        
        <script type="text/javascript">
            function sortTable(div1,div2,div3,div4,div5,div6,div7,div8,div9,div10,div11,div12,div13,div14,div15,div16,div17,div18,div19,div20,div21,div22)
            {
               d1 = document.getElementById(div1); d5 = document.getElementById(div5);
               d2 = document.getElementById(div2); d6 = document.getElementById(div6);
               d3 = document.getElementById(div3); d7 = document.getElementById(div7);
               d4 = document.getElementById(div4); d8 = document.getElementById(div8);
               d9 = document.getElementById(div9); d10 = document.getElementById(div10);
               d11 = document.getElementById(div11); d12 = document.getElementById(div12);
               d13 = document.getElementById(div13); d14 = document.getElementById(div14);
               d15 = document.getElementById(div15); d16 = document.getElementById(div16);
               d17 = document.getElementById(div17); d18 = document.getElementById(div18);
               d19 = document.getElementById(div19); d20 = document.getElementById(div20);
               d21 = document.getElementById(div21); d22 = document.getElementById(div22);
                //try {
                   d9 = document.getElementById(div9); d10 = document.getElementById(div10);
                   d9.style.display = "none"; d10.style.display = "none";
                //}
                //catch(err) {
                //console.log(err.message);
                //}
               
               d3.style.display = "none"; d4.style.display = "none"; 
               d5.style.display = "none"; d6.style.display = "none";
               d7.style.display = "none"; d8.style.display = "none";
               
               d9.style.display = "none"; d10.style.display = "none"; 
               d11.style.display = "none"; d12.style.display = "none";
               d13.style.display = "none"; d14.style.display = "none";
               d15.style.display = "none"; d16.style.display = "none";
               d17.style.display = "none"; d18.style.display = "none";
               d19.style.display = "none"; d20.style.display = "none";
               d21.style.display = "none"; d22.style.display = "none";
               
               if( d2.style.display == "none" )
               {
                  d1.style.display = "none";
                  d2.style.display = "block";
               }
               else
               {
                  d1.style.display = "block";
                  d2.style.display = "none";
               }
            }
        </script>
        
        
    </head>
    <body>
        <div class="centre" id="centreOfBody">
            <!--<div><a href="../main.html"><img src="../images/banner.png" alt="Sea View" style="width:1732px;height:304px;"></a></div>-->
            <div><a href="../main.html"><img src="../images/banner.png" alt="Sea View" style="width:100%;margin: 0 auto"></a></div>
            <div class="main">
                   <!-- <div id="chboxes">
                        <input type="checkbox" name="POS" checked />Pos
                        <input type="checkbox" name="Sentence" checked />Sentence
                        <input type="checkbox" name="SentenceBleu" checked />Sen Bleu
                        <input type="checkbox" name="TER" checked />TER
                        <input type="checkbox" name="WER" checked />WER
                    </div>-->
"""
################################ top right bottom left
tail = """
            <!--<div id="cl"><b>***Note: as an example selecting 0.52 will show all sentences with a bleu score &gt 0.51 and &lt= 0.52. 
            In addition --- signifies that no sentences had a bleu score in the respective range</b></div>-->
            <div id="cl" style="text-align: center;">
                <p>~~~~~~~~~~~~~~~~~~~~</p>
                <p><a href="dataSetStats.html">SEE DATASET RESULTS</a></p>
                <a href="search.html">SEARCH SENTENCE LIST</a>
            </div>
        </div>
    </div>
    <body>
</html>
"""

graphsTail = """
            <!--<div id="cl"><b>***Note: as an example selecting 0.52 will show all sentences with a bleu score &gt 0.51 and &lt= 0.52. 
            In addition --- signifies that no sentences had a bleu score in the respective range</b></div>-->
            <div id="cl" style="text-align: center;">
            TABLETOP
                <!--<a href="scorepages/graphs.html"><a href="graphs/graphLinks.html">
                    <img src="images/tabIconAndText.png" alt="Show Graphs" title="View Graphs" style="width:200px;height:200px;border:0;">
                </a>-->
                <p>~~~~~~~~~~~~~~~~~~~~</p>
                <p><a href="dataSetStats.html">SEE DATASET RESULTS</a></p>
                <a href="search.html">SEARCH SENTENCE LIST</a>
            </div>
        </div>
    </div>
    <body>
</html>
"""

shortTail="""
            </div>
        </div>
    <body>
</html>
"""

btnDiv = """
            <div class="square" style="background-color:rgb(###); left: lftpx;">
                <div class="content">
                    <div class="table">
                        <div class="table-cell">
                            <a style="text-decoration:none;" href="~~~"><b>%%%</b><br>xxx</a>
                        </div>
                    </div>
                </div>
            </div>
"""
btnDivNoScores = """
            <div class="square" style="background-color:rgb(###);">
                <div class="content">
                    <div class="table">
                        <div class="table-cell">
                            <b>---</b>
                        </div>
                    </div>
                </div>
            </div>
"""
metScatter = """
<div class="image"  id="cl" style="width:80%;">
                <img src="../images/bleu_v_meteor_scatter.png" alt="Scatter Bleu Vs METEOR">
                <h6><a href="../main.html">HOME</a></h6>
            </div>
"""

metHist = """
<div class="image"  id="cl" style="width:80%;">
                <img src="../images/hasMet_histAndBox.png" alt="METEOR Hist and Box">
                <h6><a href="../main.html">HOME</a></h6>
            </div>
"""

graphs = """
            <!--<div class="image"  id="cl" style="width:80%;">
                <img src="../images/histAndBox.png" alt="Hist and Box">
                <h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
            </div>
            METEOR_HIST_TO_GO_HERE-->
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/barplot.png" alt="Boxplots">
                <h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
            </div>  
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/boxplots.png" alt="Boxplots">
                <h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
            </div>   
            <!--METEOR_SCATTER_TO_GO_HERE
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/bleu_v_src_scatter.png" alt="Scatter Bleu Vs Src">
                <h6><a href="../main.html">HOME</a></h6>
            </div>
            
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/bleu_v_ref_scatter.png" alt="Scatter Bleu Vs Ref">
                <h6><a href="../main.html">HOME</a></h6>
            </div>
            
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/bleu_v_hyp_scatter.png" alt="Scatter Bleu Vs Hyp">
                <h6><a href="../main.html">HOME</a></h6>
            </div>
            
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/bleu_v_wer_scatter.png" alt="Scatter Bleu Vs WER">
                <h6><a href="../main.html">HOME</a></h6>
            </div>
            
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/bleu_v_werGood_scatter.png" alt="Scatter Bleu Vs WER Goodness">
                <h6><a href="../main.html">HOME</a></h6>
            </div>-->
            
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/hyp_v_ref_scatter.png" alt="Scatter Hyp Vs Ref">
                <h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
            </div>  
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/src_v_ref_scatter.png" alt="Scatter Hyp Vs Ref">
                <h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
            </div> 
            <div class="image"  id="cl" style="width:80%;">
                <img src="../images/src_v_hyp_scatter.png" alt="Scatter Hyp Vs Ref">
                <h6><a href="../main.html">HOME</a>&emsp;<a href="#">TOP</a></h6>
            </div> 
            """
            
css = """.square {
    float:left;
    position: relative;
    width: 4.44%;
    padding-bottom : 4.44%; /* = width for a 1:1 aspect ratio */
    margin:0.1%;
    overflow:hidden;
		border-style:solid;
		border-radius:50%;
}
.content {
    position:absolute;
    height:80%; /* = 100% - 2*10% padding */
    width:90%; /* = 100% - 2*5% padding */
    padding: 10% 5%;
}
.table{
    display:table;
    height:100%;
    width:100%;
}
.table-cell{
    display:table-cell;
    vertical-align:middle;
    text-align:center;
    font-size: 108%;
    height:100%;
    width:100%;
}
#centreOfBody{
    margin: 0 auto;
    text-align: left;
    width: 1732px;
    max-width: 1732px;
}
#cl {
    float: left;
    clear: left;
    width: 100%;
    height: 3%;
    background: #fff;
    margin: 12px;
}

a:link    {color:#000;}  /* unvisited link  */
a:visited {color:#000;}  /* visited link    */
a:hover   {color:#000;}  /* mouse over link */
a:active  {color:#000;}  /* selected link   */ 
"""

sortFunc = """
            </div> <!--end main div-->
        </div>
    </body>
</html>
"""
