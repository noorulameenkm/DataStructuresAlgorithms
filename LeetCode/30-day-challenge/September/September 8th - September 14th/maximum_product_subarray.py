import math

def maximum_product_subarray(array):
    start = 0
    maxProduct, window_product =  -math.inf , 1

    for end in range(len(array)):
        window_product *= array[end]

        if window_product > maxProduct:
            maxProduct = window_product
        else:
            while window_product < maxProduct and start <= end:
                window_product //= array[start]
                start += 1

                if window_product > maxProduct:
                    maxProduct = window_product 

    return maxProduct



print(maximum_product_subarray([-2,0,-1]))
print(maximum_product_subarray([2,3,-2,4]))
print(maximum_product_subarray([2,3,-2,10]))



