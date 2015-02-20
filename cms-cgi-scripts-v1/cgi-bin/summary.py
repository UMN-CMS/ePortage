#!/usr/bin/python

import cgi
import base
from connect import connect
import mysql.connector
from summary_functions import get



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
print                    '<th> Tests Passed </th>'
print                    '<th> Tests Remaining </th>'
print                    '<th> Final Status </th>'
print                '</tr>'

for row in List_of_rows:
    print '<tr>'
    print '<td> <a href=uHTR.py?card_id=%(id)s&serial_num=%(serial)s> %(serial)s </a></td>' %{'serial':row[0], 'id':row[1]}
    #print '<td> %s </td>' %row[1]
    
    print '<td><select>'
    for tests in row[2]:
        print '<option> %s </option>' %tests
    print '</select></td>'

    print '<td><select>'
    for tests in row[3]:
        print '<option> %s </option>' %tests
    print '</select></td>'

    print '<td> ? </td>'

    print '</tr>'

print '</tbody></table></div></div><br><br>'


base.bottom()

    

