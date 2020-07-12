def findAllPermutations(nums):
    result = []
    getpermutations(nums, 0, [], result)
    return result


def getpermutations(nums, index, permutation, result):
    if index == len(nums):
        result.append(permutation)
    else:
        num = nums[index]
        for j in range(len(permutation) + 1):
            newPermutation = list(permutation)
            newPermutation.insert(j, num)
            getpermutations(nums, index + 1, newPermutation, result)


def main():
  print("Here are all the permutations: " + str(findAllPermutations([1, 3, 5])))


main()



