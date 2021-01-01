from heapq import *
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        maxheap = []
        for seat in A:
            heappush(maxheap, -seat)
        profit = 0
        for i in range(B):
            pop = -heappop(maxheap)
            profit += pop
            heappush(maxheap, -(pop - 1))
        
        return profit




def main():
    print(Solution().solve([2,3], 3))
    print(Solution().solve([1,4], 2))



main()