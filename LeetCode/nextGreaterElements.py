"""
    Problem Link:- https://leetcode.com/problems/next-greater-element-i/
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        index_mapper = {}
        results = [0 for _ in range(len(nums1))]
        n = len(nums2)
        for i in range(len(nums1)):
            index_mapper[nums1[i]] = i
        
        for i in range(n - 1, -1, -1):
            num = nums2[i]
            
            while len(stack) > 0 and num >= nums2[stack[0]]:
                stack.pop(0)
            
            result = -1
            if len(stack) > 0:
                result = nums2[stack[0]]
                
            if num in index_mapper:
                index = index_mapper[num]
                results[index] = result
            
            stack.insert(0, i)
            
        return results


print(Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(Solution().nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))       