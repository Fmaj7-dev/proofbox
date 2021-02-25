# Raspberry abstraction
# It gets sensor temperature and powers on/off the resistor
# once the temperature is obtained, it is stored in the database

import time

# it can be executed on raspberry or pc (only for testing)
using_raspberry = False

if using_raspberry:
    import Adafruit_DHT as dht
    import RPi.GPIO as GPIO

from database import Database
import numpy as np

class Raspberry():
    # dt: seconds between sensor measures
    # target_temp: the temperature we are trying to reach
    def __init__(self, database, dt = 1, target_temp = 25):
        self.database = database
        self.dt = dt
        self.target_temp = target_temp
        self.last_temp = 1
        self.last_humidity = 1
        self.resistor = False
        self.threshold = 0.1

        if using_raspberry:
            GPIO.setmode(GPIO.BCM)
            self.RELAIS_1_GPIO = 17
            GPIO.setup(self.RELAIS_1_GPIO, GPIO.OUT)
        

    # target_temp: the temperature we are trying to reach
    def setTartgetTemp(self, target_temp):
        self.target_temp = target_temp
    
    # control loop
    def loop(self):
        while True:
            if using_raspberry:
                self.getSensorTemp()
                if self.last_temp < (self.target_temp - self.threshold):
                    self.turnResistorOn()
                elif self.last_temp > (self.target_temp + self.threshold):
                    self.turnResistorOff()
            else:
                if self.resistor:
                    self.last_temp *= 1.1
                else:
                    self.last_temp *=0.999

                if self.last_temp < self.target_temp:
                    self.turnResistorOn()
                else:
                    self.turnResistorOff()

            min_resistor_temp = self.target_temp-3
            self.database.addValue( time.time(), self.last_temp, self.last_humidity, min_resistor_temp + self.resistor * 6, self.target_temp )

            print("current temperature: "+str(self.last_temp))
            time.sleep(self.dt)
    
    # access sensor to get the temperature
    def getSensorTemp(self):
        if using_raspberry:
            #Set DATA pin
            DHT = 12
            #Read Temp and Hum from DHT22
            h,t = dht.read_retry(dht.DHT22, DHT)
            self.last_temp = t
            self.last_humidity = h
        else:
            pass

    # current time
    def getTime(self):
        return 0

    # resistor
    def turnResistorOn(self):
        if using_raspberry:
            GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH)
        self.resistor = True

    def turnResistorOff(self):
        if using_raspberry:
            GPIO.output(self.RELAIS_1_GPIO, GPIO.LOW)
        self.resistor = False

    def getResistorState(self):
        return self.resistor

    def getAverageXMinutes(self, minutes):
        dts_per_minute = int(60/self.dt)
        total_dts = dts_per_minute * minutes
        total_dts = min(self.database.getSize(), total_dts)
        print(total_dts)
        return np.mean(self.database.getValuesY()[-total_dts:])
