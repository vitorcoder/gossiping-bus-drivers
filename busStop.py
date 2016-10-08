from collections import deque
from busDriver import BusDriver

class BusStop:
    
    
    def __init__(self, number):
        self.number = number
        self.currentDrivers = set();
        
    def checkGossips(self, drivers):
        for d in drivers:
            if d.currentStop == self.number:
                self.currentDrivers.add(d)
                
        while len(self.currentDrivers) > 0:
            driver = self.currentDrivers.pop()
            for d in self.currentDrivers:
                d.exchangeGossip(driver)    
                    
        self.currentDrivers = set()        
        
        