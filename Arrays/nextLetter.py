
"""
Time Complexity - O(logN)
Space Complexity - O(1)
"""

def search_next_letter(letters, key):
  n = len(letters)
  if key > letters[n - 1] or key < letters[0]:
    return letters[0]
  
  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2

    if key >= letters[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
  return letters[start % n]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
