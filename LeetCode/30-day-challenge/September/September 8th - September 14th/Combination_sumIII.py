def combinationSum(k, n):
    results = []
    subsets = [[]]
    for num in range(1, 10):
        for i in range(len(subsets)):
            n_set = list(subsets[i])
            n_set.append(num)
            subsets.append(n_set)
            if len(n_set) == k  and sum(n_set) == n:
                results.append(list(n_set))
    return results


class Solution:
    def backtrack(self, k, n):
        results = []

        def tracker(remaining_sum, combination, next_start):
            if remaining_sum == 0 and len(combination) == k:
                results.append(list(combination))
                return
            
            if remaining_sum < 0 and len(combination) == k:
                return
            
            for i in range(next_start, 10):
                combination.append(i)
                tracker(remaining_sum - i, combination, i + 1)
                combination.pop()

        
        tracker(n, [], 1)

        return results




print(combinationSum(3, 7))
print(Solution().backtrack(3, 7))