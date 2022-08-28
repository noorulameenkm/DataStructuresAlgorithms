from heapq import *


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.distance_from_user() > other.distance_from_user()

    def distance_from_user(self):
        return (self.x * self.x) + (self.y * self.y)
    
    def print_location(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


"""
    Time Complexity - O(NlogK)
    Space Complexity - O(K)
"""
def find_closest_drivers(locations, k):
    heap = []
    for i in range(k):
        heappush(heap, locations[i])
    
    for i in range(k, len(locations)):
        if locations[i].distance_from_user() < heap[0].distance_from_user():
            heappop(heap)
            heappush(heap, locations[i])
    
    return list(heap)


result = find_closest_drivers([Location(1, 3), Location(3, 4), Location(2, -1)], 2)
print("Here are the k drivers locations closest to the user in the Seattle area: ", end='')
for location in result:
  location.print_location()