#!/usr/bin/python

import cgi
import base
import home_page_list
import sys

if(len(sys.argv) != 1):
	stdout = sys.stdout
	sys.stdout = open('%(loc)s/home_page.html' %{ 'loc':sys.argv[1]}, 'w') 
else:
	#cgi header
	print "Content-type: text/html\n"

base.header(title='ePortage Home Page')
base.top()

print    '<div class="row">'
print            '<div class="col-md-12">'
print            '<h2>Count by Test</h2>' 
print            '</div>'
print    '</div>'

home_page_list.render_list_tests()
print    '<div class="row">'
print            '<div class="col-md-3">'
print            '<h2>List of All Boards</h2>' 
print            '<b><em>(Sorted by Serial Number)</em></b>'
print            '</div>'
if len(sys.argv) == 1:
	print            '<div class="col-md-3">'
	print                    '<br><br>'
	print                    '<a href="add_module.py">'
	print                            '<button type="button">Add a New Board</button>'
	print                    '</a>'
	print            '</div>'
print  	 '</div>'
print   '<br><br>'


home_page_list.render_list_module()

base.bottom()

if len(sys.argv) != 1:
	sys.stdout.close()
	sys.stdout = stdout
