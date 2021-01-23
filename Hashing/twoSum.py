def findSum(lst, k):
    # Write your code here
    dict_ = {}
    for elem in lst:
        if abs(k - elem) in dict_:
            return [elem, abs(k - elem)]
        
        dict_[elem] = True
    
    return None


print(findSum([1, 21, 3, 14, 5, 60, 7, 6],81))