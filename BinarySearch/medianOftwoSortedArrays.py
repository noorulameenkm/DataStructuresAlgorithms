from math import inf
from typing import List

"""
Time Complexity - O(n1 + n2)
Space Complexity - O(n1 + n2)
"""
def median_of_two_sorted_arrays(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    arr3 = [0 for i in range(l1 + l2)]
    merge(arr1, arr2, arr3)

    if (l1 + l2) % 2 == 0:
        mid = (l1 + l2) // 2
        return (arr3[mid] + arr3[mid - 1]) / 2
    else:
        return float(arr3[(l1 + l2) // 2])


def merge(arr1, arr2, arr3):
    l1, l2 = len(arr1),len(arr2)

    i, j, k = 0, 0, 0

    while i < l1 and j < l2:
        if arr1[i] <= arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        
        k += 1
    

    while i < l1:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    
    while j < l2:
        arr3[k] = arr2[j]
        j += 1
        k += 1
    
    return


"""
Time Complexity - O(log min(n1, n2))
Space Complexity - O(1)
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
            
        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1
        
        while low <= high:
            
            cut1 = low + (high - low) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            l1 = -inf if cut1 == 0 else nums1[cut1 - 1]
            l2 = -inf if cut2 == 0 else nums2[cut2 - 1]
            
            r1 = inf if cut1 == n1 else nums1[cut1]
            r2 = inf if cut2 == n2 else nums2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2) / 1.0
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return 0.0

# First Approach
print(median_of_two_sorted_arrays(arr1 = [1,3], arr2 = [2]))
print(median_of_two_sorted_arrays(arr1 = [1,2], arr2 = [3,4]))
print(median_of_two_sorted_arrays(arr1 = [0,0], arr2 = [0, 0]))
print(median_of_two_sorted_arrays(arr1 = [], arr2 = [1]))
print(median_of_two_sorted_arrays(arr1 = [2], arr2 = []))


# Second Approach
print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(Solution().findMedianSortedArrays(nums1 = [0,0], nums2 = [0, 0]))
print(Solution().findMedianSortedArrays(nums1 = [], nums2 = [1]))
print(Solution().findMedianSortedArrays(nums1 = [2], nums2 = []))

