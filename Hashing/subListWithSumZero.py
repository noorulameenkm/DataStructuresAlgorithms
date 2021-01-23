def find_sub_zero(my_list):
    # Write your code here
    ht = dict()
    total_sum = 0
    for elem in my_list:
        total_sum += elem
        if elem is 0 or total_sum is 0 or ht.get(total_sum) is not None:
            return True

        ht[total_sum] = elem

    return False



print(find_sub_zero([6, 4, -7, 3, 12, 9]))
print(find_sub_zero([6, 4, 1, 2, 9, -10]))