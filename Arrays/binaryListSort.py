def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    
    j = 0
    
    for i in range(len(lst)):
        if lst[i] < 1:  # Swapping with jth element if the number is less than 1
            lst[i], lst[j] = lst[j], lst[i]  # Swapping
            j = j + 1
    
    return lst



def main():
    print(sort_binary_list([1, 0, 1, 0, 1, 0, 1, 0]))


main()