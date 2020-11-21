class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        results = []
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            
            if end < current[0]:
                results.append([start, end])
                start, end = current[0], current[1]
            else:
                start = min(start, current[0])
                end = max(end, current[1])
            
        results.append([start, end])
        
        return results
            


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))