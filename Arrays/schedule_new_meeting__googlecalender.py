
"""
    Time complexity - O(n)
    Space complexity  - O(n)
"""
def insert_meeting(meetings, new_meeting):
    output = []
    i = 0
    n = len(meetings)
    start, end = new_meeting
    while i < n and start > meetings[i][0]:
        output.append(meetings[i])
        i += 1
    
    if not output or start > output[-1][1]:
        output.append(new_meeting)
    else:
        output[-1][1] = max(end, output[-1][1])
    
    while i < n:
        start, end = meetings[i]

        if output[-1][1] < start:
            output.append(meetings[i])
        else:
            output[-1][1] = max(end, output[-1][1])

        i += 1

    return output

        

# Driver code
meeting_times = [[1, 3], [4, 6], [8, 10], [10, 12], [13, 15], [16, 18]]
new_meeting = [9, 13]
print(insert_meeting(meeting_times, new_meeting))