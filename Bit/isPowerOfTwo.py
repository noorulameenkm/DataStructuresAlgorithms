

def isPowerOfTwo(n):

    if n == 0:
        return False

    while n != 1:

        if n % 2 != 0:
            return False
        
        n >>= 1
    
    return True


def isPowerOfTwo2(n):
    if n == 0:
        return False
    
    return (n & n - 1) == 0


# Method 1
print(isPowerOfTwo(5))
print(isPowerOfTwo(32))
print(isPowerOfTwo(16))
print(isPowerOfTwo(15))

# Method 2
print(isPowerOfTwo2(5))
print(isPowerOfTwo2(32))
print(isPowerOfTwo2(16))
print(isPowerOfTwo2(15))