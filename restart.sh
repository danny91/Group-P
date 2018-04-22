#!/bin/bash
#restart intrusion switch
kill $(pgrep -f 'python /home/pi/project/button.py')
python ~/project/button.py &
#restart temp monitor
kill $(pgrep -f 'python /home/pi/project/python.py')
python ~/project/python.py &
#restart temp LED
kill $(pgrep -f 'python /home/pi/project/templed.py')
python ~/project/templed.py &