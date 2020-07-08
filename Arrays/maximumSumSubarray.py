class Solution:
    def maximum_sum(self, arr, k):
        max_sum, sum_, start = 0, 0, 0
        for end in range(len(arr)):
            sum_ = sum_ + arr[end]

            if end >= k - 1:
                if sum_ > max_sum:
                    max_sum = sum_
                sum_ = sum_ - arr[start]
                start += 1
            

        return max_sum if max_sum > 0 else -1



print(f'Solution for maximum sum subarray for [2, 1, 5, 1, 3, 2] and 3 is {Solution().maximum_sum([2, 1, 5, 1, 3, 2], 3)}')
print(f'Solution for maximum sum subarray for [2, 1] and 3 is {Solution().maximum_sum([2, 1], 3)}')