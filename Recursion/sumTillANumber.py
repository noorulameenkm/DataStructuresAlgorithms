def sumTill(targetNumber) :
  # Base Case
  if targetNumber == 1 :
    return targetNumber

  # Recursive Case
  else :
    return targetNumber + sumTill(targetNumber - 1)


def main():
    print(sumTill(5))
    print(sumTill(9))
    print(sumTill(10))



main()