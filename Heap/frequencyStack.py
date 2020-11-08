from heapq import *


"""
Time Complexity - O(logN)
Space Complexity - O(N)
"""

class FrequencyStack:
  sequenceNumber = 0
  maxHeap = []
  frequency = {}

  def push(self, num):
    self.frequency[num] = self.frequency.get(num, 0) + 1
    heappush(self.maxHeap, Element(num, self.frequency[num], self.sequenceNumber))
    self.sequenceNumber += 1


  def pop(self):
    number = heappop(self.maxHeap).number
    if self.frequency[number] > 1:
      self.frequency[number] -= 1
    else:
      del self.frequency[number]

    return number



class Element:
  def __init__(self, number, frequency, sequence):
    self.number = number
    self.frequency = frequency
    self.sequence = sequence


  def __lt__(self, other):
    if self.frequency != other.frequency:
      return self.frequency > other.frequency

    return self.sequence > other.sequence


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()







