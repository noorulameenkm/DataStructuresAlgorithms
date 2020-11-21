"""
 Time Complexity - O(N * 2^N)
 Space Complexity - O(N * 2^N)
"""

def subsets(nums):
    subsets_ = [[]]
    for num in nums:
        for i in range(len(subsets_)):
            list_ = list(subsets_[i])
            list_.append(num)
            subsets_.append(list_)
            
    return subsets_
        


print(f'Subsets for [1,2,3] are {subsets([1,2,3])}')