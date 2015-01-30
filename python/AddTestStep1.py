#!/usr/bin/python
import mysql.connector
from connect import connect
import cgi, os
import cgitb; cgitb.enable()

#connect
cnx = connect(0)
cursor = cnx.cursor()

# FIX ME TO WORK WITH CGI!
card_id = 4
# Get card sn from database, save first result
cursor.execute("select sn from Card where card_id='%d'" % ( card_id, ))
for sn in cursor:
	card_sn = sn

#cgi header
print "Content-type: text/html\n"
#page header
print "<html><head><title>Add Test for Card</title></head>";
print "<body bgcolor=#CCAA44>";

print "<h1>Add Test for Card %d</h1>" % ( card_sn );

# start the form
print "<form enctype=\"multipart/form-data\" action=\"AddTestStep2.py\" method=\"post\">";

print "<INPUT TYPE='hidden' name='card_id' value='%d'>" % ( card_id, )

# tester
cursor.execute("select person_id, person_name from People")

print "<p>Tester:"
print "<SELECT name=\"person_id\">"

for (person_id, person_name) in cursor:
	print "  <OPTION value='%d'>%s</OPTION>" % (person_id, person_name)

print "</SELECT>"

# select which test
query = ("select test_type, name, desc_short from Test_Type")

cursor.execute(query)

print "<P>Which test:"

print "<SELECT name=\"test_type\">"

for (test_type, name, desc_short) in cursor:	
	print "  <OPTION value='%d'>%s</OPTION>" % (test_type, name)

#, "", desc_short
print "</SELECT>"

print "<P>Successful? <INPUT type='checkbox' name='successful'>"

print "<P>Comments: <TEXTAREA name='comments' rows='4' cols='80'></TEXTAREA>"

print "<P>Attachment 1: <INPUT type='file' name='attach1'>"
print "<BR>Attachment 2: <INPUT type='file' name='attach2'>"
print "<BR>Attachment 3: <INPUT type='file' name='attach3'>"

print "<P><INPUT type=submit>";
print "</form>";

# footer/close
print "</body></html>";
