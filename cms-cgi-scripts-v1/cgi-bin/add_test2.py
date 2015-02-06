#!/usr/bin/python

import cgi
import base
import add_test_functions

#cgi header
print "Content-type: text/html\n"

form = cgi.FieldStorage()
person_id = form.getvalue("person_id")
test_type = form.getvalue("test_type")
serial_num = form.getvalue("serial_number")
success = form.getvalue("success")
file1 = form['attach1']
file2 =  form['attach2']
file3 =  form['attach3']
comments = form.getvalue("comments")

if file1:
    file1 = cgi.escape(file1)
if file2:
    file2 = cgi.escape(file2)
if file3:
    file3 = cgi.escape(file3)
if comments:
    comments = cgi.escape(comments)

base.header(title='Add Test')
base.top()

add_test_functions.add_test(person_id, test_type, serial_num, success, file1, file2, file3, comments)


base.bottom()

