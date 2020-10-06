class Solution:
    def bitwiseComplement(self, N):
        bit_count, num = 0, N
        if N == 0:
            return 1
        
        while num > 0:
            bit_count += 1
            num >>= 1
        
        all_bits_set = pow(2, bit_count) - 1
        
        return N ^ all_bits_set
        

print(Solution().bitwiseComplement(5))