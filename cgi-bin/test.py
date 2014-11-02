#!/usr/bin/python

import cgi, cgitb

currentseq = 'TTTTTT'

print 'Content-type: text/html'
print
print '<html><head>'
print ''
print '</head><body>'
print '<h1>Handler with new input test</h1>'
print '<form action="/cgi-bin/newtest.py" method="post">'
print 'Enter DNA Sequence: <input type="text" name="seq">  <br />'
print '<input type = "submit" value = "submit" name = "subname">' 
print '</form>'
print '<h3><a href="http://bioise2014.ist.unomaha.edu/test.html" target="_self">Input Site</a></h3>'
print '</body></html>'

