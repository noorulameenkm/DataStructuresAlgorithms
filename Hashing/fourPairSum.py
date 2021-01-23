def find_pair(my_list):
    # Write your code here
    my_dict = {}
    result = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            added = my_list[i] + my_list[j]
            if added not in my_dict:
                my_dict[added] = [my_list[i], my_list[j]]
            else:
                previous = my_dict[added]
                result.append(previous)
                result.append([my_list[i], my_list[j]])

                return result
    return result


print(find_pair([3, 4, 7, 1, 12, 9]))
print(find_pair([3, 4, 7, 1, 2, 9, 8]))