def find_happy_number(num):
  slow, fast = num, num
  while True:  
    slow = squareNumber(slow)
    fast = squareNumber(squareNumber(fast))
    if slow == fast:
      break
    
  return fast == 1



def squareNumber(num):
  k = 0
  while num != 0:
    k += (num % 10) * (num % 10)
    num = num // 10

  return k


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
