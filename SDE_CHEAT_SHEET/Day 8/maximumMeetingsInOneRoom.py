def maximumMeetings(n,start,end):
    # code here
    if n == 0 or n == 1:
        return n
        
    meetings = []
    for i in range(n):
        meetings.append(Meeting(start[i], end[i]))
    
    meetings.sort(key=lambda x: x.end)
    
    count = 1
    start, end = meetings[0].start, meetings[0].end
    for i in range(1, n):
        if meetings[i].start > end:
            count += 1
            start, end = meetings[i].start, meetings[i].end
    
    return count
        
        
            
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.start < other.start


def main():
    N = 6
    S = [1,3,0,5,8,5]
    F = [2,4,6,7,9,9]
    print(maximumMeetings(N, S, F))
    N = 8
    S = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    F = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
    print(maximumMeetings(N, S, F))

main()