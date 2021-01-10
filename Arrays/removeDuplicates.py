def remove_duplicates(arr):
  prev, next_, length = 0, 1, len(arr)

  while prev < length and next_ < length:
    if arr[prev] == arr[next_]:
      arr.pop(prev)
      length -= 1
      prev = next_ - 1
    else:
      prev = next_
      next_ += 1

  return len(arr)


def remove_duplicates2(arr):
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1
  
  return next_non_duplicate


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        
        if n == 0 or n == 1:
            return n
        
        j = 0
        for i in range(0, n - 1):
            if A[i] != A[i + 1]:
                A[j] = A[i]
                j += 1
        
        A[j] = A[n - 1]

        A = A[0: j + 1]

        return len(A)



print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))
print(remove_duplicates2([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates2([2, 2, 2, 11]))
print(Solution().removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
print(Solution().removeDuplicates([2, 2, 2, 11]))
