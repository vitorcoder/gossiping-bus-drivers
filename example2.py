from busDriver import BusDriver
from busStop import BusStop
from routeRunner import RouteRunner

d1 = BusDriver(1, [2,1,2])
d2 = BusDriver(2, [5,2,8])

drivers = [d1, d2]
stops = [BusStop(1), BusStop(2), BusStop(3), BusStop(4), BusStop(5), BusStop(6), BusStop(7), BusStop(8)]

runner = RouteRunner(drivers, stops)

runner.runRoutes()