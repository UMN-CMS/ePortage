from connect import connect
import mysql.connector
import base
import cgi, os
import cgitb; cgitb.enable()
import settings

def add_test(person_id, test_type, serial_num, success, comments):
    if success:
        success = 1
    else:
        success = 0

    db = connect(1)
    cur = db.cursor()

    if serial_num:
        cur.execute("SELECT card_id FROM Card WHERE sn = %(n)d" %{"n":serial_num})
        row = cur.fetchone()
        card_id = row[0]
        
        sql="INSERT INTO Test (person_id, test_type_id, card_id, successful, comments, day) VALUES (%s,%s,%s,%s,%s,NOW())"
        # This is safer because Python takes care of escaping any illegal/invalid text
        items=(person_id,test_type,card_id,success,comments)
        cur.execute(sql,items)
        test_id = cur.lastrowid

        db.commit()

        return test_id        
    else:
        print '<div class ="row">'
 	print			'<div class = "col-md-3">'
 	print                       '<h3> Attempt Failed. Please Specify Serial Number </h3>'
 	print                   '</div>'
 	print  '</div>'

 	add_test_template(serial_num)


def add_test_attachment(test_id, afile, desc, comments):
    if afile.filename:
        db = connect(1)
        cur = db.cursor()
        originalname = os.path.basename(afile.filename)
        
        cur.execute("INSERT INTO Attachments (test_id,attachmime,attachdesc,comments,originalname) VALUES (%s,%s,%s,%s,%s)",
                    (test_id,afile.type,desc,comments,originalname));
        att_id=cur.lastrowid
        db.commit()
        ofn=settings.getAttachmentPathFor(int(test_id),int(att_id));
        sub_path = os.path.dirname(ofn)
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)
        open(ofn,'wb').write(afile.file.read())
        print '<div> The file %s was uploaded successfully. </div>' % (originalname)
    
def add_test_template(serial_number,suggested_test):
    if not suggested_test:
        suggested_test=0
    db = connect(0)
    cur = db.cursor()

    print		'<form action="add_test2.py" method="post" enctype="multipart/form-data">'
    print 			'<INPUT TYPE="hidden" name="serial_number" value="%d">' % (serial_number)
    print			'<div class="row">'
    print				'<div class="col-md-12">'
    print					'<h1>Add Test for Card %d</h1>' %serial_number
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
        if test_type[0] == suggested_test:
            print						'<option value="%s" selected>%s</option>' % (test_type[0], test_type[1])
        else:
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
    print				'<div class="col-md-3">'
    print					'<label>Successful?'
    print					"<INPUT type='checkbox' name='success' value='1'>"
    print					'</label>'
    print				'</div>'
    print				'<div class="col-md-9">'
    print					'<label>Comments (Manditory)</label><p>'
    print					'<textarea rows="5" cols="50" name="comments"></textarea>'
    print				'</div>'
    print			'</div>'
                                    
    print			'<br><br>'
    print			'<div class="row">'
    print				'<div class="col-md-6">'
    print					'<input type="submit" value="Add Test">'
    print				'</div>'
    print			'</div>'
    for iattach in (1,2,3):
        print			'<br><hr><br>'    
        print			'<div class="row">'
        print				'<div class="col-md-2">'
        print					"<b>Attachment %d:</b>" % (iattach)
        print				'</div><div class="col-md-5">'
        print					"<INPUT type='file' name='attach%d'>"% (iattach)	
        print				'</div><div class="col-md-5">'
        print 					"<label>Description:</label> <INPUT type='text' class='form-control' name='attachdesc%d'>"% (iattach)	
        print                           '</div>'
        print                   '</div>'
        print			'<div class="row">'
        print				'<div class="col-md-10 col-md-offset-2">'
        print					'<label>Comments:</label>'
        print					'<textarea rows = "2" cols="50" class="form-control" name="attachcomment%d"></textarea>' % (iattach)	
        print                               '</div>'
        print                       '</div>'

    print			'<br><br><br><br>'

    print			'<div class="row">'
    print				'<div class="col-md-6">'
    print					'<input type="submit" value="Add Test">'
    print				'</div>'
    print			'</div>'

    print			'<br><br><br><br>'

    print		'</form>'
