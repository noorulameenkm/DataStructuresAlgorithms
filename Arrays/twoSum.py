def find_sum(lst, k):
    # Write your code here
    sList = sorted(lst)
    i, j = 0, len(sList) - 1
    while i < j:
        if sList[i] + sList[j] == k:
            return [sList[i], sList[j]]
        elif sList[i] + sList[j] < k:
            i += 1
        else:
            j -= 1

    return []


    
print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))