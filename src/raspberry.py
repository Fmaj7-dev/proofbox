# Raspberry abstraction
# It gets sensor temperature and powers on/off the resistor
# once the temperature is obtained, it is stored in the database

import time
from database import Database

class Raspberry():
    # dt: seconds between sensor measures
    # target_temp: the temperature we are trying to reach
    def __init__(self, database, dt = 1, target_temp = 25):
        self.database = database
        self.dt = dt
        self.target_temp = target_temp
        self.resistor_power = False
        self.last_temp = 1

        self.resistor = False
        pass

    # target_temp: the temperature we are trying to reach
    def setTartgetTemp(self, target_temp):
        self.target_temp = target_temp
    
    # control loop
    def loop(self):
        while True:
            ######################
            # test
            ######################
            if self.resistor:
                self.last_temp *= 1.1
            else:
                self.last_temp *=0.999

            if self.last_temp < self.target_temp:
                self.turnResistorOn()
            else:
                self.turnResistorOff()

            #######################
            # production
            #######################
            ## naive approach
            # self.last_temp = self.getSensorTemp()
            # if self.last_temp < self.target_temp:
            #   self.turnResistorOn()
            # else
            #   self.turnResistorOff()
            self.database.addValue( time.time(), self.last_temp )

            print("current temperature: "+str(self.last_temp))
            time.sleep(self.dt)
    
    # access sensor to get the temperature
    def getSensorTemp(self):
        pass

    # current time
    def getTime(self):
        return 0

    # resistor
    def turnResistorOn(self):
        self.resistor = True

    def turnResistorOff(self):
        self.resistor = False