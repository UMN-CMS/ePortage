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
file1desc = form.getvalue("file1desc")
file1comment = form.getvalue("file1comment")
file2desc = form.getvalue("file2desc")
file2comment = form.getvalue("file2comment")
file3desc = form.getvalue("file3desc")
file3comment = form.getvalue("file3comment")

if file1desc:
    file1desc = cgi.escape(file1desc)
if file1comment:
    file1comment = cgi.escape(file1comment)
if file2desc:
    file2desc = cgi.escape(file2desc)
if file2comment:
    file2comment = cgi.escape(file2comment)
if file3desc:
    file3desc = cgi.escape(file3desc)
if file3comment:
    file3comment = cgi.escape(file3comment)
if comments:
    comments = cgi.escape(comments)

base.header(title='Add Test')
base.top()

add_test_functions.add_test(person_id, test_type, serial_num, success, file1, file2, file3, comments, file1desc, file1comment, file2desc, file2comment, file3desc, file3comment)


base.bottom()

