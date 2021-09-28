from typing import List


"""
Problem Link:- https://leetcode.com/problems/sort-array-by-parity-ii/
"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd_number_at_even_index = 0
        even_number_at_odd_index = 1
        while odd_number_at_even_index < n and even_number_at_odd_index < n:
            while odd_number_at_even_index < n and nums[odd_number_at_even_index] % 2 == 0:
                odd_number_at_even_index += 2

            while even_number_at_odd_index < n and nums[even_number_at_odd_index] % 2 != 0:
                even_number_at_odd_index += 2

            if even_number_at_odd_index < n and odd_number_at_even_index < n:
                nums[even_number_at_odd_index], nums[odd_number_at_even_index] = \
                    nums[odd_number_at_even_index], nums[even_number_at_odd_index]

        return nums


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
print(Solution().sortArrayByParityII([2, 3]))
