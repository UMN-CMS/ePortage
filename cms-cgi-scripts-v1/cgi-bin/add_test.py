#!/usr/bin/python

import cgi
import base
import HomePageList
import add_test_functions


#cgi header
print "Content-type: text/html\n"

form = cgi.FieldStorage()
#card_id = form.getvalue('card_id')
serial_num = form.getvalue('serial_num')
#mac = form.getvalue('mac')

base.header(title='Add Test')
base.top()

add_test_functions.add_test_template(serial_num)

base.bottom()
