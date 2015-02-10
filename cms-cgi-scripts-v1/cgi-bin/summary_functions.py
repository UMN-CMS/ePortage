from connect import connect
import mysql.connector

def get():
    
    db = connect(0)
    cur = db.cursor()
    
    cur.execute("SELECT sn, Mac_address, Card_id FROM Card ORDER by sn ASC")
    rows = cur.fetchall()
 
    
    serial_numbers = []
    for card in rows:
        serial_numbers.append(card[0])
        
    pass_dic = dict()
    for sn in serial_numbers:
        cur.execute("SELECT Test_Type.name FROM Test_Type, Card, Test WHERE Card.sn = %(n)s And Test.card_id = Card.card_id AND Test_Type.test_type = Test.test_type_id AND Test_Type.required =1 AND Test.successful = 1" %{"n": sn})
        passed = cur.fetchall()
        temp1 = []
        for x in passed:
            if x[0] not in temp1:
                temp1.append(x[0])
        pass_dic[sn] = temp1

    list_of_all_required_tests = []
    cur.execute("SELECT name FROM Test_Type WHERE Test_Type.required = 1")
    for names in cur:
        list_of_all_required_tests.append(names[0])
    

    List_of_lists = []
    for tests in rows:
        small_list = []
        rem_list = []
        for items in tests:
            small_list.append(items)
        small_list.append(pass_dic[tests[0]])
        for remaining in list_of_all_required_tests:
            if remaining not in pass_dic[tests[0]]:
                rem_list.append(remaining)
        small_list.append(rem_list)
        List_of_lists.append(small_list)

    return List_of_lists
