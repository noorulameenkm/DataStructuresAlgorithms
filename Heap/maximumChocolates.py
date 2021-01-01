from heapq import *
import math
from collections import deque

class Solution:
	def nchoc(self, A, B):
	    total_chocolates = 0
	    maxheap = []
	    for num in B:
	        heappush(maxheap, -num)
	       
	    for _ in range(A):
	        pop = -heappop(maxheap)
	        total_chocolates += pop
	       
	        heappush(maxheap, -math.floor( pop / 2 ))
	   
	    return total_chocolates % 1000000007



def nchoc2(A, B):
    total_chocolates = 0
    B.sort(reverse=True)
    j = 0
    queue = deque()
    for _ in range(A):
        if len(queue) == 0:
            total_chocolates += B[j]
            queue.append(B[j] // 2)
            j += 1
        else:
            if B[j] >= queue[0]:
                total_chocolates += B[j]
                queue.append(B[j] // 2)
                j += 1
            else:
                a = queue.popleft()
                total_chocolates += a
                queue.append(a // 2)
        
        if j == len(B):
            B = list(queue)
            queue = deque()
            j = 0
    
    return total_chocolates % (pow(10, 9) + 7)
                
	       



def main():
    # First Solution
    print(Solution().nchoc(3, [6, 5]))
    print(Solution().nchoc(5, [2, 4, 6, 8, 10]))

    # Second Solution
    print(nchoc2(3, [6, 5]))
    print(nchoc2(5, [2, 4, 6, 8, 10]))

main()