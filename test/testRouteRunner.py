import unittest
from busStop import BusStop
from busDriver import BusDriver
from routeRunner import RouteRunner

class RouteRunnerTest(unittest.TestCase):
    
    def test_example1(self):
        d1 = BusDriver(1, [3,1,2,3])
        d2 = BusDriver(2, [3,2,3,1])
        d3 = BusDriver(3, [4,2,3,4,5])

        drivers = [d1, d2, d3]
        stops = [BusStop(1), BusStop(2), BusStop(3), BusStop(4), BusStop(5)]

        runner = RouteRunner(drivers, stops)

        time = runner.runRoutes()

        self.assertEqual(time, 5)
        
    def test_example2(self):
        d1 = BusDriver(1, [2,1,2])
        d2 = BusDriver(2, [5,2,8])

        drivers = [d1, d2]
        stops = [BusStop(1), BusStop(2), BusStop(3), BusStop(4), BusStop(5), BusStop(6), BusStop(7), BusStop(8)]

        runner = RouteRunner(drivers, stops)

        time = runner.runRoutes()

        self.assertEqual(time, None)
        
        
        
if __name__ == '__main__':
    unittest.main()