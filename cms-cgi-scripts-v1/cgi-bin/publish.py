import sys
import os

if len(sys.argv) == 1:
	print "Please input a destination directory after the script call."
	sys.exit()
else:
	if not os.path.isdir(sys.argv[1]):
		os.makedirs(sys.argv[1])
import base
from home_page_list import fetch_list_module
from connect import connect
import home_page
import module_functions
import summary
from summary_functions import get
import shutil

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

row = fetch_list_module()

for cards in row:
	stdout = sys.stdout
	sys.stdout = open('%(loc)s/card_%(sn)s.html' %{ 'loc':sys.argv[1],'sn':cards[0]}, 'w') 
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
	sys.stdout.close()
	sys.stdout = stdout

	base.bottom()

copytree('../static/css', '%s' %(sys.argv[1]))

copytree('../static/files' , '%s' %sys.argv[1])

