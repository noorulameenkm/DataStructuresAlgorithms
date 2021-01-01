class Solution:
    def sieve(self, A):
        primes = [1 for i in range(A + 1)]
        primes[0] = primes[1] = 0
        
        for i in range(2, A + 1):
            if primes[i] == 1:
                j = 2
                while (i * j) <= A:
                    primes[i * j] = 0
                    j += 1
            
        result = [i for i in range(A + 1) if primes[i] == 1]
        return result


def main():
    print(Solution().sieve(7))

main() 