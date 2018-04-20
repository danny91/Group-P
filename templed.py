import Adafruit_DHT
import time
from gpiozero import LED
from time import sleep
from myconfig import *
als = True
while als:
 led = LED(17)
 humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4) #on gpio pin 4
 temperature = str(temperature)
 if temperature >= maxtemp:
  ledon = True
  while ledon:
      led.on()
      sleep(1)
      led.off()
      sleep(1)
 else:
  time.sleep(60)