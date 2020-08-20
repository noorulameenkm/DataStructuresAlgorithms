def rearrange(nums):
    k = -1
    for i in range(len(nums)-1):
        if nums[i] >= 0:
    
            if k == -1:
                k = i + 1
            else:
                k = k + 1 
        
            while k < len(nums) and nums[k] >= 0:
                k = k + 1 

            if k < len(nums):
                temp = nums[i]
                nums[i] = nums[k]    #
                nums[k] = temp
            else:
                break
    return nums

print(f'Solution for [-1,10,20,4,5,-9,-6] is {rearrange([-1,10,20,4,5,-9,-6])}')


def rearrange2(lst):
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos


print(rearrange2([10, -1, 20, 4, 5, -9, -6]))





def rearrange3(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if (lst[curr] < 0):
            # if not the last negative number
            if (curr is not leftMostPosEle):
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


print(rearrange3([10, -1, 20, 4, 5, -9, -6]))

