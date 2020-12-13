def mergeIntervals(intervals):
    length = len(intervals)
    if length == 0:
        return []

    intervals.sort(key=lambda x: x[0])
    result = []

    i = 0
    start, end = intervals[0]
    while i < length - 1:
        j = i + 1
        while j < length:
            if intervals[j][0] <= end:
                start = min(start, intervals[j][0])
                end = max(end, intervals[j][1])
                j += 1
            else:
                result.append([start, end])
                i = j
                if i < length:
                    start, end = intervals[i]
                break

        if j == length:
            break
        
    
    result.append([start, end])
    return result


def mergeIntervals2(intervals):
    length = len(intervals)
    if length == 0:
        return []

    result = []
    
    start, end = intervals[0]
    for i in range(1, length):
        interval = intervals[i]
        if interval[0] <= end:
            start, end = min(start, interval[0]), max(end, interval[1])
        else:
            result.append([start, end])
            start, end = interval
    
    result.append([start, end])
    return result

def main():
    # First Approach
    print(mergeIntervals([[1,3], [2,6], [8,10], [15,18]]))
    print(mergeIntervals([[1,4],[4,5]]))

    # Second Approach
    print(mergeIntervals2([[1,3], [2,6], [8,10], [15,18]]))
    print(mergeIntervals2([[1,4],[4,5]]))


main()


# [[1,3],[2,6],[8,10],[15,18]]