

def find_length_recursive(nums1, nums2, index1, index2, n1, n2):
    if index1 == n1 or index2 == n2:
        return 0
    
    s1, s2, s3 = 0, 0, 0


    s1 = find_length_recursive(nums1, nums2, index1 + 1, index2, n1, n2)
    s2 = find_length_recursive(nums1, nums2, index1, index2 + 1, n1, n2)

    if nums1[index1] == nums2[index2]:
        i, j = index1, index2
        while i < n1 and j < n2 and nums1[i] == nums2[j]:
            s3 += 1
            i += 1
            j += 1
    
    return max(s1, s2, s3)


def find_length(nums1, nums2):
    return find_length_recursive(nums1, nums2, 0, 0, len(nums1), len(nums2))


def find_length_recursive_memoization(nums1, nums2, index1, index2, n1, n2, memory):
    if index1 == n1 or index2 == n2:
        return 0
    
    s1, s2, s3 = 0, 0, 0

    key = f'{index1}-{index2}'

    if key in memory:
        return memory[key]

    s1 = find_length_recursive_memoization(nums1, nums2, index1 + 1, index2, n1, n2, memory)
    s2 = find_length_recursive_memoization(nums1, nums2, index1, index2 + 1, n1, n2, memory)

    if nums1[index1] == nums2[index2]:
        i, j = index1, index2
        while i < n1 and j < n2 and nums1[i] == nums2[j]:
            s3 += 1
            i += 1
            j += 1
    
    memory[key] = max(s1, s2, s3)

    return memory[key]


def find_length_2(nums1, nums2):
    memory = {}
    return find_length_recursive_memoization(nums1, nums2, 0, 0, len(nums1), len(nums2), memory)



print(find_length(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(find_length(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))


print(find_length_2(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(find_length_2(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))