#!/usr/bin/env python

import os
import sys
import subprocess 
import mysql.connector
import getpass

## Add tester in test DB
def add_tester( db ) : 
    try:
       cur = db.cursor()
       user = raw_input('Enter tester name : ')
       #print user
       cmd_user = 'INSERT INTO People set person_name="%s"' % (user)
       cur.execute(cmd_user) 
       db.commit()
    except mysql.connector.Error as err:
       print("<h3>lost DB connection!</h3>")

## Add test 
def add_test( db, nu ) : 
    try:
       testName     = raw_input('Enter test name : ')
       testDesShort = raw_input('Give short description : ')
       testDesLong  = raw_input('Give long description : ')
       cmd_test = 'insert into Test_Type set name="%s", required=1, desc_short="%s",desc_long="%s", relative_order=%d' % ( testName, testDesShort, testDesLong, nu )

       cur = db.cursor()
       cur.execute(cmd_test) 
       db.commit()
    except mysql.connector.Error as err:
       print("<h3>lost DB connection!</h3>")

## Grant Access 
def grant_access( db ) :
    try:

       cur = db.cursor()

       print 'DB Inserter Password : '
       inpw = getpass.getpass()
       cmd_gt  = "CREATE USER 'Inserter'@'localhost' IDENTIFIED BY '%s'" % (inpw)

       cur.execute(cmd_gt) 
       db.commit()
       cur.execute("GRANT INSERT ON ePortage.* TO 'Inserter'@'localhost'")
       db.commit()
       cur.execute("GRANT SELECT ON ePortage.* TO 'Inserter'@'localhost'")
       db.commit()

       print 'DB Reader Password : '
       rdpw = getpass.getpass()
       cmd_gt  = "CREATE USER 'ReadUser'@'localhost' IDENTIFIED BY '%s'" % (rdpw)
       cur.execute(cmd_gt) 
       db.commit()
       cur.execute("GRANT SELECT ON ePortage.* TO 'ReadUser'@'localhost'")
       db.commit()

       text_file = open("connect.py", "w")
       text_file.write("import mysql.connector \n")
       text_file.write("def connect( num ):\n")
       text_file.write("    if(num==1):\n")
       text_file.write("       cnx = mysql.connector.connect(user='Inserter', password='%s', database='ePortage')\n" % inpw )
       text_file.write("    if(num==0):\n")
       text_file.write("       cnx = mysql.connector.connect(user='ReadUser', password='%s', database='ePortage')\n'" % rdpw )

       text_file.write("    return cnx\n") 

       text_file.close()

    except mysql.connector.Error as err:
       print("<h3>lost DB connection!</h3>")



## Setup area
#os.system("mkdir hcalDB")
#dbhome = subprocess.check_output("pwd")
os.chdir( os.getenv("HOME") )
#os.chdir("public_html")
dbhome = os.getcwd() 
print dbhome 
os.system("git clone https://github.com/UMN-CMS/ePortage.git")
thePath = '%s%s' % (dbhome.rstrip() , "/ePortage/cms-cgi-scripts-v1/cgi-bin")
print thePath
os.chdir(thePath) 
os.system("chmod a+x *.py")
os.chdir("../..") 

#
os.chdir("sql/") 
print 'MySQL Root password '
pw = getpass.getpass()
db = mysql.connector.connect(user='root', password= pw , database='')

cur = db.cursor()
cur.execute("create database ePortage")
db.commit()
cur.execute("use ePortage")
db.commit()

source_cmd = "mysql -u root --password=" + pw + " ePortage < schema.sql " 
#print source_cmd 
os.system( source_cmd )

while True:
  add_tester( db ) 
  more_tester = raw_input(" Add more tester ? (Yes/No) " ) 
  if ( more_tester.lower() == 'no' or more_tester.lower() == 'n' ):
     break 

nu = 0 
while True:
  nu += 1 
  print ('Add test %d', nu ) 
  add_test( db, nu ) 
  more_test = raw_input(" Add more test ? (Yes/No) " ) 
  if ( more_test.lower() == 'no' or more_test.lower() == 'n' ):
     break 

grant_access( db )
os.system("chmod a+x connect.py")
os.system("mv connect.py ../cms-cgi-scripts-v1/cgi-bin/")

os.chdir("../cms-cgi-scripts-v1")
os.system("cp ../html/files/cmslogo.jpg static/files/")
os.system("cp ../html/files/us-cms.gif static/files/")

db.close()


