
"""
    Problem Link:- https://leetcode.com/problems/push-dominoes/
    Time Complexity - O(N)
    Space Complexity - O(N)
"""


def push_dominoes(dominoes):
    lst = list(dominoes)
    n = len(lst)

    left = [-1 for _ in range(n)]
    right = [-1 for _ in range(n)]

    if lst[n - 1] == 'L':
        left[n - 1] = n - 1
    
    for i in range(n - 2, -1, -1):
        if lst[i] == '.' and left[i + 1] != -1:
            left[i] = left[i + 1]
            continue

        
        if lst[i] == 'L':
            left[i] = i
            continue

    if lst[0] == 'R':
        right[0] = 0
    
    for i in range(1, n):
        if lst[i] == '.' and right[i - 1] != -1:
            right[i] = right[i - 1]
            continue
        
        if lst[i] == 'R':
            right[i] = i
        
    
    for i in range(n):
        if left[i] == -1 and right[i] == -1:
            lst[i] = '.'
            continue

        if left[i] == -1:
            lst[i] = 'R'
            continue
        
        if right[i] == -1:
            lst[i] = 'L'
            continue
        
        if abs(left[i] - i) < abs(right[i] - i):
            lst[i] = 'L'
            continue
        
        if abs(left[i] - i) > abs(right[i] - i):
            lst[i] = 'R'
            continue

        lst[i] = '.'
    
    return ''.join(lst)




print(push_dominoes(dominoes = "RR.L"))
print(push_dominoes(dominoes = ".L.R...LR..L.."))