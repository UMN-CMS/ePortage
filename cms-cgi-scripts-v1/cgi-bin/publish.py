import cgi
import base
import home_page_list
from connect import connect
import sys
import home_page
import module_functions
import summary
from summary_functions import get

home_page

row = home_page_list.fetch_list_module()

for cards in row:
	sys.stdout = open('../cgi-bin/archive/card_%(sn)s.html' %{'sn':cards[0]}, 'w') 
	serial_num = cards[0]
	card_id = cards[1]
	base.header(title='uHTR ePortage')
	base.top()
	revokes=module_functions.Portage_fetch_revokes(serial_num)
	
	db= connect(0)
	cur = db.cursor()

	cur.execute("select test_type, name from Test_Type where required = 1 order by relative_order ASC")
	for test_type in cur:
        	module_functions.ePortageTest(test_type[0], serial_num, test_type[1], revokes)
	

	base.bottom()

summary


