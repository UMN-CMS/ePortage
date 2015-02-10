from connect import connect
import mysql.connector


def fetch_list_uHTR():
    db = connect(1)
    cur = db.cursor()
        
    cur.execute("SELECT sn, Card_id FROM Card ORDER by Card.sn ASC")
    rows = cur.fetchall()
    return rows


def render_list_uHTR():

    row = fetch_list_uHTR()
    n = 0

    print '<ul>'
    for cards in row:
        if n%3 == 0:
            print '<div class="row">'
        print '<div class="col-md-4">'
        print '<li><h4><a href="uHTR.py?card_id=%(id)s&serial_num=%(serial)s"> %(serial)s </h4></li>' %{'serial':cards[0], 'id':cards[1]}
        print '</div>'

        n += 1
        
        if n%3 == 0:
            print '</div>'
            print '<hr><br>'
        
    print '</ul>'




def add_uHTR_form():
    
    print    '<form method="post" class="sub-card-form" action="add_uHTR2.py">'
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



def add_uHTR(serial_number):
    db = connect(1)
    cur = db.cursor()

    cur.execute("INSERT INTO Card set sn = '%s'; " % (serial_number)) 
    #print '<div> INSERT INTO Card set sn = %s; </div>' %(serial_number)
    db.commit()
    
    
