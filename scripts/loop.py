#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

RELAIS_1_GPIO = 17


for i in range(10):

    print("LOW")
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    print(GPIO.input(channel))
    time.sleep(60)

    print("HIGH")
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    print(GPIO.input(channel))
    time.sleep(60)
