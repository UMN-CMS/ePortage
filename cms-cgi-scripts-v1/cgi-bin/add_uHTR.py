#!/usr/bin/python

import cgi
import base
import home_page_list

#cgi header
print "Content-type: text/html\n"

base.header(title='Home Page uHTR Testing')
base.top()

home_page_list.add_uHTR_form()


print    '<div class="row">'
print            '<div class="col-md-3">'
print            '<h2>List of All Boards</h2>' 
print            '<b><em>(Sorted by Serial Number)</em></b>'
print            '</div>'
print    '</div>'

print   '<br><br>'

home_page_list.render_list_uHTR()

base.bottom()

