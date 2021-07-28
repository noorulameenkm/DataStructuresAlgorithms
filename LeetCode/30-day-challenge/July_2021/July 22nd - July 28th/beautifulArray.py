"""
    Problem Link: https://leetcode.com/problems/beautiful-array/
"""

def beautiful_array(n):
    ans = list()
    ans.append(1)

    while len(ans) < n:
        temp = list()

        for num in ans:
            if (2 * num) - 1 <= n:
                temp.append((2 * num) - 1)
        
        for num in ans:
            if 2 * num <= n:
                temp.append(2 * num)
        
        ans = list(temp)
    
    return ans


print(beautiful_array(n = 4))
print(beautiful_array(n = 5))
