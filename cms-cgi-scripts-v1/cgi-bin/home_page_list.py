from connect import connect
import mysql.connector


def fetch_list_module():
    db = connect(1)
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
    
    
