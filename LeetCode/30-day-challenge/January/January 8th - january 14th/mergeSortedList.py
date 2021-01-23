class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0 and len(nums2) == 0:
            pass
        elif len(nums1) == 0:
            nums1 = nums2[0:]
        elif len(nums2) == 0:
            nums2 = nums1[0:]
        else:
            i, j = 0, 0
            while i < m:
                if nums1[i] > nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]
                    k = j + 1
                    while k < len(nums2) and nums2[k] < nums2[k - 1]:
                        nums2[k], nums2[k - 1] = nums2[k - 1], nums2[k]    
                        k += 1
                i += 1
            
            nums1[i:] = nums2[0:]
                        
        

def main():
    nums1 = [-10,-10,-9,-9,-9,-8,-8,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-2,-2,-1,-1,0,1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nums2 = [-10,-10,-9,-9,-9,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9]
    m, n = 55, 99
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
main()