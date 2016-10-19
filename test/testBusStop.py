import unittest
from busStop import BusStop
from busDriver import BusDriver

class BusStopTest(unittest.TestCase):
    
    def test_checkDriversOnStop(self):
        d1 = BusDriver(1, [1, 2])
        d2 = BusDriver(2, [3, 2])
        d3 = BusDriver(2, [1, 3])
        
        drivers = [d1, d2, d3]

        stop1 = BusStop(1)
        stop2 = BusStop(2)
        stop3 = BusStop(3)

        d1.travelToNextStop()
        d2.travelToNextStop()
        d3.travelToNextStop()
        
        result1 = stop1.findDriversInStop(drivers)
        result2 = stop2.findDriversInStop(drivers)
        result3 = stop3.findDriversInStop(drivers)
        
        self.assertTrue(result1.issuperset([d1, d3]))
        self.assertTrue(len(result2) == 0)
        self.assertTrue(result3.issuperset([d2]))
        
        
        d1.travelToNextStop()
        d2.travelToNextStop()
        d3.travelToNextStop()
        
        result1 = stop1.findDriversInStop(drivers)
        result2 = stop2.findDriversInStop(drivers)
        result3 = stop3.findDriversInStop(drivers)
        
        self.assertTrue(len(result1) == 0)
        self.assertTrue(result2.issuperset([d1, d2]))
        self.assertTrue(result3.issuperset([d3]))
        
        
        
        
if __name__ == '__main__':
    unittest.main()