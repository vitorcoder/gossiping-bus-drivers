import unittest
from busDriver import BusDriver

class BusDriverTest(unittest.TestCase):
    
    def test_moveSingleStop(self):
        d1 = BusDriver(1, [1])
        d1.travelToNextStop()
        d1.travelToNextStop()
        self.assertEqual(d1.currentStop, 1)
        
    def test_moveMultipleStops(self):
        d1 = BusDriver(1, [1, 5, 7])
        d1.travelToNextStop()
        self.assertEqual(d1.currentStop, 1)
        d1.travelToNextStop()
        self.assertEqual(d1.currentStop, 5)
        d1.travelToNextStop()
        self.assertEqual(d1.currentStop, 7)
        d1.travelToNextStop()
        self.assertEqual(d1.currentStop, 1)
        
    def test_exchangeSingleGossip(self):
        d1 = BusDriver(1, [1])
        d2 = BusDriver(2, [2])
        d1.exchangeGossip(d2)
        self.assertTrue(d1.gossip.issuperset([1,2]))
        self.assertTrue(d2.gossip.issuperset([1,2]))
        
    def test_exchangeMultipleGossips(self):
        d1 = BusDriver(1, [1])
        d2 = BusDriver(2, [2])
        d2.gossip.update([3])
        d1.exchangeGossip(d2)
        self.assertTrue(d1.gossip.issuperset([1,2,3]))
        self.assertTrue(d2.gossip.issuperset([1,2,3]))
        
        
if __name__ == '__main__':
    unittest.main()