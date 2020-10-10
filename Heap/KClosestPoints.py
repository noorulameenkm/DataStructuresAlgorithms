from math import *
from heapq import *

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
  
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()

  def distance_from_origin(self):
    return sqrt(pow(self.x, 2) + pow(self.y, 2))

def find_closest_points(points, k):
  result = []
  # TODO: Write your code here
  minHeap = []
  for i in range(k):
    heappush(minHeap, points[i])

  for j in range(k, len(points)):
    if points[j].distance_from_origin() < minHeap[0].distance_from_origin():
      heappop(minHeap)
      heappush(minHeap, points[j])

  return list(minHeap)
  

def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()


