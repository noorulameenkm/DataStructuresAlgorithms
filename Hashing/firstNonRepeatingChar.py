import collections

def findFirstUnique(lst):
    # Write your code here
    counts = {}
    counts = counts.fromkeys(lst, 0)
    for ele in lst:
        counts[ele] += 1
    
    for ele in lst:
        if counts[ele] == 1:
            return ele
    
    return None


def findFirstUnique_2(lst):
    orderedCounts = collections.OrderedDict()  # Creating an ordered dictionary
    # Initializing dictionary with pairs like (lst[i],0)
    orderedCounts = orderedCounts.fromkeys(lst, 0)
    for ele in lst:
        orderedCounts[ele] += 1  # Incrementing for every repitition
    for ele in orderedCounts:
        if orderedCounts[ele] == 1:
            return ele
    return None




# Approach 1
print(findFirstUnique([9, 2, 3, 2, 6, 6]))
print(findFirstUnique([4, 5, 1, 2, 0, 4]))
print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))

# Approach 2
print(findFirstUnique_2([9, 2, 3, 2, 6, 6]))
print(findFirstUnique_2([4, 5, 1, 2, 0, 4]))
print(findFirstUnique_2([1, 1, 1, 2, 3, 2, 4]))

