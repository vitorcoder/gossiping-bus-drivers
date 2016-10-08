from busDriver import BusDriver
from busStop import BusStop
from routeRunner import RouteRunner

d1 = BusDriver(1, [3,1,2,3])
d2 = BusDriver(2, [3,2,3,1])
d3 = BusDriver(3, [4,2,3,4,5])

drivers = [d1, d2, d3]
stops = [BusStop(1), BusStop(2), BusStop(3), BusStop(4), BusStop(5)]

runner = RouteRunner(drivers, stops)

runner.runRoutes()