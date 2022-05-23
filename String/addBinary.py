class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        a_i, b_i = len(a) - 1, len(b) - 1
        while a_i >= 0 or b_i >= 0:
            sum_ = carry

            if a_i >= 0:
                sum_ += (ord(a[a_i]) - ord('0'))

            if b_i >= 0:
                sum_ += (ord(b[b_i]) - ord('0'))

            if sum_ == 0:
                carry = 0
                result = "0" + result
            elif sum_ == 1:
                carry = 0
                result = "1" + result
            elif sum_ == 2:
                carry = 1
                result = "0" + result
            elif sum_ == 3:
                carry = 1
                result = "1" + result

            a_i -= 1
            b_i -= 1

        if carry == 1:
            result = "1" + result

        return result



print(Solution().addBinary(a="11", b="1"))
print(Solution().addBinary(a="1010", b="1011"))
