def right_rotate(lst, n):
    n = n % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - n, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - n):
        rotatedList.append(lst[item])
    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], abs(3)))



def right_rotate_2(lst, n):
    # get rotation index
    n = n % len(lst)    

    return lst[-n:] + lst[:-n]


print(right_rotate_2([10, 20, 30, 40, 50], abs(3)))