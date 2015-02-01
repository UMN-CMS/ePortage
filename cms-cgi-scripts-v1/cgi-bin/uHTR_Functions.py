from connect import connect
def Portage_fetch(test_type_id, card_sn):
    db = connect(1)
    cur = db.cursor()
    cur.execute("SELECT people.person_name, test.day, test.successful, test.comments, test_type.name, test.test_id FROM test, test_type, people, card  WHERE test_type.test_type = %(test_id)s AND card.sn = %(sn)s AND people.person_id = test.person_id AND test_type.test_type=test.test_type_id AND test.card_id = card.card_id ORDER BY test.day ASC" %{'test_id':test_type_id, 'sn':card_sn})
    return cur.fetchall()





def add_test_tab(sn, mac, card_id):

    print 			'<div class="row">'
    print  				'<div class="col-md-4">'
    print  					'<h2><u>e-Portage for %s</u></h2>' %sn
    print  				'</div>'
    print 				'<div class="col-md-4">'
    print 					'<br><br>'
    print 					'<form action="add_test.py">'
    print 						'<label>Add New Test'
    print 							'<input type="submit">'
    print 							'<input type="hidden" name="serial_num" value= %s>' %sn
    print                                                        '<input type="hidden" name="mac" value= %s>' %mac
    print                                                        '<input type="hidden" name="card_id" value= %s>' %card_id
    print 						'</label>'
    print 					'</form>'
    print 				'</div>'
    print 			'</div>'




def ePortage(test_type_id, card_sn, test_name):
    t =  Portage_fetch(test_type_id, card_sn) 
    print  			'<div class="row">'
    print           			'<div class="col-md-12">'
    print					'<h3>%(d)s. %(name)s </h3>' %{"d": test_type_id, "name":test_name}
    print					'<br>'

    n = 0
    for attempts in t:
        n += 1

        print       			'<h4>Attempt: %d</h4>'%n
        print				'<table class="table table-bordered table-striped Portage_table" style="width:60%">'
        print					    '<tbody>'
        print						'<tr>'
        print							'<th>Name</th>'
        print							'<th>Date</th>'
        print							'<th>Success</th>'
        print							'<th>Comments</th>'
        print						'</tr>'
        print						'<tr>'

        for columns in attempts[:-2]:
            print		    				'<td>%s</td>' %columns

        print						'</tr>'
        print					    '</tbody>'
        print                               '</table>'
 					
    print			    '</div>'
    print		        '</div>'
    print                       '<hr><br>'


