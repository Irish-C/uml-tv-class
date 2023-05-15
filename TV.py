# Define TV class
class TV:
    # constructor attributes of an TV object
    def __init__(self):
        self.channel = 1        # sets initial channel to 1
        self.volumeLevel = 1    # sets initial volume to 1
        self.on = False         # sets initial on to False if TV is initially turned off
    

    # a method that returns True when TV is on
    def turnOn(self):
        self.on = True

    # a method that return False when TV is off
    def turnOff(self):
        self.on = False
    
    # a method that returns the channel
    def getChannel(self):
        return self.channel