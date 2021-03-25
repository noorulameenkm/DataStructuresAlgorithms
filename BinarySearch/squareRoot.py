"""
    Time Complexity - O(logN)
    Space complexity - O(1)
"""
def square_root(n):
  start, end = 1, n
  res = -1
  while start <= end:
    mid = start + ((end - start) // 2)

    midSquare = mid * mid

    if midSquare > n:
      end = mid - 1
    elif midSquare <= n:
       res = mid
       start = mid + 1
  
  return res


if __name__ == '__main__':
    print("Square root:", square_root(4))
    print("Square root:", square_root(8))
    print("Square root:", square_root(10))