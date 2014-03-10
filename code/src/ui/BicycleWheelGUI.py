import sys
sys.path.append('code/src')
from BicycleWheel import * 
from Tkinter import * 
root = Tk()

class BicycleWheelGUI():
    def __init__(self):
        self.text = Text(root)
        self.wheel = BicycleWheel()
        self.OFFSET = 4
        self.MAXSIZE = 250 
          
    def getWheelCenter(self):
        return self.wheel.wheelSize + self.OFFSET    
        
    def drawCircle(self, radius):
        self.canvas.create_oval( self.getWheelCenter() - radius, self.getWheelCenter() - radius, self.getWheelCenter() + radius, self.getWheelCenter() + radius)
    
    def drawSpokes(self, numberOfSpokes, listOfSpokes):
        for i in range(numberOfSpokes):
            self.canvas.create_line(listOfSpokes[i][0] + self.OFFSET, listOfSpokes[i][1]+ self.OFFSET, listOfSpokes[i][2]+ self.OFFSET, listOfSpokes[i][3]+ self.OFFSET)
    
    def createWheelSlider(self):
        self.newWheelSlider = Scale( self.menuFrame, from_ = int(self.wheel.getMinWheelSizeAllowance()), to = self.MAXSIZE, orient = HORIZONTAL, label = "Wheel Radius:", command = self.onUpdateWheelSlider, tickinterval = (self.MAXSIZE - self.wheel.getMinWheelSizeAllowance())/5, length = 250)
        self.newWheelSlider.set(self.wheel.wheelSize)
        self.newWheelSlider.grid(row = 0, column = 0)
    
    def createHubSlider(self):
        self.newHubSlider = Scale(self.menuFrame, from_ = 0, to = int(self.wheel.getMaxHubSizeAllowance()), orient = HORIZONTAL, label = "Hub Radius:", resolution = 0.05, command = self.onUpdateWheelHubSlider, tickinterval = self.wheel.getMaxHubSizeAllowance()/5, length = 250)
        self.newHubSlider.set(self.wheel.hubSize)
        self.newHubSlider.grid(row = 1, column = 0)
    
    def createSpokesSlider(self):
        self.newSpokesSlider  = Scale(self.menuFrame, from_ = self.wheel.MIN_SPOKES, to = self.MAXSIZE, orient = HORIZONTAL, label = "Number Of Spokes:", command = self.onUpdateWheelNumberOfSpokes, tickinterval = self.MAXSIZE/5, length = 250)
        self.newSpokesSlider.set(self.wheel.numberOfSpokes)
        self.newSpokesSlider.grid(row = 2, column =0)
        
    def createMenuFrame(self):
        self.menuFrame = Frame(root)
        self.menuFrame.pack(side = "right")
        
    def createMenu(self):
        self.createWheelSlider()
        self.createHubSlider() 
        self.createSpokesSlider()  
        
        self.save = Button(self.menuFrame,text = 'Save', command = self.onSave)
        self.save.grid(row = 4, column = 0)
        
        self.load = Button(self.menuFrame,text = 'Load', command = self.onLoad)
        self.load.grid(row = 5, column = 0)

    def clearCanvas(self):
        self.canvas.delete("all")
        
    def createWheelFrame(self):
        self.wheelFrame  = Frame(root)
        self.wheelFrame.pack(side = 'left', expand  = True)
        self.canvas = Canvas(self.wheelFrame, bg ="white", width = 2*(self.MAXSIZE+self.OFFSET), height = 2*(self.MAXSIZE+self.OFFSET))
        self.canvas.pack()
    
    def drawWheel(self):
        self.drawCircle(self.wheel.wheelSize)
        self.drawCircle(self.wheel.hubSize)
        self.drawSpokes(self.wheel.numberOfSpokes, self.wheel.getPositionOfSpokes())

    def onUpdateWheelSlider(self, wheelSize):
        if float(wheelSize) != self.wheel.wheelSize:
            self.wheel.setWheelSize(float(wheelSize))
            self.updateWheel()
            self.createHubSlider()
            
    def onUpdateWheelHubSlider(self, hubSize):   
        if float(hubSize) != self.wheel.hubSize:
            self.wheel.setHubSize(float(hubSize))
            self.updateWheel()
            self.createWheelSlider()
            
    def onUpdateWheelNumberOfSpokes(self, numberOfSpokes):
        self.wheel.setNumberOfSpokes(int(numberOfSpokes))
        self.updateWheel()
            
    def updateWheel(self):
        self.clearCanvas()
        self.drawWheel()
 
    def onSave(self):
        self.wheel.saveFile(self.wheel.FILE_PATH)
       
    def onLoad(self):
        self.wheel.loadFile(self.wheel.FILE_PATH)
        self.updateWheel()
        self.createMenu()
    
    def onCreate(self):
        self.createWheelFrame()        
        self.drawWheel()
        self.createMenuFrame()
        self.createMenu()
        root.mainloop()
        
if __name__ == '__main__':
    
    gui = BicycleWheelGUI()
    gui.onCreate()