class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        
        def maxConsecutiveDifference(array):
            max_ = array[1] - array[0]
            for i in range(2, len(array)):
                if array[i] - array[i - 1] > max_:
                    max_ = array[i] - array[i - 1]
            
            return max_
        
        maxHorizontal = maxConsecutiveDifference(horizontalCuts)
        maxVertial = maxConsecutiveDifference(verticalCuts)
        
        return (maxHorizontal * maxVertial) % 1000000007
        


print(Solution().maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
print(Solution().maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
print(Solution().maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))