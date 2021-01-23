# Decimal library to assign infinite numbers
from decimal import Decimal


def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    # Write your code here!
    max1 = lst[0]
    max2 = Decimal('-Infinity')

    min1 = lst[0]
    min2 = Decimal('Infinity')

    for num in lst:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    if max1 * max2 > min1 * min2:
        return max2, max1
    else:
        return min2, min1
    


def main():
    print(find_max_prod([1, 3, 5, 2, 6]))
    print(find_max_prod([1, 2, 3, 4, 5, 6, 7, 8]))
    print(find_max_prod([0, 1, 0, 1, 0, 1]))

main()