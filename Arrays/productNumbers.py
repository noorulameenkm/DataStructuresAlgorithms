def productExceptSelf(arr):
    productTillBefore = 1
    result = []

    for i in range(len(arr)):
        currentProduct = 1

        for k in arr[i + 1:]:
            currentProduct = currentProduct * k
        
        result.append(currentProduct * productTillBefore)
        productTillBefore = productTillBefore * arr[i]

    return result


class Solution:
    def productExceptSelf(self, nums):
        products = []
        
        left = 1
        for num in nums:
            products.append(left)
            left *= num
            
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] = products[i] * right
            right = right * nums[i]
            
        return products



#[1,2,3,4]
print(f'Product Except Self for [1,2,3,4] is {productExceptSelf([1,2,3,4])}')
print(f'Product Except Self for [1,2,3,4] is {Solution().productExceptSelf([1,2,3,4])}')