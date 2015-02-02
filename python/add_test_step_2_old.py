#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
from connect import connect
import mysql.connector

form = cgi.FieldStorage()

card_id = form.getfirst('card_id', '')
# Avoid script injection escaping the user input
card_id = cgi.escape(card_id)

test_type = form.getfirst('test_type', '')
test_type = cgi.escape(test_type)

person_id = form.getfirst('person_id', '')
# Avoid script injection escaping the user input
person_id = cgi.escape(person_id)

comments = form.getfirst('comments', '')
comments = cgi.escape(comments)

# A nested FieldStorage instance holds the file
fileitem = form['attach1']

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('files/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
 
fileitem2 = form['attach2']

# Test if the file was uploaded
if fileitem2.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn2 = os.path.basename(fileitem2.filename)
   open('files/' + fn2, 'wb').write(fileitem2.file.read())
   message = 'The file "' + fn2 + '" was uploaded successfully'

fileitem3 = form['attach3']

# Test if the file was uploaded
if fileitem3.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn3 = os.path.basename(fileitem3.filename)
   open('files/' + fn3, 'wb').write(fileitem3.file.read())
   message = 'The file "' + fn3 + '" was uploaded successfully'
 
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
<p>Card Id: %s
<p>Person Id: %s
</body></html>
""" % (message,card_id,person_id)

cnx = connect(1)

cursor = cnx.cursor()


print "Insert into Test set test_type_id=%s, card_id=%s, person_id=%s, comments=%s;" % (test_type,card_id,person_id,comments) 

