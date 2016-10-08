from collections import deque

class BusDriver:
    
    
    def __init__(self, driverName, route):
        self.gossip = set()
        self.name = driverName
        self.gossip.add(driverName)
        self.route = deque(route)
        self.currentStop = None
    
    def exchangeGossip(self, otherDriver):
        self.gossip.update(otherDriver.gossip)
        otherDriver.gossip.update(self.gossip)
        
    def travelToNextStop(self):
        if self.currentStop != None:
            self.route.append(self.currentStop)
        
        self.currentStop = self.route.popleft()
        