import math

def mergeTwoSortedArray(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return []

    if len(arr1) == 0:
        return arr2
    
    if len(arr2) == 0:
        return arr1

    i, j, merged = 0, 0, []

    while i < len(arr1) and j < len(arr2):
        num1, num2 = arr1[i], arr2[j]
        min_ = min(num1, num2)

        merged.append(min_)
        if min_ == num1:
            i += 1
        else:
            j += 1
        
    if i < len(arr1):
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
    
    if j < len(arr2):
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1

    return merged


def mergeTwoArrays(nums1, nums2):
    i, j = 0, 0

    while i < len(nums1):
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            k = j
            while k < len(nums2) - 1 and nums2[k] > nums2[k + 1]:
                nums2[k], nums2[k + 1] = nums2[k + 1], nums2[k]
                k += 1
        i += 1

    return


def mergeTwoArrays2(nums1, nums2):
    gap = math.ceil(len(nums1) + len(nums2) / 2)

    while gap >= 1:
        i = 0

        while i + gap < len(nums1):
            if nums1[i] > nums1[i + gap]:
                nums1[i], nums1[i + gap] = nums1[i + gap], nums1[i]

            i += 1

        j = gap - len(nums1) if gap > len(nums1) else 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j]  = nums2[j], nums1[i]

            i += 1
            j += 1

        if j < len(nums2):
            j = 0
            while j + gap < len(nums2):
                if nums2[j] > nums2[j + gap]:
                    nums2[j], nums2[j + gap] = nums2[j + gap], nums2[j]

                j += 1


        gap = 0 if gap == 1 else math.ceil(gap / 2)


def main():
    # first Approach
    print(mergeTwoSortedArray([1,2,3], [2,5,6]))

    #seond Approach
    nums1, nums2 = [1,2,3], [2,2,6]
    print(f'Before merging, nums1 is {nums1} and nums2 is {nums2}')
    mergeTwoArrays(nums1, nums2);
    print(f'After merging, nums1 is {nums1} and nums2 is {nums2}')

    # Third Approach
    nums1, nums2 = [1,2,10], [4,5,6,9]
    print(f'Before merging, nums1 is {nums1} and nums2 is {nums2}')
    mergeTwoArrays(nums1, nums2);
    print(f'After merging, nums1 is {nums1} and nums2 is {nums2}')

    # Fourth Approach
    nums1, nums2 = [1,2,10], [4,5,6,9]
    print(f'Before merging, nums1 is {nums1} and nums2 is {nums2}')
    mergeTwoArrays2(nums1, nums2);
    print(f'After merging, nums1 is {nums1} and nums2 is {nums2}')


main()


