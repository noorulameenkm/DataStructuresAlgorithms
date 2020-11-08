from heapq import *

"""
Time Complexity - O(min(N, K), K * logN)
Space Complexity - O(N)
"""

def find_Kth_smallest(matrix, k):
  number = -1
  minheap = []
  for i in range(min(k, len(matrix))):
    heappush(minheap, (matrix[i][0], 0, matrix[i]))

  count = 1
  while minheap:
    number, index, matrix_ = heappop(minheap)

    if count == k:
      break
    
    if index + 1 < len(matrix_):
      heappush(minheap, (matrix_[index + 1], index + 1, matrix_))
    
    count += 1

  return number


"""
Time Complexity - O(N * log(max - min))
Space Complexity - O(1)

The Binary Search could take O(log(max-min )) iterations where ‘max’ is the largest and ‘min’ 
is the smallest element in the matrix and in each iteration we take O(N) for counting, therefore, 
the overall time complexity of the algorithm will be O(N*log(max-min)).
"""

def find_kth_smallest_alternate(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = matrix[0][0], matrix[n - 1][n - 1]
        count, smaller, larger = find_smaller_larger_and_count(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        elif count < k:
            start = larger
        else:
            end = smaller
    
    return start


def find_smaller_larger_and_count(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0

    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += (row + 1)
            col += 1
    
    return count, smaller, larger


def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
        str(find_Kth_smallest([[-5]], 1)))

    print("Kth smallest number is: " +
        str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))

    print("Kth smallest number(Alternate) is: " +
        str(find_kth_smallest_alternate([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))
    
    print("Kth smallest number is: " +
        str(find_kth_smallest_alternate([[-5]], 1)))

    print("Kth smallest number is: " +
        str(find_kth_smallest_alternate([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main()
