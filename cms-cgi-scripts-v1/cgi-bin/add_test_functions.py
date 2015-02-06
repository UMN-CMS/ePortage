from connect import connect
import mysql.connector
import base
import cgi, os
import cgitb; cgitb.enable()


def add_test(person_id, test_type, serial_num, success, file1='', file2='', file3='', comments='', file1desc='', file1comment='', file2desc='', file2comment='', file3desc='',file3comment=''):
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
  
	dc = connect(0)
    	sor = dc.cursor()
	sor.execute("SELECT test_id from Test order by day DESC;")
	id1 = sor.fetchone()
	id = id1[0]
	
	if file1.filename or file2.filename or file3.filename: 
		dd = connect(1)
		cus = dd.cursor()

		if file1.filename:
			fn = os.path.basename(file1.filename)
			open('files/' + fn, 'wb').write(file1.file.read())
			print '<div> The file %s was uploaded successfully. </div>' % (fn)
			cus.execute("INSERT INTO Attachments SET test_id=%s, attachdesc = '%s', comments = '%s', attachpath = '%s';" % ( id, file1desc, file1comment, fn ))

		if file2.filename:
			fn2 = os.path.basename(file2.filename)
			open('files/' + fn2, 'wb').write(file2.file.read())
			print '<div> The file %s was uploaded successfully. </div>' % (fn2)
			cus.execute("INSERT INTO Attachments SET test_id=%s, attachdesc = '%s', comments = '%s', attachpath = '%s';" % ( id, file2desc, file2comment, fn2 ))

		if file3.filename:
			fn3 = os.path.basename(file3.filename)
			open('files/' + fn3, 'wb').write(file3.file.read())
			print '<div> The file %s was uploaded successfully. </div>' % (fn3)
			cus.execute("INSERT INTO Attachments SET test_id=%s, attachdesc = '%s', comments = '%s', attachpath = '%s';" % ( id, file3desc, file3comment, fn3 ))	
	
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

    print		'<form action="add_test2.py" method="post" enctype="multipart/form-data">'
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
    print 					"<p>Description: </p>"
    print					'<textarea rows = "1" cols="35" name="file1desc"></textarea>'
    print					'<p>Attachment comments:</p>'
    print					'<textarea rows = "2" cols="35" name="file1comment"></textarea>'	

    print					"<br><br><p>Attachment 2: <INPUT type='file' name='attach2'>"
    print 					"<p>Description: </p>"
    print					'<textarea rows = "1" cols="35" name="file2desc"></textarea>'
    print					'<p>Attachment comments:</p>'
    print					'<textarea rows = "2" cols="35" name="file2comment"></textarea>'

    print					"<br><br><p>Attachment 3: <INPUT type='file' name='attach3'>"
    print 					"<p>Description: </p>"
    print					'<textarea rows = "1" cols="35" name="file3desc"></textarea>'
    print					'<p>Attachment comments:</p>'
    print					'<textarea rows = "2" cols="35" name="file3comment"></textarea>'   
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
