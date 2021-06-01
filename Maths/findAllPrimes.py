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



class Solution2:
    def sieve(number):
        if number <= 1:
            return []


        primes = [True for _ in range(number + 1)]
        primes[0] = primes[1] = False

        i = 2
        while i * i <= number:
            if primes[i] == True:
                for j in range(i * i, number + 1, i):
                    primes[j] = False
            i += 1

        res = []
        for k in range(2, number + 1):
            if primes[k] == True:
                res.append(k)

        return res
        




def main():
    print(Solution().sieve(7))
    print(Solution2.sieve(7))
    print(Solution2.sieve(3))
    print(Solution2.sieve(2))
    print(Solution2.sieve(1))

main() 