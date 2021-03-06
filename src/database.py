# Temperature database.
# holds an array of temperatures


class Database():
    def __init__(self, max=3600):
        self.valuesX=[]
        self.valuesY=[]
        self.humidities=[]
        self.resistors=[]
        self.targets=[]
        self.max_values = max

    def addValue(self, valueX, valueY, humidity, resistor, target):
        self.valuesX.append(valueX)
        self.valuesY.append(valueY)
        self.humidities.append(humidity)
        self.resistors.append(resistor)
        self.targets.append(target)

        # keep at most self.max_values
        if(len(self.valuesX) > self.max_values):
            self.valuesX.pop(0)
            self.valuesY.pop(0)
            self.humidities.pop(0)
            self.resistors.pop(0)
            self.targets.pop(0)

    def getSize(self):
        return len(self.valuesX)

    def getValuesX(self):
        return self.valuesX

    def getValuesY(self):
        return self.valuesY

    def getHumidity(self):
        return self.humidities

    def getResistor(self):
        return self.resistors

    def getTarget(self):
        return self.targets