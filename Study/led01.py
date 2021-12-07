import RPi.GPIO as GPIO

import time

GPiO.setmode(GPIO.BOARD)

LED = 11
GPiO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try :
    while 1: #트루란 뜻
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
GPIO.cleanup()