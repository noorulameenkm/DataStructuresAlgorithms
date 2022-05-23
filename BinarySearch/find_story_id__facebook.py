
"""
    Time Comlexity - O(logn)
    Space Complexity - O(1)
"""


def find_story_id(stories, key):
    start, end = 0, len(stories) - 1

    if start > end:
        return -1

    while start <= end:
        mid = start + (end - start) // 2

        if stories[mid] == key:
            return mid

        if stories[start] <= stories[mid] and \
           stories[start] <= key and \
           key <= stories[mid]:
            end = mid - 1
        elif stories[mid] <= stories[end] and \
            stories[mid] <= key and key <= stories[end]:
             start = mid + 1
        # The below condition doesn't make sense
        elif stories[start] <= stories[mid] and \
             stories[mid] <= stories[end] and \
             key > stories[end]:
             start = mid + 1
        elif stories[end] <= stories[mid]:
            start = mid + 1
        elif stories[start] >= stories[mid]:
            end = mid - 1
        else:
            return -1

    return -1


v1 = [6, 7, 1, 2, 3, 4, 5]
print("Story(3) found at index: " + str(find_story_id(v1, 3)))
print("Story(6) found at index: " + str(find_story_id(v1, 6)))

v2 = [5,6,7,8,9,10,11,12,1,2,3,4]

print("Story(3) found at index: " + str(find_story_id(v2, 3)))
print("Story(6) found at index: " + str(find_story_id(v2, 6)))
