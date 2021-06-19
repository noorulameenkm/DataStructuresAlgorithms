
"""
 Time complexity - O(1)
 Space complexity - O(1)
"""
def count_set_bits(number):
    count = 0

    while number > 0:
        if number & 1 == 1:
            count += 1
        
        number = number >> 1
    
    return count


def count_set_bits_2(number):
    count = 0

    while number > 0:
        count += 1
        number &= (number - 1)
    
    return count



def count_set_bits_3(n):
    table = [0 for _ in range(256)]
    table[0] = 0

    for i in range(1, 256):
        table[i] = (i & 1) + table[i >> 1] # i >> 1 equals to i/2

    res = 0; 
    for i in range(4):
        res += table[n & 0xff]; 
        n >>= 8; 

    return res


print(count_set_bits(number=125))
print(count_set_bits_2(number=125))
print(count_set_bits_3(n=125))