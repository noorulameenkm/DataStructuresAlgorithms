def find_first_unique(lst):
    # Write your code here
    frequency = {}
    for i in range(len(lst)):
        num = lst[i]
        if num not in frequency:
            frequency[num] = [num, 0, 0]
        frequency[num] = [num, frequency[num][1] + 1, i]

    uniques = [[x[1][0], x[1][2]] for x in frequency.items() if x[1][1] == 1]
    if len(uniques) == 0:
        return None
    
    uniques = sorted(uniques, key=lambda x: x[1])

    return uniques[0][0]



print(find_first_unique([9, 2, 3, 2, 6, 6]))
print(find_first_unique([4, 5, 1, 2, 0, 4]))