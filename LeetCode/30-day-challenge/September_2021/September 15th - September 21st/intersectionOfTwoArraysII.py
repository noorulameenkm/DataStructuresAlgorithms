from typing import List


"""
    Problem Link:- https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequency = {}
        result = []
        for num in nums1:
            if num not in frequency:
                frequency[num] = 0

            frequency[num] += 1

        for num in nums2:
            if num not in frequency:
                continue

            result.append(num)
            frequency[num] -= 1
            if frequency[num] == 0:
                del frequency[num]

        return result


print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
