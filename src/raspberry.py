# Raspberry abstraction
# It gets sensor temperature and powers on/off the resistor
# once the temperature is obtained, it is stored in the database

import time

class Raspberry():
    # dt: seconds between sensor measures
    # target_temp: the temperature we are trying to reach
    def __init__(self, dt = 1, target_temp = 25):
        self.dt = dt
        self.target_temp = target_temp
        self.resistor_power = False
        self.last_temp = 0

        self.resistor = False
        pass

    # target_temp: the temperature we are trying to reach
    def setTartgetTemp(self, target_temp):
        self.target_temp = target_temp
    
    # control loop
    def loop(self):
        while True:
            if self.resistor:
                self.last_temp += 1
            else:
                self.last_temp *=0.99

            if self.last_temp < self.target_temp:
                self.turnResistorOn()
            else:
                self.turnResistorOff()

            print("current temperature: "+str(self.last_temp))
            time.sleep(self.dt)
    
    # access sensor to get the temperature
    def getTemp(self):
        return self.last_temp

    # current time
    def getTime(self):
        return 0

    # resistor
    def turnResistorOn(self):
        self.resistor = True

    def turnResistorOff(self):
        self.resistor = False