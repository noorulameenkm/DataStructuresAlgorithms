def counts_after(index, heights, height, direction):
    result = 0
    if direction == 'L':
        start = index - 1
        while start >= 0 and heights[start] >= height:
            result += 1
            start -= 1
    elif direction == 'R':
        start = index + 1
        while start < len(heights) and heights[start] >= height:
            result += 1
            start += 1
    
    return result

def largest_histogram(heights):
    max_ = 0

    for i, height in enumerate(heights):
        left = counts_after(i, heights, height, 'L')
        right = counts_after(i, heights, height, 'R')
        count = left + right + 1
        max_ = max(max_, count * height)
    
    return max_


def largest_histogram_2(heights):
    n = len(heights)
    left = [0] * n
    right = [0] * n
    stack = []

    for i in range(n):

        while len(stack) > 0 and heights[stack[0]] >= heights[i]:
            stack.pop(0)
        
        if len(stack) == 0:
            left[i] = 0
        else:
            left[i] = stack[0] + 1

        stack.insert(0, i)

    stack = []
    for j in range(n - 1, -1, -1):

        while len(stack) > 0 and heights[stack[0]] >= heights[j]:
            stack.pop(0)
        
        if len(stack) == 0:
            right[j] = n - 1
        else:
            right[j] = stack[0] - 1
        
        stack.insert(0, j)

    max_ = 0
    for i in range(n):
        res = (right[i] - left[i] + 1) * heights[i]
        max_ = max(max_, res)
    
    return max_


def largest_histogram_3(heights):
    stack = []
    max_ = 0
    n = len(heights)
    for i in range(n + 1):
        while len(stack) > 0 and (i == n or heights[stack[0]] >= heights[i]):
            height = heights[stack[0]]
            stack.pop(0)
            width = i if len(stack) == 0 else i - stack[0] - 1
            max_ = max(max_, height * width)
        
        stack.insert(0, i)
    
    return max_
            

# First Approach
print(largest_histogram(heights = [2,1,5,6,2,3]))
print(largest_histogram(heights = [2,4]))


# Second Approach
print(largest_histogram_2(heights = [2,1,5,6,2,3]))
print(largest_histogram_2(heights = [2,4]))

# Third Approach
print(largest_histogram_3(heights = [2,1,5,6,2,3]))
print(largest_histogram_3(heights = [2,4]))