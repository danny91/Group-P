from gpiozero import LED, Button
import time
import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import csv
import sys
from myconfig import *

ledon = False
led = LED(27)
button = Button(2)

# For easier demonstration Press rather than release
#button.wait_for_release()
button.wait_for_press()
ledon = True
led.on()
sent_from = gmail_user    
msg = MIMEMultipart()
msg['From'] = configemailfrom
msg['To'] = configemailto
msg['Subject'] = configsubjectbutton
message = 'Intruder Alert'
msg.attach(MIMEText(message))
#Send email and increment counter to prevent another email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, msg.as_string())
server.close()
print 'Email sent!'
# If something went wrong make sure the counter is 0

while ledon:
 led.on()
 time.sleep(900)