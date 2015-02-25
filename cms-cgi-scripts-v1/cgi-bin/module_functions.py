from connect import connect


def Portage_fetch(test_type_id, card_sn):
    db = connect(1)
    cur = db.cursor()
    cur.execute("SELECT People.person_name, Test.day, Test.successful, Test.comments, Test_Type.name, Test.test_id FROM Test, Test_Type, People, Card  WHERE Test_Type.test_type = %(test_id)s AND Card.sn = %(sn)s AND People.person_id = Test.person_id AND Test_Type.test_type=Test.test_type_id AND Test.card_id = Card.card_id ORDER BY Test.day ASC" %{'test_id':test_type_id, 'sn':card_sn})
    return cur.fetchall()

def Portage_fetch_attach(test_id):
    db = connect(1)
    cur = db.cursor()
    cur.execute('SELECT attach_id, attachmime, attachdesc, originalname FROM Attachments WHERE test_id=%(tid)s ORDER BY attach_id' % {'tid':test_id})
    return cur.fetchall()

def add_test_tab(sn, card_id):

    print 			'<div class="row">'
    print  				'<div class="col-md-8">'
    print  					'<h2><u>e-Portage for %d</u></h2>' %sn
    print  				'</div>'
    print 				'<div class="col-md-4">'
    print 					'<br><br><br><br>'
    print                   '<a href="add_test.py?card_id=%(id)d&serial_num=%(serial)d">' %{'serial':sn, 'id':card_id}
    print                          '<button> Add a New Test </button>'
    print                   '</a>'
    print 				'</div>'
    print 			'</div>'




def ePortageTest(test_type_id, card_sn, test_name):
    attempts =  Portage_fetch(test_type_id, card_sn) 
    print  			'<div class="row">'
    print           			'<div class="col-md-12">'
    print					'<h3> %(name)s </h3>' %{ "name":test_name}
    print					'<br>'

    n = 0
    for attempt in attempts:
        n += 1

        print       			'<h4>Attempt: %d</h4>'%n
        print				'<table class="table table-bordered table-striped Portage_table" style="width:60%">'
        print					    '<tbody>'
        print						'<tr>'
        print							'<th>Name</th>'
        print							'<th>Date</th>'
        print							'<th>Successful?</th>'
#        print							'<th>Comments</th>'
        print						'</tr>'
        print						'<tr>'
        print					                '<td> %(pname)s </td>' %{ "pname":attempt[0]}
        print					                '<td> %(when)s </td>' %{ "when":attempt[1]}
        if attempt[2] == 1:
			print					'<td>Yes</td>'
        else:
			print					'<td>No</td>'
        print						'</tr>'
        print						'<tr>'
        print					                '<td><b>Comments:</b></td>' 
        print					                '<td colspan=2> %(comm)s </td>' %{ "comm":attempt[3]}
        print						'</tr>'
        attachments=Portage_fetch_attach(attempt[5])
        for afile in attachments:
            print '<tr><td>Attachment: <a href="get_attach.py?attach_id=%s">%s</a><td colspan=2><i>%s</i></tr>' % (afile[0],afile[3],afile[2])
        
        print					    '</tbody>'
        print                               '</table>'
 					
    print			    '</div>'
    print		        '</div>'
    print                       '<hr><br>'


