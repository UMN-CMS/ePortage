#!/usr/bin/python

import cgi
import base
import HomePageList

#cgi header
print "Content-type: text/html\n"

base.header(title='Home Page uHTR Testing')
base.top()

HomePageList.add_uHTR_form()


print    '<div class="row">'
print            '<div class="col-md-3">'
print            '<h2>List of All Boards</h2>' 
print            '<b><em>(Sorted by Serial Number)</em></b>'
print            '</div>'
print    '</div>'

print   '<br><br>'

HomePageList.render_list_uHTR()

base.bottom()

