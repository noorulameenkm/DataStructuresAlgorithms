def calculate_bitwise_complement(n):
  # TODO: Write your code here
  bit_count, num = 0, n 
  while num > 0:
    bit_count += 1
    num = num >> 1 

  all_bits_set = pow(2, bit_count) - 1

  return n ^ all_bits_set

def main():
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
  print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()