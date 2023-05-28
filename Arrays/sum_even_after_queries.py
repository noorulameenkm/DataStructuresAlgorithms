


class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        
        sum_even_values = 0
        results = []
        for num in nums:
            if num % 2 == 0:
                sum_even_values += num
        
        
        for val, index in queries:
            
            if (nums[index] + val) % 2 == 0:
                if nums[index] % 2 == 0:
                    sum_even_values += val
                else:
                    sum_even_values += (nums[index] + val)
            else:
                if nums[index] % 2 == 0:
                    sum_even_values -= nums[index]
            
            nums[index] += val
            
            results.append(sum_even_values)
        
        return results
            



nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(Solution().sumEvenAfterQueries(nums, queries))