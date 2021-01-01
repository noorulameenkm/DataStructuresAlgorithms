from math import sqrt

def verifyPrime(num):
    if num == 1:
        return False
    
    factors = getAllFactors(num)
    if len(factors) == 2:
        return True
    
    return False


def getAllFactors(A):
    factors = []
    for i in range(1, int(sqrt(A)) + 1):
        if A % i == 0:
            factors.append(i)
            
            if i != (A // i):
                factors.append(A // i)
        
    return factors


class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A == 1:
            return False
            
        for i in range(2, int(sqrt(A)) + 1):
            if A % i == 0:
                return False
        
        return True


def main():
    # Method 1
    print(verifyPrime(6))
    print(verifyPrime(2))
    print(verifyPrime(7))

    # Method 2
    print(Solution().isPrime(6))
    print(Solution().isPrime(2))
    print(Solution().isPrime(7))

main()