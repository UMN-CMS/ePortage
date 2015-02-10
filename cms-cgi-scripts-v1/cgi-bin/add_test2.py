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
comments = form.getvalue("comments")

if comments:
    comments = cgi.escape(comments)

base.header(title='Add Test')
base.top()

test_id=add_test_functions.add_test(person_id, test_type, serial_num, success)

for itest in (1,2,3):
    afile = form['attach%d'%(itest)]
    if (afile.filename):
        adesc= form.getvalue("attachdesc%d"%(itest))
        if adesc:
            adesc = cgi.escape(adesc)
        acomment= form.getvalue("attachcomment%d"%(itest))
        if acomment:
            acomment = cgi.escape(acomment)
        add_test_functions.add_test_attachment(test_id,afile,adesc,comments)
    

base.bottom()

