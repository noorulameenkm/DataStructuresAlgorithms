from heapq import *

"""
Space Complexity - O(N * logK)
Time Complexity - O(K)
"""

class Solution:
    def topKFrequent(self, words, k):
        frequency = {}
        minHeap = []
        
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        
        
        for word, frequency in frequency.items():
            if len(minHeap) < k:
                heappush(minHeap, Frequency(word, frequency))
            elif frequency > minHeap[0].frequency:
                heappop(minHeap)
                heappush(minHeap, Frequency(word, frequency))
            elif frequency == minHeap[0].frequency and word < minHeap[0].word:
                heappop(minHeap)
                heappush(minHeap, Frequency(word, frequency))
            
        result = []
        while len(minHeap):
            result.append(heappop(minHeap).word)
            
        return result[::-1]


class Frequency:
    def __init__(self, string, frequency):
        self.word = string
        self.frequency = frequency
        
    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word
        
        return self.frequency < other.frequency
        
    

def main():
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))

main()