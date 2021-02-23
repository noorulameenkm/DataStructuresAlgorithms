from math import factorial


"""
Time Complexity - O(N^2)
Space Complexity - O(N^2)
"""
class Solution:
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                current = [1]
                previous = list(result[i - 1])
                for j in range(len(previous) - 1):
                    current.append(previous[j] + previous[j + 1])
                
                current.append(1)
                
                result.append(current)
                
        return result

def kthValueInNthRow(n, k):
    # equation n - 1 C k - 1
    n, k = n - 1, k - 1
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
        

def pascalsTriangle(n):
    p = []
    i = 0
    while i < n:
        row = []
        for j in range(i + 1):
            if j == 0 or j == i: 
                row.append(1)
            else:
                row.append(p[i - 1][j - 1] + p[i - 1][j])

        p.append(row) 
        i += 1

    return p


def pascalsTriangle2(n):
    p = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                p[i].append(1)
            else:
                p[i].append(p[i - 1][j - 1] + p[i - 1][j])
    
    return p


def main():
    print(Solution().generate(5))
    print(kthValueInNthRow(5, 3))
    print(pascalsTriangle(5))
    print(pascalsTriangle2(5))

main()