class Solution:
    def insert(self, intervals, newInterval):
        merged = []
        
        i, start, end = 0, 0, 1
        
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start], newInterval[end] = min(intervals[i][start], newInterval[start]), max(intervals[i][end], newInterval[end])
            i += 1
            
        
        merged.append(newInterval)
        
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
            
        
        return merged



print(Solution().insert([[1, 3], [5, 7], [8, 12]], [4, 6]))