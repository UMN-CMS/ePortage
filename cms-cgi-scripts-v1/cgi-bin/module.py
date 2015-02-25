#!/usr/bin/python

import cgi
import base
import home_page_list
import module_Functions
from connect import connect

#cgi header
print "Content-type: text/html\n"


form = cgi.FieldStorage()
card_id = base.cleanCGInumber(form.getvalue('card_id'))
serial_num = base.cleanCGInumber(form.getvalue('serial_num'))
base.header(title='uHTR ePortage')
base.top()
#print 'card_id = ', card_id
#print  'serial_num = ', serial_num

module_functions.add_test_tab(serial_num, card_id)

db = connect(0)
cur = db.cursor()

cur.execute("select test_type, name from Test_Type where required = 1 order by relative_order ASC")
for test_type in cur:
	module_functions.ePortageTest(test_type[0], serial_num, test_type[1])


base.bottom()
