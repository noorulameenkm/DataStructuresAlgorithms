class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        
        merged = []
        
        intervals.sort(key=lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
                
        merged.append([start, end])
        return merged


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
        