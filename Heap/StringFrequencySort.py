from heapq import *

def sort_character_by_frequency(str_):
  # TODO: Write your code here
  frequency, minHeap = {}, []
  for i in range(len(str_)):
    if str_[i] not in frequency:
      frequency[str_[i]] = 0
    frequency[str_[i]] += 1

  for s, frequency in frequency.items():
    heappush(minHeap, (-frequency, s))

  string = ""
  while minHeap:
    freq_s = heappop(minHeap)
    string += freq_s[1] * -freq_s[0]

  return string


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
