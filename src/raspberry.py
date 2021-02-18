# Raspberry abstraction
# It gets sensor temperature and powers on/off the resistor
# once the temperature is obtained, it is stored in the database

class Raspberry():
    # dt: seconds between sensor measures
    # target_temp: the temperature we are trying to reach
    def __init__(self, dt = 1, target_temp = 25):
        self.dt = dt
        self.target_temp = target_temp
        self.resistor_power = False
        pass

    # target_temp: the temperature we are trying to reach
    def setTartgetTemp(self, target_temp):
        self.target_temp = target_temp
    
    # control loop
    def loop(self):
        pass
    
    # access sensor to get the temperature
    def getTemp(self):
        return 42

    # current time
    def getTime(self):
        return 0

    # resistor
    def turnResistorOn(self):
        pass

    def turnResistorOff(self):
        pass