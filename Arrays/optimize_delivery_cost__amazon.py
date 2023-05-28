
"""
    Time Complexity - O(1)
    Space Complexity - O(min(n, k))
"""
def check_delivery(packages, k):
    curr_sum = 0
    remainders = {}

    remainders[0] = -1

    for i in range(len(packages)):
        curr_sum += packages[i]

        if k != 0:
            curr_sum = curr_sum % k
        
        if curr_sum in remainders:
            if i - remainders[curr_sum] > 1:
                return True
        else:
            remainders[curr_sum] = i


# Driver code
packages = [11, 42, 54, 44, 49, 26]
k = 10
print(check_delivery(packages, k))