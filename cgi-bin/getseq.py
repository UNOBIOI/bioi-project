#!/usr/bin/python

import cgi, cgitb

def showseq(seq):

    print 'Content-type: text/html'
    print
    print '<html><head>'
    print 'GET SEQUENCE IS %s ' % (seq)
    print '</head><body>'
    print '</body></html>'


