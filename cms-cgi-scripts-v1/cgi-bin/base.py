import re
import sys
def header(title=''):
    print '<head>'
    if len(sys.argv) == 1:
    	print '<link  rel="stylesheet" href="../static/css/bootstrap.min.css">'
    	print '<link  rel="stylesheet" href="../static/css/style.css">'
    else:
	print '<link  rel="stylesheet" href="bootstrap.min.css">'
    	print '<link  rel="stylesheet" href="style.css">'
    print '<title> %s </title>' %title
    print '</head>'

def top():
    print '<body>'
    print '<div class="container">'
    print '<div class="row">'
    if len(sys.argv) == 1:
    	print '<div class="col-md-8"><img src="../static/files/us-cms.gif" class="img-responsive"></div>'
    else:
    	print '<div class="col-md-8"><img src="us-cms.gif" class="img-responsive"></div>'
    print '<div class="col-md-4">'
    print '<br><h2 style="color:blue"> &emsp;&emsp;&emsp; HCAL Upgrade Test  </h2>'
    print '<hr>'
    print '<br>'
    print '</div>'
    print '</div>'
    if len(sys.argv) == 1:
    	print                               '<div class ="row">'
    	print                                   '<div class = "col-md-12">'
    	print                                       '<a href="home_page.py">'
    	print                                           '<button>  HOME  </button>'
    	print                                       '</a>'
    	print                                       '<a href="summary.py">'
    	print					    '<button>  Summary  </button>'
    	print					'</a>'
    	print					'<a href="testers.py">'
    	print					    '<button>  Testers  </button>'
    	print   				        '</a>'
    	#print					'<a href="add_test.py">'
    	#print					    '<button>  Add a New Test  </button>'
    	#print					'</a>'
    	print                                   '</div>'
    	print                                   '<br><br><br>'
    	print                               '</div>'
    else:
	print                               '<div class ="row">'
    	print                                   '<div class = "col-md-12">'
    	print                                       '<a href="index.html">'
    	print                                           '<button>  HOME  </button>'
    	print                                       '</a>'
    	print                                       '<a href="summary.html">'
    	print					    '<button>  Summary  </button>'
    	print					'</a>'
    	print					'<a href="testers.html">'
    	print					    '<button>  Testers  </button>'
    	print   				        '</a>'
    	print                                   '</div>'
    	print                                   '<br><br><br>'
    	print                               '</div>'

def bottom():
    print '</div>'
    print '</body>'
    print '</html>'
    
def cleanCGInumber(cgitext):
    if cgitext is None:
        return 0
    return int(re.sub('[^0-9]','',cgitext))

