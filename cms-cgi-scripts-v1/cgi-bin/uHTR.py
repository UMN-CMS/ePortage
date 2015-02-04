#!/usr/bin/python

import cgi
import base
import HomePageList
import uHTR_Functions

#cgi header
print "Content-type: text/html\n"


form = cgi.FieldStorage()
card_id = form.getvalue('card_id')
serial_num = form.getvalue('serial_num')

base.header(title='uHTR ePortage')
base.top()
print 'card_id = ', card_id
print  'serial_num = ', serial_num

uHTR_Functions.add_test_tab(serial_num, card_id)

uHTR_Functions.ePortage(1, serial_num, 'Internal links Lumi')
uHTR_Functions.ePortage(2, serial_num, 'Internal links F2B')
uHTR_Functions.ePortage(3, serial_num, 'Internal links IP Bus')
uHTR_Functions.ePortage(4, serial_num, 'I2C communication to mezz')
uHTR_Functions.ePortage(5, serial_num, 'I2C communication to SPF')
uHTR_Functions.ePortage(6, serial_num, 'I2C communication to PPoD')
uHTR_Functions.ePortage(7, serial_num, 'SDRAM')
uHTR_Functions.ePortage(8, serial_num, 'Firmware reload')
uHTR_Functions.ePortage(9, serial_num, 'MMC Operation')


base.bottom()
