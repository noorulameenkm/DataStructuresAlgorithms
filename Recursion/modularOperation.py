def mod(dividend, divisor) :
  # Check division by 0
  if divisor == 0 :
    print("Divisor cannot be ")
    return 0

  # Base Case
  if dividend < divisor :
    return dividend

  # Recursive Case
  else :
    return mod(dividend - divisor, divisor)

def main():
    print(mod(10, 4))
    print(mod(12, 4))

main()