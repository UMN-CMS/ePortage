#!/usr/bin/python

import cgi
import base
import HomePageList

#cgi header
print "Content-type: text/html\n"

base.header(title='Home Page uHTR Testing')
base.top()

form = cgi.FieldStorage()

if form.getvalue('serial_number') and form.getvalue('mac_address'):
    sn = cgi.escape(form.getvalue('serial_number'))
    mac = cgi.escape(form.getvalue('mac_address'))

    #print '<div> Serial Number = %(s)s , Mac = %(d)s </div>' %{'s': sn, 'd':mac} 
    HomePageList.add_uHTR(sn, mac)
    
    print    '<div class="row">'
    print            '<div class="col-md-3">'
    print            '<h2>List of All Boards</h2>' 
    print            '<b><em>(Sorted by Serial Number)</em></b>'
    print            '</div>'
    print            '<div class="col-md-3">'
    print                    '<br><br>'
    print                    '<a href="add_uHTR.py">'
    print                            '<button type="button">Add a New Board</button>'
    print                    '</a>'
    print            '</div>'
    print    '</div>'

    print   '<br><br>'


    HomePageList.render_list_uHTR()

    base.bottom()


else:
    print    '<div class="row">'
    print            '<div class="col-md-12">'
    print               '<h4><b> FAILED. Enter both SERIAL NUMBER and MAC ADDRESS </b></h4>'
    print             '</div>'
    print    '</div>'

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

    
    
    
