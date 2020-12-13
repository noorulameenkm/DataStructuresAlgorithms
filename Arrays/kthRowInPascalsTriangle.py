class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        
        previous = self.getRow(A - 1)
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        
        current.append(1)

        return current


def getRow(n):
    li = []
    li1 = []

    for i in range(0, n + 1):
        for j in range(0, i + 1):
            if j == 0 or j == i:
                li1.append(1)
            else:
                li1.append(li[i - 1][j - 1] + li[i - 1][j])

        li.append(li1)
        li1 = []
    return li[n]




def main():
    print(Solution().getRow(5))
    print(Solution().getRow(3))
    print(getRow(3))

main()