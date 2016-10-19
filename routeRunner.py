from busDriver import BusDriver
from busStop import BusStop

class RouteRunner:
    
    def __init__(self, drivers, stops):
        self.drivers = drivers
        self.stops = stops


    def runRoutes(self):
        i = 1
        
        
        while i < 481:
        
            print "minute {}".format(i)
            for d in self.drivers:
                d.travelToNextStop()
                print "   driver {} is int stop {}".format(d.name, d.currentStop) 
            
                
            for s in self.stops:
                s.checkGossips(self.drivers)
                
            print " current gossips"
            
            finish = True
            
            for d in self.drivers:
                print "   driver {} has gossips {}".format(d.name, d.gossip)
                if len(d.gossip) != len(self.drivers):
                    finish = False
                
            if finish:
                break 
            else:
                print "need another iteration to spread all gossips to all drivers" 
            
            i+=1
                
        if i < 481:
            print "gossips where spread to all drivers in {} minutes!".format(i)
            return i
        else:
            print "the drivers never will know all gossips"
            return None
        