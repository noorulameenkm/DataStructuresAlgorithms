from math import sqrt

def findAllFactors1(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def findAllFactors2(num):
    factors = [1]
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            factors.append(i)

    if num > 1:
        factors.append(num)
    return factors


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = []
        for i in range(1, int(sqrt(A)) + 1):
            if A % i == 0:
                factors.append(i)
                
                if i != (A // i):
                    factors.append(A // i)
        
        factors.sort()
        return factors



def main():
    # Method 1
    print(findAllFactors1(6))

    # Method 2
    print(findAllFactors2(6))

    # Method 3
    print(Solution().allFactors(6))


main()