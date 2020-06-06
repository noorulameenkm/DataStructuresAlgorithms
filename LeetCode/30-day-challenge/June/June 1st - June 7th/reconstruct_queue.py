class Solution:
    def reconstructQueue(self, people):
        sorted_queue = sorted(people, key=lambda x: (-x[0], x[1]))
        new_arr = []
        for k in sorted_queue:
            new_arr.insert(k[1], k)
        return new_arr


print(f'Solution is {Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])}')