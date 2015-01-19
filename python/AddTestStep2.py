#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import connect from connect

form = cgi.FieldStorage()

card_id = form.getfirst('card_id', '')
# Avoid script injection escaping the user input
card_id = cgi.escape(card_id)

person_id = form.getfirst('person_id', '')
# Avoid script injection escaping the user input
person_id = cgi.escape(person_id)

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




