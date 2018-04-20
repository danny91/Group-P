import Adafruit_DHT
import time
import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import csv
import sys
csvfile = "temp.csv"
# Set Max Temp for email alert
maxtemp = '18'
# Set Max Humidity for Email Alert
#Email Login Info
gmail_user = '#'  
gmail_password = '#'
# Init email counter
emailcount = 0
#Loop continuous
als = True
while als:
 # Get temp info from temp sensor
 humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4) #on gpio pin 4
 #Check data exists
 if humidity is not None and temperature is not None:
      humidity = round(humidity, 2)
      temperature = str(temperature)
	  # Check if current temp is over max temp
      if temperature <= maxtemp:
       print 'Temp OK, Sleeping for 60 Seconds ' + temperature
      else:
	    # Check if email has already been sent
       if emailcount < 1:
		# Email info
        sent_from = gmail_user  
        to = ['#']      
        msg = MIMEMultipart()
        msg['From'] = '#'
        msg['To'] = '#'
        msg['Subject'] = 'Temp Alert'
        message = 'Alert, Temp over threshhold, Max Temp ' + maxtemp + ' current ' + temperature + '\nNo further Emails will be sent.'
        msg.attach(MIMEText(message))
        try:
		  #Send email and increment counter to prevent another email
          server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
          server.ehlo()
          server.login(gmail_user, gmail_password)
          server.sendmail(sent_from, to, msg.as_string())
          server.close()
          print 'Email sent!'
          emailcount = emailcount + 1
		# If something went wrong make sure the counter is 0
        except:  
          print 'Something went wrong...'
          emailcount = 0
       else:
	   # Still print updates if email already sent.
	    print 'Email already sent, not sending again. Temp over Limit ' + maxtemp + ' current ' + temperature
	  
	  # Fields for CSV
      timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
      data = [temperature, timeC]
	  #Write CSV
      with open(csvfile, "a")as output:
        writer = csv.writer(output, delimiter=",", lineterminator = '\n')
        writer.writerow(data)
	
	  # Sleep for 60 seconds
      time.sleep(60) # read data every minute
	 
# Handle no sensor errors	 
else:
     print 'can not connect to the sensor!'