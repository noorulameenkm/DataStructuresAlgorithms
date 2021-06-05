from heapq import *

def maxiumPerformanceOfTeam(n, speed, efficiency, k):
    min_heap = []

    engineers = []
    for eff, sp in zip(efficiency, speed):
        engineers.append([eff, sp])
    
    engineers.sort(key=lambda x: -x[0])

    total_speed = 0
    performance = 0
    for eff, sp in engineers:
        total_speed += sp

        heappush(min_heap, sp)

        if len(min_heap) > k:
            total_speed -= heappop(min_heap)
        
        performance = max(total_speed * eff, performance)
    
    return performance % 10000000007




print(maxiumPerformanceOfTeam(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))
print(maxiumPerformanceOfTeam(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3))
print(maxiumPerformanceOfTeam(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4))