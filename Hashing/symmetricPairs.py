def find_symmetric(my_list):
    # Write your code here
    pair_set = set()
    result = []
    for pair in my_list:
        pair_tup = tuple(pair)
        pair.reverse()
        reverse_tup = tuple(pair)
        if reverse_tup in pair_set:
            result.append(list(pair_tup))
            result.append(list(reverse_tup))
        else:
            pair_set.add(pair_tup)

    return result


print(find_symmetric([[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]))