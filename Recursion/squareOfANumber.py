def findSquare(targetNumber):
  if targetNumber == 0:
    return 0
  
  return findSquare(targetNumber - 1) + (2 * targetNumber) - 1



def main():
    print(findSquare(12))
    print(findSquare(13))

    # Formula
    # Use the following mathematical identity to solve this problem: (n-1)^2 = n^2 - 2n + 1

main()