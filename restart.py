from gpiozero import Button
import sys
import os
#define button
button = Button(22)
#loop each press
while True:
 button.wait_for_press()
 os.system('./restart.sh')