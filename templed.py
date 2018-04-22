import Adafruit_DHT
import time
from gpiozero import LED
from time import sleep
from myconfig import *
als = True
#Define LED
led = LED(17)
# Ensure LED starts off
led.off()
#Loop until temp over max
while als:
 humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4) #on gpio pin 4
 temperature = str(temperature)
 if temperature >= maxtemp:
  ledon = True
  #Flash led until reset button pushed
  while ledon:
      led.on()
      sleep(0.5)
      led.off()
      sleep(0.5)
# If temp ok sleep for a min
 else:
  time.sleep(60)