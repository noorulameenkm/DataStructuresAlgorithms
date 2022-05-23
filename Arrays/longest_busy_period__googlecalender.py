
"""
    Time Complexity - O(n)
    Space Complexity - O(n)
"""
def longest_busy_period(schedule):
    schedule_set = set(schedule)

    longest_period = 0

    for slot in schedule_set:
        if slot - 1 not in schedule_set:
            period = 0
            j = slot
            while j in schedule_set:
                period += 1
                j += 1
            
            longest_period = max(longest_period, period)


    return longest_period



print(longest_busy_period([3, 1, 15, 5, 2, 12, 10, 4, 8, 9]))