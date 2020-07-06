class Solution:
    def plusOne(self, digits):
        length_minus_one = len(digits) - 1
        if len(digits) == 0:
            return []
        
        rem = 1
        for i in range(length_minus_one, -1, -1):
            num = digits[i] + rem
            if num <= 9:
                digits[i] = num
                break
            else:
                digits[i] = num % 10
                rem = num // 10
                if i == 0:
                    digits.insert(0, rem)
                    
        return digits


print(f'Solution for [1,2,3,9] is {Solution().plusOne([1,2,3,9])}')
        
        