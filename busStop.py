from collections import deque
from busDriver import BusDriver

class BusStop:
    
    
    def __init__(self, number):
        self.number = number
        self.currentDrivers = set();
        
    def findDriversInStop(self, drivers):
        result = set();
        
        for d in drivers:
            if d.currentStop == self.number:
                result.add(d)
        
        return result

        
    def checkGossips(self, drivers):
        
        self.currentDrivers = set()
        self.currentDrivers.update(self.findDriversInStop(drivers))
        
        while len(self.currentDrivers) > 0:
            driver = self.currentDrivers.pop()
            for d in self.currentDrivers:
                d.exchangeGossip(driver)    
           
                
        
        