#!/usr/bin/python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
#GPIO.cleanup()
