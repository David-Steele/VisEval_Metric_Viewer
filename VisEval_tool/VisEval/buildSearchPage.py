# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:40:32 2017
@author: david
"""

#create search page HTML
htmlHead = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
<style>
* {
  box-sizing: border-box;
}

#myInput {
  background-position: 10px 12px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}

#myUL {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

#myUL li a {
  border: 1px solid #ddd;
  margin-top: -1px; /* Prevent double borders */
  background-color: #f6f6f6;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  color: black;
  display: block
}

#myUL li a:hover:not(.header) {
  background-color: #eee;
}
</style>
</head>
<body>

<h2>Search Sentence List</h2>

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for a sentence..." title="Type in a few words from your sentence...">
<h6><a href="main.html">HOME</a></h6>
<ul id="myUL">
"""

htmlTail = """
<script>
function myFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";

        }
    }
}
</script>
<a href="main.html">HOME</a>
</body>
</html>\n
"""
contents = []
contents.append(htmlHead)

def showList(aList):
    for el in aList:
        link = el[-1].split('/')
        link = 'scorepages/'+link[-1]
        for idx, sen in enumerate(el[0]):
            line = '<li><a href="{0}#{1}">{2}</br>{3}</a></li>\n'.format(link, idx + 1, sen[0], sen[1])
            contents.append(line)
    contents.append(htmlTail)
    return contents
        
