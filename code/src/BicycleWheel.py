import math

class BicycleWheel():
    def __init__(self):
        self.FILE_PATH = 'savedFile.txt'
        self.MIN_SPOKES = 8
        
        self.wheelSize = 80.0
        self.hubSize = 10.0
        self.numberOfSpokes = self.MIN_SPOKES 
    
    def getMinWheelSizeAllowance(self):
        return self.hubSize*4
    
    def getMaxHubSizeAllowance(self):
        return self.wheelSize/4
    
    def setWheelSize(self, wheelSize):
        if self.hubSize <= (wheelSize/4):
            self.wheelSize = wheelSize
        
    def setHubSize(self, hubSize):
        if hubSize <= (self.wheelSize/4):
            self.hubSize = hubSize
        
    def setNumberOfSpokes(self, numberOfSpokes):
        if numberOfSpokes >= 8:
            self.numberOfSpokes = numberOfSpokes
            
    def getAngleOfSpokes(self):
        return (2*math.pi)/self.numberOfSpokes
    
    def getPositionOfSpokes(self):
        positionList = [[0 for x in range (4)] for y in range(self.numberOfSpokes)]
        for i in range (self.numberOfSpokes):
            xWheel = self.wheelSize + self.wheelSize * math.cos(i*self.getAngleOfSpokes())
            yWheel = self.wheelSize - self.wheelSize * math.sin(i*self.getAngleOfSpokes())
            xHub = self.wheelSize + self.hubSize * math.cos(i*self.getAngleOfSpokes())
            yHub = self.wheelSize - self.hubSize * math.sin(i*self.getAngleOfSpokes())
            positionList[i] = [xWheel, yWheel, xHub, yHub]
        return positionList
        
    def loadFile(self, path):
        try:
            with open(path, 'r') as file:
                self.wheelSize = float(file.readline())
                self.hubSize = float(file.readline())
                self.numberOfSpokes = int(file.readline())
                file.close()
                return [self.wheelSize, self.hubSize, self.numberOfSpokes]
        except IOError: pass
            
    def saveFile(self, path):
        data = str(self.wheelSize) + "\n" + str(self.hubSize) + "\n" + str(self.numberOfSpokes) + "\n"
        with open(path, 'w') as file:
            file.write(data)
            file.close()

        
            

            
        

        