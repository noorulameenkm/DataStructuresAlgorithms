"""
    Problem Link:- https://leetcode.com/problems/three-equal-parts/
"""

class Solution:
    def threeEqualParts(self, arr):
        number_of_ones = 0
        for num in arr:
            number_of_ones += num
        
        if number_of_ones == 0:
            return [0, 2]
        
        if number_of_ones % 3 != 0:
            return [-1, -1]
        
        number_of_ones_each_part = number_of_ones // 3
        first_one_part_one = -1
        first_one_part_two = -1
        first_one_part_three = -1
        number_of_ones = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                number_of_ones += 1
                if number_of_ones == number_of_ones_each_part + 1:
                    first_one_part_two = i
                elif number_of_ones == (2 * number_of_ones_each_part) + 1:
                    first_one_part_three = i
                elif number_of_ones == 1:
                    first_one_part_one = i
        
        while first_one_part_three < len(arr):
            if arr[first_one_part_one] == arr[first_one_part_three] and arr[first_one_part_three] == arr[first_one_part_two]:
                first_one_part_one += 1
                first_one_part_three += 1
                first_one_part_two += 1
            else:
                return [-1, -1]
        
        return [first_one_part_one - 1, first_one_part_two]


print(Solution().threeEqualParts(arr = [1,0,1,0,1]))
print(Solution().threeEqualParts(arr = [1,1,0,1,1]))
print(Solution().threeEqualParts(arr = [1,1,0,0,1]))