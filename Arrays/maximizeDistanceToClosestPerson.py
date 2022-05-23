from math import inf

class Solution:
    def maxDistToClosest(self, seats):
        distance = -1 
        Maximum_Distance = 0
        for i in range(len(seats)):
            if seats[i] == 1: # if seat is 0 that means it is empty we won't perform any action
                if distance == -1: # if we are encounting the first seated person
                    Maximum_Distance = i 

                else:
                    Maximum_Distance = max(Maximum_Distance,((i - distance) // 2)) 
                    # if we have encounted any seated person before then we will compare for the maximum distance till now to the current distance possible
                
                distance = i 

        if seats[-1] == 0: # if end seat is empty
            Maximum_Distance = max(Maximum_Distance, (len(seats) - 1 - distance))

        return Maximum_Distance


class Solution2:
    def maxDistToClosest(self, seats):
        n = len(seats)
        left_, right_ = [-1] * n, [-1] * n
        
        i, lastOne, maxDis = 0, -1, -1
        
        while i < n:
            if seats[i] == 0:
                left_[i] = lastOne
                # maxDis = 1
            else:
                lastOne = i
            
            i += 1
        
        i = n - 1
        lastOne = -1
        
        while i >= 0:
            if seats[i] == 0:
                right_[i] = lastOne
            else:
                lastOne = i
            
            i -= 1
        
        for i in range(n):
            if seats[i] == 0:
                left_dis = inf if left_[i] == -1 else (i - left_[i])
                right_dis = inf if right_[i] == -1 else (right_[i] - i)
                dis = min(left_dis, right_dis)
                if dis > maxDis:
                    maxDis = dis
        
        return maxDis


print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
print(Solution2().maxDistToClosest([1,0,0,0,1,0,1]))