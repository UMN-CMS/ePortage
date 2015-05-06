from connect import connect
import mysql.connector

def fetch_list_tests():
    db = connect(0)
    cur=db.cursor()
    cur.execute("select Test_Type.name,COUNT(*),COUNT(DISTINCT Test.card_id) from Test,Test_Type WHERE Test.successful=1 and Test.test_type_id=Test_Type.test_type  GROUP BY Test.test_type_id ORDER BY Test_Type.relative_order");
    rows = cur.fetchall()
    cur.execute("select Test_Type.name,COUNT(*) from Test,Test_Type WHERE Test.test_type_id=Test_Type.test_type  GROUP BY Test.test_type_id ORDER BY Test_Type.relative_order");
    rows2 = cur.fetchall()
    finalrows = ()
    for i in range (0,len(rows)):
        arow=(rows[i][0], rows[i][1],rows[i][2],rows2[i][1])
        finalrows=finalrows+(arow,)
    return finalrows

def render_list_tests():
    rows = fetch_list_tests()
    
    print    '<div class="row">'
    print            '<div class="col-md-1"> </div>'
    print            '<div class="col-md-11"><table class="table table-bordered table-striped Portage_table">'
    print            '<tr><th>Test<th>Total Tests<th>Total Successful Tests<th>Total Cards with Successful Tests</tr>'
#    print            '<div class="col-md-3"><b>Total Tests</b></div>'
#    print            '<div class="col-md-3"><b>Total Successful Tests</b></div>'
#    print            '<div class="col-md-3"><b>Total Cards with Successful Tests</b></div>'
    for test in rows:
#            print    '<div class="row">'
            print            '<tr><td>%s' % (test[0])
            print            '<td>%s' % (test[3])
            print            '<td>%s' % (test[1])
            print            '<td>%s' % (test[2])
            print    '</tr>'            
    print    '</table></div>'

def fetch_list_module():
    db = connect(0)
    cur = db.cursor()

    cur.execute("SELECT sn, Card_id FROM Card ORDER by Card.sn ASC")
    rows = cur.fetchall()
    return rows


def render_list_module():

    row = fetch_list_module()
    n = 0

    col1=''
    col2=''
    col3=''
    
    for cards in row:
        if n%3 == 0:
            col1+='<li><a href="module.py?card_id=%(id)s&serial_num=%(serial)s"> %(serial)s </h4></li>' %{'serial':cards[0], 'id':cards[1]}
        if n%3 == 1:
            col2+='<li><a href="module.py?card_id=%(id)s&serial_num=%(serial)s"> %(serial)s </h4></li>' %{'serial':cards[0], 'id':cards[1]}
        if n%3 == 2:
            col3+='<li><a href="module.py?card_id=%(id)s&serial_num=%(serial)s"> %(serial)s </h4></li>' %{'serial':cards[0], 'id':cards[1]}
        n += 1
        
    print '<div class="row">'
    print '<div class="col-md-4"><ul>'
    print col1
    print '</ul></div><div class="col-md-4"><ul>'
    print col2
    print '</ul></div><div class="col-md-4"><ul>'
    print col3
    print '</ul></div>'

def add_module_form():
    
    print    '<form method="post" class="sub-card-form" action="add_module2.py">'
    print    '<div class="row">'
    print            '<div class="col-md-12">'
    print                    '<h4><u>Adding a new Test Board</u></h4>'
    print            '</div>'
    print    '</div>'

    print    '<br>'
    print    '<br>'

    print    '<div class="row">'
    print            '<div class = "col-md-6">'
    print                    '<label class="sub-card">Serial Number'
    print                            '<input type="int" name="serial_number">'
    print                    '</label>'
    print            '</div>'
    print    '</div>'

    print    '<br>'

    print    '<div class="row">'
    print            '<div class="col-md-12 sub-card-submit">'
    print                    '<input type="submit">'
    print            '</div>'
    print    '</div>'

    print    '</form>'



def add_module(serial_number):
    try:
        db = connect(1)
        cur = db.cursor()

        cur.execute("INSERT INTO Card set sn = '%s'; " % (serial_number)) 
        #print '<div> INSERT INTO Card set sn = %s; </div>' %(serial_number)
        db.commit()
        db.close()
    except mysql.connector.Error as err:
       print("<h3>Serial number already exists!</h3>")
    
    
