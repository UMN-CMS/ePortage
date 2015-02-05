def header(title=''):
    print '<head>'
    print '<link  rel="stylesheet" href="/static/css/bootstrap.min.css">'
    print '<link  rel="stylesheet" href="/static/css/style.css">'
    print '<title> %s </title>' %title
    print '</head>'

def top():
    print '<body>'
    print '<div class="container">'
    print '<div class="row">'
    print '<div class="col-md-8"><img src="/static/files/us-cms.gif" class="img-responsive"></div>'
    print '<div class="col-4">'
    print '<h2 style="color:blue"> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &#181HTR Test  </h2>'
    print '<hr>'
    print '<br>'
    print '</div>'
    print '</div>'

    print                               '<div class ="row">'
    print                                   '<div class = "col-md-12">'
    print                                       '<a href="home_page.py">'
    print                                           '<button>  HOME  </button>'
    print                                       '</a>'
    print                                       '<a href="/summary">'
    print					    '<button>  Summary  </button>'
    print					'</a>'
    print					'<a href="/testers">'
    print					    '<button>  Testers  </button>'
    print   				        '</a>'
    print					'<a href="add_test.py">'
    print					    '<button>  Add a New Test  </button>'
    print					'</a>'
    print                                   '</div>'
    print                                   '<br><br><br>'
    print                               '</div>'


def bottom():
    print '</div>'
    print '</body>'
    print '</html>'
    
