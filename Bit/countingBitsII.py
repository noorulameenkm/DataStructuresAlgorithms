def helper(n):
    count = 0
    while n > 0:
        count += 1
        n &= (n - 1)
    
    return count


""""
 Time complexity - O(n)
"""
def counting_set_bits(n):

    result = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        result[i] = helper(i)

    return result



print(counting_set_bits(6))