def find_second_maximum(lst):
    firstMax = float('-inf')
    secondMax = float('-inf')
    # find first max
    for item in lst:
        if item > firstMax:
            firstMax = item
    # find max relative to first max
    for item in lst:
        if item != firstMax and item > secondMax:
            secondMax = item
    return secondMax


print(find_second_maximum([9, 2, 3, 6]))



def find_second_maximum_2(lst):
   if (len(lst) < 2):
       return
   # initialize the two to infinity
   max_ = second_max = float('-inf')
   for i in range(len(lst)):
       # update the max max if max value found
       if (lst[i] > max_):
           second_max = max_
           max_ = lst[i]
       # check if it is the second_max max and not equal to max
       elif (lst[i] > second_max and lst[i] != max_):
           second_max = lst[i]
   if (second_max == float('-inf')):
       return
   else:
       return second_max


print(find_second_maximum_2([9, 2, 3, 6]))

