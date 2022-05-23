from collections import defaultdict

class Solution:
    def minJumps(self, arr):
        
        frequency = defaultdict(list)
        queue = []
        for i, num in enumerate(arr):
            frequency[num].append(i)
            
        visited = [False] * len(arr)
        level = 0
        queue.append(0)
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                index = queue.pop(0)
                
                if index == len(arr) - 1:
                    return level
                
                if index < 0 or index >= len(arr) or visited[index]:
                    size -= 1
                    continue
                
                if index - 1 > 0 and not visited[index - 1]:
                    queue.append(index - 1)
                
                if index + 1 < len(arr) and not visited[index + 1]:
                    queue.append(index + 1)
                
                if arr[index] in frequency:
                    for index_ in frequency[arr[index]]:
                        if index_ >= 0 and index_ < len(arr) and not visited[index_]:
                            queue.append(index_)
                    
                    del frequency[arr[index]]
                
                visited[index] = True
                
                size -= 1
                
            level += 1
        
        return -1
            
                    
print(Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404]))
print(Solution().minJumps([7,6,9,6,9,6,9,7]))
