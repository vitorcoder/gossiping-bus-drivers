class BusDriver:
    
    
    def __init__(self, driverName):
        self.gossip = set()
        self.gossip.add(driverName)
    
    def exchangeGossip(self, otherDriver):
        self.gossip.update(otherDriver.gossip)
        otherDriver.gossip.update(self.gossip)
        
    