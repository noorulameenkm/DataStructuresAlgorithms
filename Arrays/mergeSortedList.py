def merge_lists(lst1, lst2):
    # Write your code here
    sortedList = []

    while len(lst1) != 0 and len(lst2) != 0:
        minElement = min(lst1[0], lst2[0])
        sortedList.append(minElement)
        if minElement == lst1[0]:
            lst1 = lst1[1:]
        else:
            lst2 = lst2[1:]

    if len(lst1) != 0:
        # sortedList[len(sortedList):] = lst1
        sortedList.extend(lst1)
    if len(lst2) != 0:
        # sortedList[len(sortedList):] = lst2
        sortedList.extend(lst2)
    
    return sortedList


print(f'Solution is {merge_lists([1,5,6,8],[2,3,88])}')