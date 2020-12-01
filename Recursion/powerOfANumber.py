def power(base, exponent):
  # Base Case
  if exponent == 0 :
    return 1
    
  # Recursive Case
  else :
    return base * power(base, exponent - 1);


def main():
    print(power(2, 3))
    print(power(3, 3))


main()