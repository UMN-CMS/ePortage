from connect import connect
import base


def add_test(person_id, test_type, serial_num, success, file1='', file2='', file3='', comments=''):
    if success:
        success = 1
    else:
        success = 0

    db = connect(1)
    cur = db.cursor()

    if serial_num:
        cur.execute("SELECT card_id FROM card WHERE sn = %(n)s" %{"n":serial_num})
        row = cur.fetchone()
        card_id = row[0]
        

        cur.execute("INSERT INTO test (person_id, test_type_id, card_id, test_id, successful, day, comments) VALUES (%(pers_id)s, %(test_typ)s, %(card)s, NULL, %(succ)s, NOW(), '%(comment)s')"%{"pers_id": person_id, "test_typ": test_type, "card": card_id, "succ":success, "comment":comments})
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

    print		'<form action="add_test2.py" method="post">'

    print			'<div class="row">'
    print				'<div class="col-md-12">'
    print					'<h1>Add Test for Card %s</h1>' %serial_number
    print				'</div>'
    print			'</div>'

    print			'<br><br>'

    print			'<div class="row">'
    print				'<div class="col-md-6">'
    print					'<label>Tester'
    print					'<select name="person_id">'
    print						"<option value='1'>Michael</option>"
    print						"<option value='2'>Asad</option>"
    print						"<option value='3'>Quynh</option>"				
    print					'</select>'
    print					'</label>'
    print				'</div>'
    print				'<div class="col-md-6">'
    print					'<label>Test Type'
    print					'<select name="test_type">'
    print						'<option value="1">Internal links Lumi</option>'
    print						'<option value="2">Internal links F2B</option>'
    print						'<option value="3">Internal links IP Bus</option>'
    print						'<option value="4">I2C communication to mezz</option>'
    print						'<option value="5">I2C communication to SPF</option>'
    print						'<option value="6">I2C communication to PPOD</option>'
    print						'<option value="7">SDRAM</option>'
    print						'<option value="8">Firmware Reload</option>'
    print						'<option value="9">MMC Operation</option>'
    print					'</select>'
    print					'</label>'
    print				'</div>'
    print			'</div>'

    print			'<br><br>'

    print			'<div class = "row">'
    print				'<div class = "col-md-6">'
    print					'<label> Serial Number:'
    print						'<input name="serial_number" value="%s">'%serial_number
    print					'</label>'
    print				'</div>'
    print			'</div>'

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
    print					'<textarea name="comments"></textarea>'
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
