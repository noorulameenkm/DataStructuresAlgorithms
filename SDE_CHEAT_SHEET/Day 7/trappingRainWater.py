def trappingRainWater(heights):
    totalWater = 0
    for i in range(len(heights)):
        leftMax = getMax(heights, i, "left")
        rightMax = getMax(heights, i, "right")
        minMax = min(leftMax, rightMax)

        if minMax - heights[i] > 0:
            totalWater += (minMax - heights[i])
    
    return totalWater


def getMax(heights, starting, direction):
    if direction == "right":
        end = len(heights)
        delimiter = 1
    else:
        end = -1
        delimiter = -1

    max_ = heights[starting]
    
    for k in range(starting, end, delimiter):
        max_ = max(max_, heights[k])
    
    return max_


def trappingRainWater2(heights):
    leftMax = [0 for _ in range(len(heights))]
    rightMax = [0 for _ in range(len(heights))]
    n = len(heights)
    totalWater = 0

    leftMax[0] = heights[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], heights[i])
    
    rightMax[n - 1] = heights[n - 1]
    for j in range(n - 2, -1, -1):
        rightMax[j] = max(rightMax[j + 1], heights[j])

    for k in range(n):
        if min(rightMax[k], leftMax[k]) - heights[k] > 0:
            totalWater += (min(rightMax[k], leftMax[k]) - heights[k])

    return totalWater


def trappingRainWater3(heights):
    n = len(heights)
    totalWater = 0
    leftMax = rightMax = 0
    left, right = 0, n - 1

    while left <= right:
        if heights[left] <= heights[right]:
            if heights[left] >= leftMax:
                leftMax = heights[left]
            else:
                totalWater += (leftMax - heights[left])
            
            left += 1
        else:
            if heights[right] >= rightMax:
                rightMax = heights[right]
            else:
                totalWater += (rightMax - heights[right])

            right -= 1
    
    return totalWater
    



def main():

    # Method 1
    print(trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trappingRainWater([4,2,0,3,2,5]))


    # Method 2
    print(trappingRainWater2([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trappingRainWater2([4,2,0,3,2,5]))

    # Method 2
    print(trappingRainWater3([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trappingRainWater3([4,2,0,3,2,5]))

main()