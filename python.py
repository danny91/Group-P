import Adafruit_DHT
import time
import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass
als = True
# Set Max Temp for email alert
maxtemp = 15
# Set Max Humidity for Email Alert

while als: 
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4) #on gpio pin 4 or pin 7
    if humidity is not None and temperature is not None:
      humidity = round(humidity, 2)
      temperature = str(temperature)
      if temperature <= maxtemp:
       time.sleep(60) # read data every minute
      else:
       gmail_user = '#'  
       gmail_password = '#'
       
       sent_from = gmail_user  
       to = ['#']  
       subject = 'Temp Alert'  
       body = 'Alert, Temp over threshhold' + temperature
       
       email_text = """\  
       From: %s  
       To: %s  
       Subject: %s
       
       %s
       """ % (sent_from, ", ".join(to), subject, body)

       try:  
         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
         server.ehlo()
         server.login(gmail_user, gmail_password)
         server.sendmail(sent_from, to, email_text)
         server.close()
         print 'Email sent!'
       except:  
         print 'Something went wrong...'
       
       time.sleep(6000) # read data every minute

      #print 'Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity)
      #print temperature1
    else:
      print 'can not connect to the sensor!'