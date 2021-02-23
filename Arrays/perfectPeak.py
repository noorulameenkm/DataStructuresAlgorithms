import math

def perfectPeak(arr):
    if len(arr) <= 2:
        return 0
    
    i = 1
    while i < len(arr) - 1:
        max_left = -math.inf
        min_right = math.inf
        key = arr[i]
        for k in range(i):
            max_left = max(max_left, arr[k])
        
        for m in range(i + 1, len(arr)):
            min_right = min(min_right, arr[m])
        
        if key > max_left and key < min_right:
            return 1

        i += 1

    return 0



def perfectPeak2(arr):
    if len(arr) <= 2:
        return 0

    maxLeft = [0 for _ in range(len(arr))]
    minRight = [0 for _ in range(len(arr))]
    maxLeft[0], minRight[-1] = arr[0], arr[-1]
    n = len(arr)
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i - 1], arr[i])
    
    for j in range(n - 2, -1, -1):
        minRight[j] = min(minRight[j + 1], arr[j])
    
    for k in range(1, n):
        if arr[k] > maxLeft[k - 1] and arr[k] < minRight[k + 1]:
            return 1
    
    return 0


def perfectPeak3(arr):
    if len(arr) <= 2:
        return 0
    
    n = len(arr)
    maxLeft = [0 for i in range(n)]
    maxLeft[0] = arr[0]
    
    for i in range(1, n):
        maxLeft[i] = max(arr[i], maxLeft[i - 1])
    
    minRight = arr[-1]
    for j in range(n - 1, -1, -1):
        if arr[j] > maxLeft[j - 1] and arr[j] < minRight:
            return 1
        
        minRight = min(minRight, arr[j])
    
    return 0


def perfectPeak4(arr):
    if len(arr) < 3:
        return 0
    
    m_left = arr[0]
    m_right = arr[-1]

    L = [False] * (len(arr) - 1)
    for i in range(1, len(arr) - 1):
        if arr[i] > m_left:
            m_left = arr[i]
            L[i] = True
    
    for j in range(len(arr) - 2, 0, -1):
        if arr[j] < m_right:
            if L[j] == True:
                return 1
            
            m_right = arr[j]
    
    return 0


def perfectPeak5(A):
        min_a = [0]*len(A)
        max_a = [0]*len(A)
        maxa = A[0]
        mina = A[-1]
        n= len(A)
        for i in range(len(A)):
            if A[i]>maxa:
                max_a[i] = A[i]
                maxa= A[i]
            elif A[i]<maxa:
                max_a[i] = maxa
            else:
                max_a[i] = None
                
            if A[n-i-1] < mina:
                min_a[n-i-1] = A[n-i-1]
                mina = A[n-i-1]
            elif A[n-i-1]>mina:
                A[n-i-1] = mina
            else:
                min_a[n-i-1]=None
        for i in range(1,n-1):
            if A[i]==max_a[i] and A[i]==min_a[i]:
                return 1
        return 0

def main():
    # Approach 1
    print(perfectPeak([5, 1, 4, 3, 6, 8, 10, 7, 9]))
    print(perfectPeak([5, 1, 4, 4]))

    # Approach 2
    print(perfectPeak2([5, 1, 4, 3, 6, 8, 10, 7, 9]))
    print(perfectPeak2([5, 1, 4, 4]))

    # Approach 3
    print(perfectPeak3([5, 1, 4, 3, 6, 8, 10, 7, 9]))
    print(perfectPeak3([5, 1, 4, 4]))

    # Approach 4
    print(perfectPeak4([5, 1, 4, 3, 6, 8, 10, 7, 9]))
    print(perfectPeak4([5, 1, 4, 4]))

    # Approach 5
    print(perfectPeak5([5, 1, 4, 3, 6, 8, 10, 7, 9]))
    print(perfectPeak5([5, 1, 4, 4]))

main()