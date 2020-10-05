class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        start, end = intervals[0][0], intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= start and interval[1] <= end:
                start, end = min(start, interval[0]), max(end, interval[1])
            else:
                start, end = interval[0], interval[1] 
                count += 1
            
        return count


print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(Solution().removeCoveredIntervals([[3,10],[4,10],[5,11]]))
print(Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]]))