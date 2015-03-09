#!/usr/bin/python

import cgi
import base
from connect import connect
import mysql.connector
from summary_functions import get
import module_functions



#cgi header
print "Content-type: text/html\n"

base.header(title='Summary')
base.top()

List_of_rows = get()

print '<div class="row">'
print    '<div class="col-md-12">'
print        '<table class="table" style="width:100%">'
print            '<tbody>'
print                '<tr>'
print                    '<th> S/N </th>'
print                    '<th colspan=2> Tests Passed </th>'
print                    '<th colspan=2> Tests Remaining </th>'
#print                    '<th> Final Status </th>'
print                '</tr>'

for row in List_of_rows:
    print '<tr>'
    print '<td> <a href=module.py?card_id=%(id)s&serial_num=%(serial)s> %(serial)s </a></td>' %{'serial':row[0], 'id':row[1]}
    #print '<td> %s </td>' %row[1]
    
    print '<td><ul>'
    for tests in row[2][0:][::2]:
        print '<li>%s' %tests
    print '</ul></td>'

    print '<td><ul>'
    for tests in row[2][1:][::2]:
        print '<li>%s' %tests
    print '</ul></td>'

    print '<td><ul>'
    for tests in row[3][0:][::2]:
        print '<li> <a href="add_test.py?serial_num=%d&suggested=%d">%s</a>' %(row[0],tests[1],tests[0])
    print '</ul></td>'

    print '<td><ul>'
    for tests in row[3][1:][::2]:
        print '<li> <a href="add_test.py?serial_num=%d&suggested=%d">%s</a>' %(row[0],tests[1],tests[0])
    print '</ul></td>'

#    print '<td> ? </td>'

    print '</tr>'

print '</tbody></table></div></div><br><br>'


base.bottom()

    

