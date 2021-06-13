
from heapq import *


"""
 Time Complexity - (N * logN)
 Space Complexity - O(N)
"""
def minimum_no_of_fuel_stops(target, start_fuel, stations):
    stops, miles, n = 0, 0, len(stations)
    max_heap = []
    
    for station in stations:

        while len(max_heap) > 0 and start_fuel + miles < station[0]:
            start_fuel += -heappop(max_heap)
            stops += 1

        if start_fuel + miles < station[0]:
            return -1

        heappush(max_heap, -station[1])
        start_fuel -= (station[0] - miles)
        miles = station[0]

    while len(max_heap) > 0 and start_fuel + miles < target:
        start_fuel += -heappop(max_heap)
        stops += 1
    
    if start_fuel + miles < target:
        return -1
    
    return stops


"""
Time Complexity - O(N^2)
Space Complexity - (N)
"""
def minRefuelStops(target, start_fuel, stations):
    dp = [start_fuel] + [0] * len(stations)
    for i, (location, capacity) in enumerate(stations):
        for t in range(i, -1, -1):
            if dp[t] >= location:
                dp[t+1] = max(dp[t+1], dp[t] + capacity)

    for i, d in enumerate(dp):
        if d >= target: return i
    return -1



# Test case 1
print(minimum_no_of_fuel_stops(target = 1, start_fuel = 1, stations = []))
print(minimum_no_of_fuel_stops(target = 100, start_fuel = 1, stations = [[10,100]]))
print(minimum_no_of_fuel_stops(target = 100, start_fuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))


# Test case 2
print(minRefuelStops(target = 1, start_fuel = 1, stations = []))
print(minRefuelStops(target = 100, start_fuel = 1, stations = [[10,100]]))
print(minRefuelStops(target = 100, start_fuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))


         
