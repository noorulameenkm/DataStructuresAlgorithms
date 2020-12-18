def pow2(x, n):

    result = 1.0
    nn = n
    if nn < 0:
        nn = -1 * nn

    while nn > 0:
        if nn % 2 == 0:
            nn = nn / 2
            x = x * x
        else:
            result *= x
            nn = nn - 1
    
    if n < 0:
        result = 1.00000 / result

    return result


def pow_(x, n):
    result = 1.0

    for i in range(n):
        result *= x
    
    return result



def main():

    # First Approach
    print(pow_(2.00000, 10))

    # Second Approach
    print(pow2(2.00000, 10))

main()
