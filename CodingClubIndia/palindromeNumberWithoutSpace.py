class Solution:
    def isPalidrome(self, number):

        if number == 0:
            return True

        # find the divisor
        divisor = 1
        while (number // divisor) > 10:
            divisor *= 10
        
        while number > 0:
            # first integers
            firstNumber = number // divisor
            # last integers
            lastNumber = number % 10

            # Integers are not equal then returns false
            if firstNumber != lastNumber:
                return False

            
            # removing first and last integers
            number = (number % divisor) // 10
            # dividing divisor by 100, because we are removing two number each time
            divisor = divisor // 100

        return True
            


print(f'isPalindrom 100 {Solution().isPalidrome(100)}')
print(f'isPalindrom 121 {Solution().isPalidrome(121)}')
print(f'isPalindrom 1221 {Solution().isPalidrome(1221)}')
print(f'isPalindrom 12321 {Solution().isPalidrome(12321)}')
print(f'isPalindrom 123421 {Solution().isPalidrome(123421)}')

