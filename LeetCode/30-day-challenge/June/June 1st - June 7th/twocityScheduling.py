class Solution:
    def twoCitySchedCost(self, costs):
        minimumCost = 0
        length = len(costs)
        diff_cost_sorted = sorted(costs, key=lambda co: co[0] - co[1])
        for i in range(length):
            if i < length / 2:
                minimumCost += diff_cost_sorted[i][0]
            else:
                minimumCost += diff_cost_sorted[i][1]
            
        return minimumCost



print(f'Minimum Cost is {Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])}')