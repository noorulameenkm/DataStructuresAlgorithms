class Interval:
    def __init__(self,start, end):
        self.start = start
        self.end = end


class Solution:
    def checkOverlap(self, intervals):
        if len(intervals) < 2:
            return False

        intervals.sort(key=lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval.start <= end:
                return True
            else:
                start = interval.start
                end = interval.end
        
        return False


input_1 = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
print(Solution().checkOverlap(input_1))
input_2 = [Interval(1, 4), Interval(5, 6), Interval(7, 9)]
print(Solution().checkOverlap(input_2))
        
