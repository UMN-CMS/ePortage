#!/usr/bin/python

import cgi
import base
import add_test_functions

#cgi header
print "Content-type: text/html\n"

form = cgi.FieldStorage()
person_id = base.cleanCGInumber(form.getvalue("person_id"))
test_type = base.cleanCGInumber(form.getvalue("test_type"))
serial_num = base.cleanCGInumber(form.getvalue("serial_number"))
success = base.cleanCGInumber(form.getvalue("success"))
comments = form.getvalue("comments")

if comments:
    comments = cgi.escape(comments)

base.header(title='Add Test')
base.top()

test_id=add_test_functions.add_test(person_id, test_type, serial_num, success, comments)

for itest in (1,2,3):
    afile = form['attach%d'%(itest)]
    if (afile.filename):
        adesc= form.getvalue("attachdesc%d"%(itest))
        if adesc:
            adesc = cgi.escape(adesc)
        acomment= form.getvalue("attachcomment%d"%(itest))
        if acomment:
            acomment = cgi.escape(acomment)
        add_test_functions.add_test_attachment(test_id,afile,adesc,acomment)
    

base.bottom()

