import cgi
import base
import home_page_list
from connect import connect
import sys
import home_page

sys.stdout = open('../cgi-bin/archive/home_page.html', 'w')

home_page > '../cgi-bin/archive/home_page.html'
