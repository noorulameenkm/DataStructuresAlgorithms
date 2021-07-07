from math import inf

class Result:
    def __init__(self, sum, left, right, top, bottom):
        self.max_sum = sum
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f'max_sum = {self.max_sum}, left = {self.left}, right = {self.right}, top = {self.top}, bottom = {self.bottom}'


def kadanes(arr):
    current_start = 0
    max_sum = -inf
    sum_ = 0
    max_start, max_end = -1, -1
    for i in range(len(arr)):
        sum_ += arr[i]

        if sum_ < 0:
            sum_ = 0
            current_start = i + 1
        
        if sum_ > max_sum:
            max_sum = sum_
            max_start = current_start
            max_end = i

    return max_start, max_end, max_sum

"""
    Time Complexity - O(N^2 M)
    Space Complexity - O(M)
"""
def find_max_sum_rectangle(matrix):
    max_left, max_right = 0, 0
    max_sum = -inf
    max_top, max_bottom = 0, 0
    M, N = len(matrix), len(matrix[0])
    sums = [0] * M
    for L in range(N):
        sums = [0] * M
        for R in range(L, N):
            for i in range(M):
                sums[i] += matrix[i][R]

            top, bottom, sum_ = kadanes(sums)
            if sum_ > max_sum:
                max_sum = sum_
                max_top = top
                max_bottom = bottom
                max_left = L
                max_right = R

    return Result(max_sum, max_left, max_right, max_top, max_bottom)

    
    
print(find_max_sum_rectangle(matrix = [[ 2,  1, -3, -4,  5],[ 0,  6,  3,  4,  1],[ 2, -2, -1,  4, -5],[-3,  3,  1,  0,  3]]))
