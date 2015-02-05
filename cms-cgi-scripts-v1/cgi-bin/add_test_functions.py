from connect import connect
import mysql.connector
import base


def add_test(person_id, test_type, serial_num, success, file1='', file2='', file3='', comments=''):
    if success:
        success = 1
    else:
        success = 0

    db = connect(1)
    cur = db.cursor()

    if serial_num:
        cur.execute("SELECT card_id FROM Card WHERE sn = %(n)s" %{"n":serial_num})
        row = cur.fetchone()
        card_id = row[0]
        

        cur.execute("INSERT INTO Test (person_id, test_type_id, card_id, test_id, successful, day, comments) VALUES (%(pers_id)s, %(test_typ)s, %(card)s, NULL, %(succ)s, NOW(), '%(comment)s')"%{"pers_id": person_id, "test_typ": test_type, "card": card_id, "succ":success, "comment":comments})
        db.commit()

        print '<div class ="row">'
 	print			'<div class = "col-md-3">'
 	print                       '<h3> Test Successfully Added </h3>'
 	print                   '</div>'
 	print  '</div>'

        
    else:
        print '<div class ="row">'
 	print			'<div class = "col-md-3">'
 	print                       '<h3> Attempt Failed. Please Specify Serial Number </h3>'
 	print                   '</div>'
 	print  '</div>'

 	add_test_template(serial_num)




def add_test_template(serial_number):
    
    db = connect(0)
    cur = db.cursor()

    print		'<form action="add_test2.py" method="post">'
    print 			'<INPUT TYPE="hidden" name="serial_number" value="%s">' % (serial_number)
    print			'<div class="row">'
    print				'<div class="col-md-12">'
    print					'<h1>Add Test for Card %s</h1>' %serial_number
    print				'</div>'
    print			'</div>'

    print			'<br><br>'
	
    cur.execute("Select person_id, person_name from People;")

    print			'<div class="row">'
    print				'<div class="col-md-6">'
    print					'<label>Tester'
    print					'<select name="person_id">'
    for person_id in cur:
    	print						"<option value='%s'>%s</option>" % ( person_id[0] , person_id[1] )
    					
    print					'</select>'
    print					'</label>'
    print				'</div>'
    cur.execute("select test_type, name from Test_Type order by relative_order ASC;")
    print				'<div class="col-md-6">'
    print					'<label>Test Type'
    print					'<select name="test_type">'
    for test_type in cur:
    	print						'<option value="%s">%s</option>' % (test_type[0], test_type[1])
    print					'</select>'
    print					'</label>'
    print				'</div>'
    print			'</div>'
    #print			'<br><br>'

    #print			'<div class = "row">'
    #print				'<div class = "col-md-6">'
    #print					'<label> Serial Number:'
    #print						'<input name="serial_number" value="%s">'%serial_number
    #print					'</label>'
    #print				'</div>'
    #print			'</div>'

    print			'<br><br>'

    print			'<div class="row">'
    print				'<div class="col-md-4">'
    print					'<label>Successful?'
    print					"<INPUT type='checkbox' name='success'>"
    print					'</label>'
    print				'</div>'
    print			'</div>'
                                    
    print			'<br><br>'

    print			'<div class="row">'
    print				'<div class="col-md-6">'
    print					"<P>Attachment 1: <INPUT type='file' name='attach1'>"
    print					"<br><p>Attachment 2: <INPUT type='file' name='attach2'>"
    print					"<br><p>Attachment 3: <INPUT type='file' name='attach3'>"
    print				'</div>'
    print				'<div class="col-md-6">'
    print					'<p>Comments</p>'
    print					'<textarea rows="5" cols="50" name="comments"></textarea>'
    print				'</div>'
    print			'</div>'

    print			'<br><br><br><br>'

    print			'<div class="row">'
    print				'<div class="col-md-6">'
    print					'<input type="submit">'
    print				'</div>'
    print			'</div>'

    print			'<br><br><br><br>'

    print		'</form>'
