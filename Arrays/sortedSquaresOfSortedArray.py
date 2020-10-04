def make_squares(arr):
  squares = []
  # TODO: Write your code here
  start, end = 0, len(arr) - 1
  while start < end:
    startSquare = square(arr[start])
    endSquare = square(arr[end])
    if startSquare >= endSquare:
      squares.insert(0, startSquare)
      start += 1
    else:
      squares.insert(0, endSquare)
      end -= 1
    
  if start == end:
    squares.insert(0, square(arr[start]))

  return squares


def make_squares2(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares


def square(n):
  return n * n



print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))
print(make_squares2([-2, -1, 0, 2, 3]))
print(make_squares2([-3, -1, 0, 1, 2]))