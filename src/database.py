# Temperature database.
# holds an array of temperatures


class Database():
    def __init__(self, max=3600):
        self.valuesX=[]
        self.valuesY=[]
        self.max_values = max

    def addValue(self, valueX, valueY):
        self.valuesX.append(valueX)
        self.valuesY.append(valueY)

    def getSize(self):
        return len(self.valuesX)

    def getValuesX(self):
        return self.valuesX

    def getValuesY(self):
        return self.valuesY